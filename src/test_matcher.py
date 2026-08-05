from core.cve_matcher import lookup_service_cves


def main() -> None:

    cves = lookup_service_cves(
        product="Apache",
        version="2.4.7",
    )

    print(f"\nFound {len(cves)} CVEs\n")

    for cve in cves:

        print("=" * 70)
        print(f"CVE : {cve.cve_id}")
        print(f"Severity : {cve.severity}")
        print(f"CVSS : {cve.cvss_score}")


if __name__ == "__main__":
    main()