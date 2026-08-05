from core.cve import CVE


def parse_cves(data: dict) -> list[CVE]:
    """
    Convert an NVD API response into a list of CVE objects.
    """

    cves: list[CVE] = []

    vulnerabilities = data.get("vulnerabilities", [])

    for item in vulnerabilities:

        cve_data = item.get("cve", {})

        cve_id = cve_data.get("id", "Unknown")

        description = "No description available."

        descriptions = cve_data.get("descriptions", [])

        if descriptions:
            description = descriptions[0].get(
                "value",
                description,
            )

        severity = "Unknown"
        score = 0.0

        metrics = cve_data.get("metrics", {})

        if "cvssMetricV31" in metrics:

            metric = metrics["cvssMetricV31"][0]

            severity = metric["cvssData"]["baseSeverity"]

            score = metric["cvssData"]["baseScore"]

        elif "cvssMetricV30" in metrics:

            metric = metrics["cvssMetricV30"][0]

            severity = metric["cvssData"]["baseSeverity"]

            score = metric["cvssData"]["baseScore"]

        elif "cvssMetricV2" in metrics:

            metric = metrics["cvssMetricV2"][0]

            severity = metric["baseSeverity"]

            score = metric["cvssData"]["baseScore"]

        cves.append(
            CVE(
                cve_id=cve_id,
                description=description,
                severity=severity,
                cvss_score=score,
                published=cve_data.get("published", ""),
                last_modified=cve_data.get("lastModified", ""),
            )
        )

    return cves