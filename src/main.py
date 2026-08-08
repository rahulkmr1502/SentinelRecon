from core.banner_grabber import grab_banner
from core.config_loader import load_config
from core.config_factory import create_scanner_config
from core.cve_matcher import lookup_service_cves
from core.dns_resolver import resolve_target
from core.http_analyzer import analyze_http
from core.json_report_generator import generate_json_report
from core.logger import logger
from core.misconfig_detector import detect_http_misconfigurations
from core.port_scanner import scan_ports
from core.report_generator import generate_html_report
from core.risk_analyzer import analyze_risk
from core.tls_analyzer import analyze_tls
from core.validator import validate_target


def main() -> None:

    # ==========================================================
    # Target Input
    # ==========================================================

    target = input("Enter an IP address or domain: ").strip()

    if not target:
        print("Target cannot be empty.")
        return

    if not validate_target(target):
        logger.warning("Invalid target: %s", target)
        print("Invalid IP address or domain.")
        return

    # ==========================================================
    # Configuration
    # ==========================================================

    config_data = load_config()
    config = create_scanner_config(config_data)

    print("\nScanner Configuration")
    print("-" * 50)
    print(f"Start Port  : {config.start_port}")
    print(f"End Port    : {config.end_port}")
    print(f"Timeout     : {config.timeout}")
    print(f"Max Workers : {config.max_workers}")

    # ==========================================================
    # DNS Resolution
    # ==========================================================

    print(f"\nResolving '{target}'...")

    addresses = resolve_target(target)

    if not addresses:
        print("DNS resolution failed.")
        return

    print("\nResolved Addresses:")

    for address in addresses:
        print(f" - {address}")

    target_ip = next(
        (address for address in addresses if "." in address),
        None,
    )

    if target_ip is None:
        print("No IPv4 address found.")
        return

    # ==========================================================
    # Port Scanning
    # ==========================================================

    print(f"\nScanning TCP ports on {target_ip}...")
    print("Please wait...\n")

    open_ports = scan_ports(target_ip, config)

    if not open_ports:
        print("No open TCP ports found.")
        return

    print("=" * 72)
    print(f"{'PORT':<8}{'SERVICE':<15}{'PRODUCT':<20}{'VERSION'}")
    print("=" * 72)

    service_results = []
    all_findings = []
    all_cves = []

    # ==========================================================
    # Banner Grabbing & Service Fingerprinting
    # ==========================================================

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

    # ==========================================================
    # HTTP Analysis
    # ==========================================================

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

        all_findings.extend(findings)

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

    # ==========================================================
    # HTTPS / TLS Analysis
    # ==========================================================

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

    # ==========================================================
    # CVE Lookup
    # ==========================================================

    print("\nKnown Vulnerabilities")
    print("=" * 70)

    found_any = False

    for service in service_results:

        product = service["product"]
        version = service["version"]

        if product == "Unknown":
            continue

        print(f"\n{product} {version}")
        print("-" * 70)

        cves = lookup_service_cves(product, version)

        all_cves.extend(cves)

        if not cves:

            print("No known CVEs found.")
            continue

        found_any = True

        for cve in cves[:5]:

            print(f"CVE ID      : {cve.cve_id}")
            print(f"Severity    : {cve.severity}")
            print(f"CVSS Score  : {cve.cvss_score}")
            print(f"Published   : {cve.published}")
            print(f"Description : {cve.description[:120]}...")
            print("-" * 70)

    if not found_any:
        print("No known vulnerabilities found.")

    # ==========================================================
    # Risk Analysis
    # ==========================================================

    risk_summary = analyze_risk(all_cves)

    print("\nRisk Summary")
    print("=" * 70)

    print(f"Critical       : {risk_summary.critical}")
    print(f"High           : {risk_summary.high}")
    print(f"Medium         : {risk_summary.medium}")
    print(f"Low            : {risk_summary.low}")
    print(f"Informational  : {risk_summary.informational}")
    print(f"Total CVEs     : {risk_summary.total}")
    print(f"Average CVSS   : {risk_summary.average_cvss}")
    print(f"Overall Risk   : {risk_summary.overall_risk}")

    # ==========================================================
    # HTML Report
    # ==========================================================

    html_report = generate_html_report(
        target=target,
        services=service_results,
        findings=all_findings,
        cves=all_cves,
        summary=risk_summary,
    )

    print("\nHTML Report Created:")
    print(html_report)

    # ==========================================================
    # JSON Report
    # ==========================================================

    json_report = generate_json_report(
        target=target,
        services=service_results,
        findings=all_findings,
        cves=all_cves,
        summary=risk_summary,
    )

    print("\nJSON Report Created:")
    print(json_report)


if __name__ == "__main__":
    main()