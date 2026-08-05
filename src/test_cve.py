from core.cve import CVE


def main() -> None:

    cve = CVE(
        cve_id="CVE-2024-12345",
        description="Example vulnerability.",
        severity="HIGH",
        cvss_score=8.8,
        published="2024-01-15",
        last_modified="2024-02-01",
    )

    print(cve)


if __name__ == "__main__":
    main()
    