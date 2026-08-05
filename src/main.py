from core.banner_grabber import grab_banner
from core.config import ScannerConfig
from core.dns_resolver import resolve_target
from core.http_analyzer import analyze_http
from core.logger import logger
from core.misconfig_detector import detect_http_misconfigurations
from core.port_scanner import scan_ports
from core.tls_analyzer import analyze_tls
from core.validator import validate_target


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
        print("No IPv4 address found.")
        return

    print(f"\nScanning TCP ports on {target_ip}...")
    print("Please wait...\n")

    config = ScannerConfig()

    open_ports = scan_ports(target_ip, config)

    if not open_ports:
        print("No open TCP ports found.")
        return

    print("=" * 72)
    print(f"{'PORT':<8}{'SERVICE':<15}{'PRODUCT':<20}{'VERSION'}")
    print("=" * 72)

    service_results = []

    for port in open_ports:
        result = grab_banner(target_ip, port)
        service_results.append(result)

        print(
            f"{result['port']:<8}"
            f"{result['service']:<15}"
            f"{result['product']:<20}"
            f"{result['version']}"
        )

    print("=" * 72)
    print(f"Total Open Ports Found: {len(open_ports)}")

    # HTTP Analysis
    if 80 in open_ports:

        http_result = analyze_http(target_ip)

        print("\nHTTP Analysis")
        print("-" * 50)

        print(f"Status Code : {http_result['status_code']}")
        print(f"Server      : {http_result['server']}")
        print(f"Content-Type: {http_result['content_type']}")

        print("\nSecurity Header Analysis")
        print("-" * 50)

        for header, present in http_result["security_headers"].items():

            status = "✓ Present" if present else "✗ Missing"

            print(f"{header:<35} {status}")

        findings = detect_http_misconfigurations(http_result)

        if findings:

            print("\nSecurity Findings")
            print("=" * 70)

            for finding in findings:

                print(f"Title          : {finding.title}")
                print(f"Severity       : {finding.severity}")
                print(f"Category       : {finding.category}")
                print(f"Description    : {finding.description}")
                print(f"Recommendation : {finding.recommendation}")
                print("-" * 70)

    # HTTPS / TLS Analysis
    if 443 in open_ports:

        tls_result = analyze_tls(target)

        print("\nTLS Analysis")
        print("-" * 50)

        print(f"TLS Version        : {tls_result['tls_version']}")
        print(f"Issuer             : {tls_result['issuer']}")
        print(f"Subject            : {tls_result['subject']}")
        print(f"Valid From         : {tls_result['valid_from']}")
        print(f"Valid Until        : {tls_result['valid_until']}")
        print(f"Certificate Status : {tls_result['certificate_status']}")
        print(f"Days Remaining     : {tls_result['days_remaining']}")


if __name__ == "__main__":
    main()