import re
import socket

from core.logger import logger


def parse_banner(port: int, banner: str) -> dict:
    """
    Extract service, product, and version information from a banner.
    """

    result = {
        "port": port,
        "service": "Unknown",
        "product": "Unknown",
        "version": "Unknown",
        "banner": banner,
    }

    if banner.startswith("SSH-"):
        result["service"] = "SSH"

        match = re.search(r"OpenSSH[_-]([\w\.p]+)", banner)

        if match:
            result["product"] = "OpenSSH"
            result["version"] = match.group(1)

    elif banner.startswith("HTTP/"):
        result["service"] = "HTTP"

        match = re.search(r"Server:\s*([^\r\n]+)", banner)

        if match:
            server = match.group(1).strip()

            if "/" in server:
                product, version = server.split("/", 1)
                result["product"] = product
                result["version"] = version
            else:
                result["product"] = server

    return result


def grab_banner(host: str, port: int) -> dict:
    """
    Grab a service banner and return structured information.
    """

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(3)
            client.connect((host, port))

            if port == 80:
                request = (
                    f"GET / HTTP/1.1\r\n"
                    f"Host: {host}\r\n"
                    "User-Agent: SentinelRecon\r\n"
                    "Connection: close\r\n\r\n"
                )

                client.sendall(request.encode())

            chunks = []

            while True:
                try:
                    data = client.recv(4096)

                    if not data:
                        break

                    chunks.append(data)

                    if len(b"".join(chunks)) > 4096:
                        break

                except socket.timeout:
                    break

            response = b"".join(chunks).decode(errors="ignore")

            if port == 80:
                banner = response.split("\r\n\r\n")[0]
            else:
                banner = response.strip()

            logger.info("Banner on port %s:\n%s", port, banner)

            return parse_banner(port, banner)

    except Exception as error:
        logger.warning("Banner grab failed on port %s: %s", port, error)

    return {
        "port": port,
        "service": "Unknown",
        "product": "Unknown",
        "version": "Unknown",
        "banner": "Unknown",
    }