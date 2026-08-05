from core.findings import Finding
from core.severity import Severity

finding = Finding(
    title="Missing CSP",
    severity=Severity.MEDIUM.value,
    category="Security Misconfiguration",
    description="Content Security Policy header is missing.",
    recommendation="Configure the Content-Security-Policy header."
)

print(finding)