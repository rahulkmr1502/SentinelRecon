from core.cve import CVE
from core.risk_summary import RiskSummary


def analyze_risk(cves: list[CVE]) -> RiskSummary:
    """
    Analyze a list of CVEs and generate an overall risk summary.
    """

    summary = RiskSummary()

    if not cves:
        summary.overall_risk = "None"
        return summary

    total_score = 0.0

    for cve in cves:

        severity = cve.severity.upper()

        if severity == "CRITICAL":
            summary.critical += 1

        elif severity == "HIGH":
            summary.high += 1

        elif severity == "MEDIUM":
            summary.medium += 1

        elif severity == "LOW":
            summary.low += 1

        else:
            summary.informational += 1

        total_score += cve.cvss_score

    summary.total = len(cves)
    summary.average_cvss = round(total_score / summary.total, 2)

    if summary.critical > 0:
        summary.overall_risk = "Critical"

    elif summary.high > 0:
        summary.overall_risk = "High"

    elif summary.medium > 0:
        summary.overall_risk = "Medium"

    elif summary.low > 0:
        summary.overall_risk = "Low"

    else:
        summary.overall_risk = "Informational"

    return summary