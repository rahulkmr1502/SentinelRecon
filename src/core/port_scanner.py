import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

from core.config import ScannerConfig
from core.logger import logger


def scan_port(host: str, port: int, timeout: float) -> int | None:
    """
    Scan a single TCP port.
    Returns the port number if open, otherwise None.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
            scanner.settimeout(timeout)

            result = scanner.connect_ex((host, port))

            if result == 0:
                logger.info("Port %s is OPEN", port)
                return port

    except Exception as error:
        logger.error("Error scanning port %s: %s", port, error)

    return None


def scan_ports(
    host: str,
    config: ScannerConfig,
) -> list[int]:
    """
    Scan a range of TCP ports concurrently.
    """

    open_ports: list[int] = []

    with ThreadPoolExecutor(max_workers=config.max_workers) as executor:

        futures = {
            executor.submit(
                scan_port,
                host,
                port,
                config.timeout,
            ): port
            for port in range(config.start_port, config.end_port + 1)
        }

        for future in as_completed(futures):

            result = future.result()

            if result is not None:
                open_ports.append(result)

    open_ports.sort()

    return open_ports