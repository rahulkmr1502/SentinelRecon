import ipaddress
import re


DOMAIN_PATTERN = re.compile(
    r"^(?=.{1,253}$)(?!-)(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z]{2,63}$"
)


def is_valid_ip(target: str) -> bool:
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False


def is_valid_domain(target: str) -> bool:
    return bool(DOMAIN_PATTERN.fullmatch(target))


def validate_target(target: str) -> bool:
    return is_valid_ip(target) or is_valid_domain(target)