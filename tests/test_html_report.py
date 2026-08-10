from core.cve import CVE
from core.findings import Finding
from core.report_generator import generate_html_report
from core.risk_summary import RiskSummary


def main():

    services = [

        {
            "port": 22,
            "service": "SSH",
            "product": "OpenSSH",
            "version": "6.6.1p1",
        },

        {
            "port": 80,
            "service": "HTTP",
            "product": "Apache",
            "version": "2.4.7",
        },

    ]

    findings = [

        Finding(
            title="Missing CSP",
            severity="Medium",
            category="Security Misconfiguration",
            description="Content Security Policy header is missing.",
            recommendation="Configure the Content-Security-Policy header.",
        ),

        Finding(
            title="Missing HSTS",
            severity="Medium",
            category="Security Misconfiguration",
            description="HSTS header is missing.",
            recommendation="Enable Strict-Transport-Security.",
        ),

    ]

    cves = [

        CVE(
            cve_id="CVE-2021-44228",
            description="Apache Log4Shell",
            severity="CRITICAL",
            cvss_score=10.0,
            published="2021-12-10",
            last_modified="2021-12-15",
        ),

        CVE(
            cve_id="CVE-2024-12345",
            description="Example CVE",
            severity="HIGH",
            cvss_score=8.8,
            published="2024-01-15",
            last_modified="2024-01-20",
        ),

    ]

    summary = RiskSummary(
        critical=1,
        high=2,
        medium=3,
        low=1,
        informational=0,
        total=7,
        average_cvss=7.86,
        overall_risk="High",
    )

    report = generate_html_report(
        "google.com",
        services,
        findings,
        cves,
        summary,
    )

    print(f"\nReport Created:\n{report}")


if __name__ == "__main__":
    main()