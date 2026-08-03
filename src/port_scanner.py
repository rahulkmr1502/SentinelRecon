import socket

from logger import logger


def scan_ports(host: str, start_port: int = 20, end_port: int = 1024) -> list[int]:
    """
    Scan TCP ports and return a list of open ports.
    """
    open_ports: list[int] = []

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
            scanner.settimeout(0.5)

            result = scanner.connect_ex((host, port))

            if result == 0:
                open_ports.append(port)
                logger.info("Open port found: %s", port)

    return open_ports