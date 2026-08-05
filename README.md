# SentinelRecon

A professional Python-based Network Reconnaissance & Vulnerability Assessment Tool built from scratch for learning cybersecurity, networking, and software engineering.

The project focuses on understanding how reconnaissance tools work internally instead of relying on high-level libraries.

---

## Features

- Target validation
- DNS resolution
- IPv4 and IPv6 support
- Concurrent TCP port scanning
- Banner grabbing
- Service fingerprinting
- HTTP analysis
- HTTP header extraction
- Security header analysis
- TLS certificate inspection
- Certificate expiry analysis
- Logging
- Modular architecture

---

## Project Structure

```
SentinelRecon/
│
├── src/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── banner_grabber.py
│   │   ├── config.py
│   │   ├── dns_resolver.py
│   │   ├── http_analyzer.py
│   │   ├── logger.py
│   │   ├── port_scanner.py
│   │   ├── service_fingerprint.py
│   │   ├── tls_analyzer.py
│   │   └── validator.py
│   │
│   ├── test_http.py
│   └── test_tls.py
│
├── logs/
├── reports/
├── README.md
└── requirements.txt
```

---

# Milestone 1

## Features Completed

- Professional project structure
- Modular architecture
- Logging configuration
- Target validation
- GitHub repository setup

---

# Milestone 2

## Features Completed

- DNS resolution
- IPv4 support
- IPv6 support
- Logging of resolved addresses
- Graceful DNS error handling

---

# Milestone 3

## Features Completed

- Concurrent TCP port scanning
- Configurable port range
- Timeout configuration
- Open port detection
- Scan logging
- ThreadPoolExecutor implementation

---

# Milestone 4

## Features Completed

- Banner grabbing
- SSH banner detection
- HTTP banner parsing
- Product detection
- Version extraction
- Service fingerprinting
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

---

# Milestone 5

## Features Completed

- Code refactoring
- Configuration using dataclass
- Separation of concerns
- Dedicated Service Fingerprinting module
- Cleaner project architecture
- Improved modularity

---

# Milestone 6

## Features Completed

- HTTP service analysis
- Raw HTTP GET request using sockets
- HTTP response parsing
- HTTP header extraction
- Security header analysis
- HTTPS support
- TLS certificate inspection
- Certificate issuer detection
- Certificate subject detection
- Certificate validity analysis
- Days remaining calculation
- Certificate status detection
- Integration of HTTP & TLS analysis into the main scanner

### Sample Output

```text
========================================================================
PORT    SERVICE        PRODUCT             VERSION
========================================================================
80      HTTP           gws                 Unknown
443     Unknown        Unknown             Unknown
========================================================================

HTTP Analysis
--------------------------------------------------
Status Code : 301
Server      : gws
Content-Type: text/html; charset=UTF-8

Security Header Analysis
--------------------------------------------------
Strict-Transport-Security           ✗ Missing
Content-Security-Policy             ✗ Missing
X-Frame-Options                     ✓ Present
X-Content-Type-Options              ✗ Missing
Referrer-Policy                     ✗ Missing
Permissions-Policy                  ✗ Missing

TLS Analysis
--------------------------------------------------
TLS Version        : TLSv1.3
Issuer             : Google Trust Services
Subject            : *.google.com
Valid From         : Jun 29 08:37:25 2026 GMT
Valid Until        : Sep 21 08:37:24 2026 GMT
Certificate Status : Valid
Days Remaining     : 46
```

---

# Technologies Used

- Python 3
- Socket Programming
- SSL/TLS
- ThreadPoolExecutor
- Logging
- Regular Expressions
- Dataclasses

---

# Cybersecurity Concepts Covered

- DNS Resolution
- TCP/IP
- TCP Port Scanning
- Banner Grabbing
- Service Fingerprinting
- HTTP Protocol
- HTTPS
- TLS Handshake
- X.509 Certificates
- Security Headers
- Reconnaissance
- Network Enumeration

---

# Upcoming Features

- Security Misconfiguration Detection
- Severity Levels
- CVE Lookup (NIST NVD API)
- CVSS Scoring
- HTML Report Generation
- JSON Report Export
- Configuration File Support
- Unit Testing
- Integration Testing
- Docker Support
- GitHub Actions CI/CD
- Final Refactoring

---

# Learning Objectives

This project is designed to understand:

- Network reconnaissance
- TCP socket programming
- HTTP and HTTPS internals
- Service fingerprinting
- Vulnerability assessment workflow
- Secure software engineering
- Modular Python application design

---

# Author

**Rahul Kumar**

GitHub:
https://github.com/rahulkmr1502

---

## License

This project is licensed under the MIT License.