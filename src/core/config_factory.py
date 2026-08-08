from core.config import ScannerConfig


def create_scanner_config(config: dict) -> ScannerConfig:
    """
    Create ScannerConfig from loaded configuration.
    """

    scanner = config.get("scanner", {})

    return ScannerConfig(
        start_port=int(scanner.get("start_port", 1)),
        end_port=int(scanner.get("end_port", 1024)),
        timeout=float(scanner.get("timeout", 1.0)),
        max_workers=int(scanner.get("max_workers", 50)),
    )