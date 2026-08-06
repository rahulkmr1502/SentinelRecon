from core.cve import CVE
from core.risk_analyzer import analyze_risk


def main() -> None:

    cves = [

        CVE(
            cve_id="CVE-1",
            description="",
            severity="CRITICAL",
            cvss_score=9.8,
            published="",
            last_modified="",
        ),

        CVE(
            cve_id="CVE-2",
            description="",
            severity="HIGH",
            cvss_score=8.7,
            published="",
            last_modified="",
        ),

        CVE(
            cve_id="CVE-3",
            description="",
            severity="MEDIUM",
            cvss_score=5.6,
            published="",
            last_modified="",
        ),

        CVE(
            cve_id="CVE-4",
            description="",
            severity="LOW",
            cvss_score=3.2,
            published="",
            last_modified="",
        ),
    ]

    summary = analyze_risk(cves)

    print(summary)


if __name__ == "__main__":
    main()