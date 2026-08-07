from core.cve import CVE
from core.findings import Finding
from core.json_report_generator import generate_json_report
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
            recommendation="Configure the Strict-Transport-Security header.",
        ),
    ]

    cves = [
        CVE(
            cve_id="CVE-2021-44228",
            description="Example critical vulnerability.",
            severity="CRITICAL",
            cvss_score=10.0,
            published="2021-12-10",
            last_modified="2021-12-15",
        ),
        CVE(
            cve_id="CVE-2024-12345",
            description="Example high severity vulnerability.",
            severity="HIGH",
            cvss_score=8.8,
            published="2024-01-15",
            last_modified="2024-02-01",
        ),
    ]

    summary = RiskSummary(
        critical=1,
        high=1,
        medium=0,
        low=0,
        informational=0,
        total=2,
        average_cvss=9.4,
        overall_risk="Critical",
    )

    report = generate_json_report(
        target="google.com",
        services=services,
        findings=findings,
        cves=cves,
        summary=summary,
    )

    print("\nJSON Report Created:")
    print(report)


if __name__ == "__main__":
    main()