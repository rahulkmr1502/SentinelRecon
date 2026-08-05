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
- Security misconfiguration detection
- Severity classification
- Structured security findings
- Logging
- Modular architecture
- CVE lookup using NVD API
- Vulnerability intelligence

---

## Project Structure

```
SentinelRecon/
│
├── src/
│   ├── main.py
│   │
│   ├── core/
│   │  │── __init__.py
│   |  |── banner_grabber.py
│   |  |── config.py
│   |  |── cve.py
│   |  |── cve_matcher.py
│   |  |── cve_parser.py
│   |  |── dns_resolver.py
│   |  |── findings.py
│   |  |── http_analyzer.py
│   |  |── logger.py
│   |  |── misconfig_detector.py
│   |  |── nvd_client.py
│   |  |── port_scanner.py
│   |  |── service_fingerprint.py
│   |  |── severity.py
│   |  |── tls_analyzer.py
|   |  └── validator.py
│   │
│   ├── test_finding.py
│   ├── test_http.py
│   ├── test_misconfig.py
│   ├── test_severity.py
|   |──test_cve.py
|   |──test_cve_parser.py
|   |──test_matcher.py
|   |──test_nvd.py
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

```
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

# Milestone 7

## Features Completed

- Finding model using Python dataclasses
- Severity classification using Enum
- HTTP security misconfiguration detection
- Detection of missing security headers
- Structured security findings
- Security recommendations
- Integration into the main scanner

### Security Checks

- Strict-Transport-Security
- Content-Security-Policy
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy

### Sample Output

```
Security Findings
======================================================================
Title          : Missing Content-Security-Policy Header
Severity       : Medium
Category       : Security Misconfiguration
Description    : The application does not define a Content Security Policy.
Recommendation : Configure the Content-Security-Policy header.
----------------------------------------------------------------------
Title          : Missing Referrer-Policy Header
Severity       : Low
Category       : Security Misconfiguration
Description    : Sensitive URL information may leak through the Referer header.
Recommendation : Configure the Referrer-Policy header.
----------------------------------------------------------------------
```

---

# Milestone 8

## Features Completed

- NVD API integration
- CVE data model
- CVE JSON parser
- CVE lookup by detected software
- Vulnerability intelligence
- Integration with SentinelRecon

### Sample Output

```
Known Vulnerabilities
======================================================================

Apache 2.4.7
----------------------------------------------------------------------
CVE ID      : CVE-2024-38474
Severity    : CRITICAL
CVSS Score  : 9.8
Published   : 2024-07-01
Description : ...
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
- Requests
- REST APIs
- JSON

---

# Cybersecurity Concepts Covered

- DNS Resolution
- TCP/IP
- TCP Port Scanning
- Concurrent Network Scanning
- Banner Grabbing
- Service Fingerprinting
- HTTP Protocol
- HTTPS
- TLS Handshake
- X.509 Certificates
- Security Headers
- Security Misconfiguration Detection
- Vulnerability Assessment
- Reconnaissance
- Network Enumeration
- Common Vulnerabilities and Exposures (CVE)
- National Vulnerability Database (NVD)
- Vulnerability Intelligence
- Software Enumeration

---

# Upcoming Features

- CVSS Risk Prioritization
- HTML Report Generation
- JSON Report Export
- Configuration File Support
- Unit Testing
- Integration Testing
- Docker Support
- GitHub Actions CI/CD
- Final Refactoring
- Final Documentation

---

# Learning Objectives

This project is designed to understand:

- Network reconnaissance
- TCP socket programming
- Concurrent network scanning
- HTTP and HTTPS internals
- Service fingerprinting
- TLS certificate inspection
- Security header analysis
- Security misconfiguration detection
- Vulnerability assessment workflow
- Secure software engineering
- Modular Python application design

---

# Project Progress

| Milestone | Status |
|-----------|--------|
| Project Setup | ✅ |
| DNS Resolution | ✅ |
| Concurrent TCP Port Scanner | ✅ |
| Banner Grabbing & Service Fingerprinting | ✅ |
| Architecture Refactoring | ✅ |
| HTTP & TLS Analysis | ✅ |
| Security Misconfiguration Detection | ✅ |
| CVE Lookup (NVD API) | ✅ |
| CVSS Risk Prioritization | ⏳ |
| HTML Report Generation | ⏳ |
| JSON Export | ⏳ |
| Docker Support | ⏳ |
| GitHub Actions CI | ⏳ |
| Final Documentation | ⏳ |

---

# Author

**Rahul Kumar**

GitHub:
https://github.com/rahulkmr1502

---

## License

This project is licensed under the MIT License.