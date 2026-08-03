from dns_resolver import resolve_target
from logger import logger
from validator import validate_target


def main() -> None:
    target = input("Enter an IP address or domain: ").strip()

    if not target:
        print("Target cannot be empty.")
        return

    if not validate_target(target):
        logger.warning("Invalid target: %s", target)
        print("Invalid IP address or domain.")
        return

    print(f"\nResolving '{target}'...")

    addresses = resolve_target(target)

    if not addresses:
        print("DNS resolution failed.")
        return

    print("\nResolved Addresses:")

    for address in addresses:
        print(f" - {address}")

    print(f"\nTotal addresses found: {len(addresses)}")


if __name__ == "__main__":
    main()