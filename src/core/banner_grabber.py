import socket

from core.logger import logger
from core.service_fingerprint import fingerprint_service


def grab_banner(host: str, port: int) -> dict:
    """
    Connect to a service, grab its banner,
    and return fingerprinted information.
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

            return fingerprint_service(port, banner)

    except Exception as error:
        logger.warning("Banner grab failed on port %s: %s", port, error)

    return {
        "port": port,
        "service": "Unknown",
        "product": "Unknown",
        "version": "Unknown",
        "banner": "Unknown",
    }