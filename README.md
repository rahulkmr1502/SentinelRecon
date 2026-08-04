# SentinelRecon

A Python-based cybersecurity tool for network reconnaissance and vulnerability assessment.

## Milestone 1

### Features Completed
- ✅ Project structure created
- ✅ Logging configured
- ✅ IP address validation
- ✅ Domain validation
- ✅ Target validation

## Project Structure

```
SentinelRecon/
│
├── src/
│   ├── __init__.py
│   ├── dns_resolver.py
│   ├── port_scanner.py
│   ├── main.py
│   ├── validator.py
│   └── logger.py
│
├── reports/
├── logs/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

1. Create a virtual environment.
2. Activate it.
3. Run:

```bash
python src/main.py
```

## Sample Output

```
Enter an IP address or domain: google.com
Target 'google.com' is valid.
```

## Tech Stack

- Python 3
- Logging
- pathlib
- ipaddress
- Regular Expressions (re)
- socket
- DNS Resolution 
- TCP networking

---
**Project Status:** Milestone 1 Complete 🚀

## Milestone 2

### Features Completed

- DNS resolution
- IPv4 support
- IPv6 support
- Logging of resolved addresses
- Graceful DNS error handling

## Milestone 3

### Features Completed

- TCP port scanning
- Configurable port range
- Open port detection
- Scan logging

## Milestone 4 – Banner Grabbing & Service Fingerprinting

### Features Implemented

- Banner grabbing for open TCP services
- HTTP header parsing
- SSH banner detection
- Service fingerprinting
- Product detection
- Version extraction
- Structured scan results
- Professional tabular output

### Sample Output

```text
========================================================================
PORT    SERVICE        PRODUCT             VERSION
========================================================================
22      SSH            OpenSSH             6.6.1p1
80      HTTP           Apache              2.4.7 (Ubuntu)
========================================================================
```

## Milestone 5 – Concurrent TCP Port Scanning

### Features Implemented

- Concurrent TCP port scanning using `ThreadPoolExecutor`
- Configurable scanner settings using `ScannerConfig`
- Multi-threaded port scanning for improved performance
- Configurable scan timeout
- Configurable worker threads
- Modular scanner architecture
- Automatic sorting of discovered open ports
- Enhanced logging for concurrent scans
- Type hints for improved code quality
- Improved code organization with `core` package