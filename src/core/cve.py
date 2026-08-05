from dataclasses import dataclass


@dataclass(slots=True)
class CVE:
    """
    Represents a vulnerability returned by the NVD API.
    """

    cve_id: str
    description: str
    severity: str
    cvss_score: float
    published: str
    last_modified: str