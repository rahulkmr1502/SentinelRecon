from dataclasses import dataclass


@dataclass(slots=True)
class Finding:
    """
    Represents a security finding produced by the scanner.
    """

    title: str
    severity: str
    category: str
    description: str
    recommendation: str