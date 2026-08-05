from enum import Enum


class Severity(Enum):
    """
    Standard severity levels used by SentinelRecon.
    """

    INFORMATIONAL = "Informational"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"