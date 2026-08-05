from core.findings import Finding
from core.severity import Severity


def detect_http_misconfigurations(http_result: dict) -> list[Finding]:
    """
    Detect HTTP security misconfigurations.
    """

    findings: list[Finding] = []

    security_headers = http_result.get("security_headers", {})

    rules = {
        "Strict-Transport-Security": (
            "Missing Strict-Transport-Security Header",
            "The application does not enforce HTTPS using HSTS.",
            "Configure the Strict-Transport-Security header.",
            Severity.MEDIUM,
        ),
        "Content-Security-Policy": (
            "Missing Content-Security-Policy Header",
            "The application does not define a Content Security Policy.",
            "Configure the Content-Security-Policy header.",
            Severity.MEDIUM,
        ),
        "X-Frame-Options": (
            "Missing X-Frame-Options Header",
            "The application may be vulnerable to clickjacking.",
            "Configure the X-Frame-Options header.",
            Severity.MEDIUM,
        ),
        "X-Content-Type-Options": (
            "Missing X-Content-Type-Options Header",
            "Browsers may MIME-sniff responses.",
            "Configure the X-Content-Type-Options header.",
            Severity.LOW,
        ),
        "Referrer-Policy": (
            "Missing Referrer-Policy Header",
            "Sensitive URL information may leak through the Referer header.",
            "Configure the Referrer-Policy header.",
            Severity.LOW,
        ),
        "Permissions-Policy": (
            "Missing Permissions-Policy Header",
            "Browser features are not explicitly restricted.",
            "Configure the Permissions-Policy header.",
            Severity.LOW,
        ),
    }

    for header, present in security_headers.items():

        if present:
            continue

        title, description, recommendation, severity = rules[header]

        findings.append(
            Finding(
                title=title,
                severity=severity.value,
                category="Security Misconfiguration",
                description=description,
                recommendation=recommendation,
            )
        )

    return findings