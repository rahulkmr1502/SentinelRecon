from core.nvd_client import search_cves


def main() -> None:

    data = search_cves("Apache")

    if not data:
        print("Request failed.")
        return

    print("Request Successful!\n")

    print("Results Found:")
    print(data["totalResults"])


if __name__ == "__main__":
    main()