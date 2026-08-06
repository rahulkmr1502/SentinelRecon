from dataclasses import dataclass


@dataclass(slots=True)
class RiskSummary:
    """
    Overall vulnerability risk summary.
    """

    critical: int = 0
    high: int = 0
    medium: int = 0
    low: int = 0
    informational: int = 0

    total: int = 0

    average_cvss: float = 0.0

    overall_risk: str = "Unknown"