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
        print("\nNo IPv4 address found for scanning.")
        return

    print(f"\nScanning TCP ports on {target_ip}...")
    print("Please wait...\n")

    # Scan only ports 20-100 for now (faster while learning)
    open_ports = scan_ports(target_ip, 20, 100)

    if open_ports:
        print("Open TCP Ports:")
        for port in open_ports:
            print(f" - {port}")

        print(f"\nTotal Open Ports Found: {len(open_ports)}")

    else:
        print("No open TCP ports found in the scanned range.")


if __name__ == "__main__":
    main()