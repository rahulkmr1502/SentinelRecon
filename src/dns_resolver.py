import socket

from logger import logger


def resolve_target(target: str) -> list[str]:
    """
    Resolve a domain or IP address to a list of IP addresses.
    """

    try:
        address_info = socket.getaddrinfo(
            target,
            None,
            family=socket.AF_UNSPEC,
            type=socket.SOCK_STREAM,
        )

        addresses = sorted({info[4][0] for info in address_info})

        logger.info("Resolved '%s' to %s", target, addresses)

        return addresses

    except socket.gaierror:
        logger.error("DNS resolution failed for '%s'", target)
        return []