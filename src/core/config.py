from dataclasses import dataclass


@dataclass
class ScannerConfig:
    start_port: int = 1
    end_port: int = 1024
    timeout: float = 1.0
    max_workers: int = 50