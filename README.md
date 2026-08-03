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
network-recon-tool/
│
├── src/
│   ├── __init__.py
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

---
**Project Status:** Milestone 1 Complete 🚀

## Milestone 2

### Features Completed

- DNS resolution
- IPv4 support
- IPv6 support
- Logging of resolved addresses
- Graceful DNS error handling
