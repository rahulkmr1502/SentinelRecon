import re


def fingerprint_service(port: int, banner: str) -> dict:
    """
    Identify the service, product and version from a banner.
    """

    result = {
        "port": port,
        "service": "Unknown",
        "product": "Unknown",
        "version": "Unknown",
        "banner": banner,
    }

    # SSH
    if banner.startswith("SSH-"):

        result["service"] = "SSH"

        match = re.search(r"OpenSSH[_-]([\w\.p]+)", banner)

        if match:
            result["product"] = "OpenSSH"
            result["version"] = match.group(1)

    # HTTP
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