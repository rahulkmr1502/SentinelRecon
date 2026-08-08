import json
from pathlib import Path


DEFAULT_CONFIG = {
    "scanner": {
        "start_port": 1,
        "end_port": 1024,
        "timeout": 1.0,
        "max_workers": 50,
    }
}


def load_config(config_path: str = "config.json") -> dict:
    """
    Load scanner configuration from a JSON file.
    """

    path = Path(config_path)

    if not path.exists():
        print("Configuration file not found.")
        print("Using default configuration.")

        return DEFAULT_CONFIG.copy()

    try:
        with path.open("r", encoding="utf-8") as file:
            config = json.load(file)

    except json.JSONDecodeError:
        print("Invalid configuration file.")
        print("Using default configuration.")

        return DEFAULT_CONFIG.copy()

    scanner_config = config.get("scanner", {})

    return {
        "scanner": {
            "start_port": scanner_config.get(
                "start_port",
                DEFAULT_CONFIG["scanner"]["start_port"],
            ),
            "end_port": scanner_config.get(
                "end_port",
                DEFAULT_CONFIG["scanner"]["end_port"],
            ),
            "timeout": scanner_config.get(
                "timeout",
                DEFAULT_CONFIG["scanner"]["timeout"],
            ),
            "max_workers": scanner_config.get(
                "max_workers",
                DEFAULT_CONFIG["scanner"]["max_workers"],
            ),
        }
    }