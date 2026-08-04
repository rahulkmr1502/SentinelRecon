from banner_grabber import grab_banner
from dns_resolver import resolve_target
from logger import logger
from port_scanner import scan_ports
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

    # Select the first IPv4 address
    target_ip = next(
        (address for address in addresses if "." in address),
        None,
    )

    if target_ip is None:
        print("No IPv4 address found for scanning.")
        return

    print(f"\nScanning TCP ports on {target_ip}...")
    print("Please wait...\n")

    open_ports = scan_ports(target_ip, 20, 100)

    if not open_ports:
        print("No open TCP ports found.")
        return

    print("=" * 72)
    print(f"{'PORT':<8}{'SERVICE':<15}{'PRODUCT':<20}{'VERSION'}")
    print("=" * 72)

    for port in open_ports:
        result = grab_banner(target_ip, port)

        print(
            f"{result['port']:<8}"
            f"{result['service']:<15}"
            f"{result['product']:<20}"
            f"{result['version']}"
        )

    print("=" * 72)
    print(f"Total Open Ports Found: {len(open_ports)}")


if __name__ == "__main__":
    main()