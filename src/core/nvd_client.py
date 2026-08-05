import requests

from core.logger import logger


NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def search_cves(keyword: str) -> dict:
    """
    Query the NVD API using a keyword.
    """

    try:
        response = requests.get(
            NVD_API_URL,
            params={
                "keywordSearch": keyword,
                "resultsPerPage": 5,
            },
            timeout=15,
        )

        response.raise_for_status()

        logger.info("Fetched CVEs for %s", keyword)

        return response.json()

    except requests.RequestException as error:
        logger.error("NVD API request failed: %s", error)
        return {}