from core.cve_parser import parse_cves
from core.nvd_client import search_cves


def main() -> None:

    data = search_cves("Apache")

    cves = parse_cves(data)

    print(f"\nFound {len(cves)} CVEs\n")

    for cve in cves:

        print("=" * 70)
        print(f"CVE ID      : {cve.cve_id}")
        print(f"Severity    : {cve.severity}")
        print(f"CVSS Score  : {cve.cvss_score}")
        print(f"Published   : {cve.published}")
        print(f"Modified    : {cve.last_modified}")
        print(f"Description : {cve.description[:150]}...")


if __name__ == "__main__":
    main()