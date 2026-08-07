import json
from datetime import datetime
from pathlib import Path

from core.cve import CVE
from core.findings import Finding
from core.risk_summary import RiskSummary


def create_json_report_directory() -> Path:
    """
    Create the reports directory if it doesn't exist.
    """

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    return reports_dir


def generate_json_report_filename(target: str) -> Path:
    """
    Generate a timestamped JSON report filename.
    """

    reports_dir = create_json_report_directory()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return reports_dir / f"{target}_{timestamp}.json"


def findings_to_dict(findings: list[Finding]) -> list[dict]:
    """
    Convert Finding objects into JSON-compatible dictionaries.
    """

    return [
        {
            "title": finding.title,
            "severity": finding.severity,
            "category": finding.category,
            "description": finding.description,
            "recommendation": finding.recommendation,
        }
        for finding in findings
    ]


def cves_to_dict(cves: list[CVE]) -> list[dict]:
    """
    Convert CVE objects into JSON-compatible dictionaries.
    """

    return [
        {
            "cve_id": cve.cve_id,
            "severity": cve.severity,
            "cvss_score": cve.cvss_score,
            "published": cve.published,
            "last_modified": cve.last_modified,
            "description": cve.description,
        }
        for cve in cves
    ]


def risk_summary_to_dict(summary: RiskSummary) -> dict:
    """
    Convert RiskSummary object into a JSON-compatible dictionary.
    """

    return {
        "critical": summary.critical,
        "high": summary.high,
        "medium": summary.medium,
        "low": summary.low,
        "informational": summary.informational,
        "total": summary.total,
        "average_cvss": summary.average_cvss,
        "overall_risk": summary.overall_risk,
    }


def generate_json_report(
    target: str,
    services: list[dict],
    findings: list[Finding],
    cves: list[CVE],
    summary: RiskSummary,
) -> Path:
    """
    Generate a complete JSON vulnerability assessment report.
    """

    report_path = generate_json_report_filename(target)

    report_data = {
        "target": target,
        "generated_at": datetime.now().isoformat(),
        "services": services,
        "security_findings": findings_to_dict(findings),
        "known_vulnerabilities": cves_to_dict(cves),
        "risk_summary": risk_summary_to_dict(summary),
    }

    report_path.write_text(
        json.dumps(
            report_data,
            indent=4,
        ),
        encoding="utf-8",
    )

    return report_path