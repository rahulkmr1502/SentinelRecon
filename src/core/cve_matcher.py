from core.cve import CVE
from core.cve_parser import parse_cves
from core.nvd_client import search_cves


def lookup_service_cves(product: str, version: str) -> list[CVE]:
    """
    Look up CVEs for a detected product and version.
    """

    if product == "Unknown":
        return []

    keyword = product

    if version and version != "Unknown":
        keyword += f" {version}"

    data = search_cves(keyword)

    if not data:
        return []

    return parse_cves(data)