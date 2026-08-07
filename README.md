# SentinelRecon

A professional Python-based Network Reconnaissance & Vulnerability Assessment Tool built from scratch for learning cybersecurity, networking, and software engineering.

SentinelRecon is designed to demonstrate how a reconnaissance and vulnerability assessment workflow works internally using Python socket programming, HTTP/TLS analysis, service fingerprinting, CVE intelligence, risk assessment, and automated security reporting.

> **Important:** Use SentinelRecon only against systems that you own or have explicit authorization to assess.

---

# Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Complete Workflow](#complete-workflow)
- [Project Structure](#project-structure)
- [Milestone 1 - Project Setup](#milestone-1---project-setup)
- [Milestone 2 - DNS Resolution](#milestone-2---dns-resolution)
- [Milestone 3 - TCP Port Scanner](#milestone-3---tcp-port-scanner)
- [Milestone 4 - Banner Grabbing](#milestone-4---banner-grabbing)
- [Milestone 5 - Code Refactoring](#milestone-5---code-refactoring)
- [Milestone 6 - HTTP and TLS Analysis](#milestone-6---http-and-tls-analysis)
- [Milestone 7 - Security Misconfiguration Detection](#milestone-7---security-misconfiguration-detection)
- [Milestone 8 - CVE Lookup](#milestone-8---cve-lookup)
- [Milestone 9 - Risk Assessment](#milestone-9---risk-assessment)
- [Milestone 10 - HTML Reporting](#milestone-10---html-reporting)
- [Milestone 11 - JSON Reporting](#milestone-11---json-reporting)
- [Technologies Used](#technologies-used)
- [Cybersecurity Concepts Covered](#cybersecurity-concepts-covered)
- [Reports](#reports)
- [Installation](#installation)
- [Usage](#usage)
- [Learning Objectives](#learning-objectives)
- [Project Progress](#project-progress)
- [Upcoming Features](#upcoming-features)
- [Responsible Use](#responsible-use)
- [Author](#author)
- [License](#license)

---

# Overview

SentinelRecon performs a modular network reconnaissance and vulnerability assessment workflow.

The scanner accepts an IP address or domain and performs:

1. Target validation
2. DNS resolution
3. IPv4/IPv6 discovery
4. Concurrent TCP port scanning
5. Banner grabbing
6. Service fingerprinting
7. HTTP analysis
8. Security header analysis
9. TLS certificate inspection
10. Security misconfiguration detection
11. CVE lookup
12. CVSS analysis
13. Risk assessment
14. HTML report generation
15. JSON report generation

The project was developed milestone-by-milestone to understand the internal implementation of common cybersecurity reconnaissance and vulnerability assessment functionality.

---

# Features

- Target validation
- DNS resolution
- IPv4 support
- IPv6 support
- Concurrent TCP port scanning
- Configurable port range
- Configurable timeout
- Open port detection
- TCP socket programming
- Banner grabbing
- SSH banner detection
- HTTP banner parsing
- Product detection
- Version extraction
- Service fingerprinting
- HTTP service analysis
- HTTP response parsing
- HTTP header extraction
- Security header analysis
- HTTPS support
- TLS certificate inspection
- TLS version detection
- Certificate issuer detection
- Certificate subject detection
- Certificate validity analysis
- Certificate expiry analysis
- Security misconfiguration detection
- Security severity classification
- Security recommendations
- NIST NVD API integration
- CVE lookup
- CVE response parsing
- Product and version matching
- CVSS score extraction
- CVE severity extraction
- Vulnerability enumeration
- Risk summary
- Average CVSS calculation
- Overall risk calculation
- HTML report generation
- JSON report generation
- Machine-readable security reports
- Logging
- Modular architecture

---

# Complete Workflow

```text
                         SentinelRecon
                              |
                              v
                     Target Input
                              |
                              v
                    Target Validation
                              |
                              v
                       DNS Resolution
                              |
                     +--------+--------+
                     |                 |
                     v                 v
                   IPv4              IPv6
                     |
                     v
             TCP Port Scanning
                     |
                     v
             Open Port Detection
                     |
                     v
              Banner Grabbing
                     |
                     v
           Service Fingerprinting
                     |
          +----------+----------+
          |                     |
          v                     v
    HTTP Analysis          TLS Analysis
          |                     |
          v                     v
 Security Headers       X.509 Certificate
    Analysis                Inspection
          |                     |
          +----------+----------+
                     |
                     v
      Security Misconfiguration
             Detection
                     |
                     v
                CVE Lookup
                     |
                     v
               CVSS Analysis
                     |
                     v
              Risk Assessment
                     |
              +------+------+
              |             |
              v             v
         HTML Report    JSON Report
```

---

# Project Structure

```text
SentinelRecon/
│
├── src/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── banner_grabber.py
│   │   ├── config.py
│   │   ├── cve.py
│   │   ├── cve_matcher.py
│   │   ├── cve_parser.py
│   │   ├── dns_resolver.py
│   │   ├── findings.py
│   │   ├── http_analyzer.py
│   │   ├── json_report_generator.py
│   │   ├── logger.py
│   │   ├── misconfig_detector.py
│   │   ├── nvd_client.py
│   │   ├── port_scanner.py
│   │   ├── report_generator.py
│   │   ├── risk_analyzer.py
│   │   ├── risk_summary.py
│   │   ├── service_fingerprint.py
│   │   ├── severity.py
│   │   ├── tls_analyzer.py
│   │   └── validator.py
│   │
│   ├── test_cve_parser.py
│   ├── test_http.py
│   ├── test_json_report.py
│   └── test_tls.py
│
├── logs/
│
├── reports/
│   ├── *.html
│   └── *.json
│
├── README.md
└── requirements.txt
```

---

# Milestone 1 - Project Setup

## Features Completed

- Professional project structure
- Modular architecture
- Logging configuration
- Target validation
- GitHub repository setup
- Initial Python scanner structure

## Main Concepts

- Python project organization
- Modules
- Packages
- Logging
- Input validation
- Git/GitHub workflow

---

# Milestone 2 - DNS Resolution

## Features Completed

- DNS resolution
- IPv4 address resolution
- IPv6 address resolution
- Multiple address handling
- Logging of resolved addresses
- Graceful DNS error handling

## Sample Output

```text
Enter an IP address or domain: google.com

Resolving 'google.com'...

Resolved Addresses:
 - 192.178.158.100
 - 192.178.158.101
 - 192.178.158.102
 - 192.178.158.113
 - 192.178.158.138
 - 192.178.158.139
 - 2404:6800:4002:81a::200e
```

---

# Milestone 3 - TCP Port Scanner

## Features Completed

- TCP socket scanning
- Concurrent scanning
- Configurable port range
- Timeout configuration
- Open port detection
- Scan logging
- ThreadPoolExecutor implementation

## Sample Output

```text
Scanning TCP ports on 192.178.158.100...
Please wait...

========================================================================
PORT    SERVICE        PRODUCT             VERSION
========================================================================
80      HTTP           gws                 Unknown
443     Unknown        Unknown             Unknown
========================================================================
Total Open Ports Found: 2
```

---

# Milestone 4 - Banner Grabbing

## Features Completed

- TCP banner grabbing
- SSH banner detection
- HTTP banner detection
- Product detection
- Version extraction
- Service identification
- Structured service results
- Professional tabular output

## Sample Output

```text
========================================================================
PORT    SERVICE        PRODUCT             VERSION
========================================================================
22      SSH            OpenSSH             6.6.1p1
80      HTTP           Apache              2.4.7
========================================================================
```

The scanner converts raw service banners into structured information:

```text
Port
Service
Product
Version
```

This information is later used for vulnerability matching.

---

# Milestone 5 - Code Refactoring

## Features Completed

- Code refactoring
- Separation of concerns
- Configuration using dataclasses
- Dedicated service fingerprinting
- Modular scanner components
- Cleaner imports
- Improved project architecture
- Reduced coupling between modules

## Architecture

The scanner was separated into dedicated modules for:

```text
Validation
DNS
Port Scanning
Banner Grabbing
Service Fingerprinting
HTTP Analysis
TLS Analysis
CVE Processing
Risk Analysis
Reporting
Logging
```

This makes the project easier to maintain and extend.

---

# Milestone 6 - HTTP and TLS Analysis

## HTTP Features

- Raw HTTP GET requests using sockets
- HTTP response parsing
- HTTP status code extraction
- Server header extraction
- Content-Type extraction
- Security header analysis

## TLS Features

- HTTPS support
- TLS connection
- TLS version detection
- Certificate inspection
- Certificate issuer detection
- Certificate subject detection
- Certificate validity dates
- Certificate expiry analysis
- Days remaining calculation
- Certificate status detection

## Sample Output

```text
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

# Milestone 7 - Security Misconfiguration Detection

## Features Completed

- Security header validation
- Missing HSTS detection
- Missing CSP detection
- Missing X-Content-Type-Options detection
- Missing Referrer-Policy detection
- Missing Permissions-Policy detection
- Security severity classification
- Security recommendations
- Structured Finding objects

## Security Headers Checked

```text
Strict-Transport-Security
Content-Security-Policy
X-Frame-Options
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
```

## Sample Output

```text
Security Findings
======================================================================
Title          : Missing Strict-Transport-Security Header
Severity       : Medium
Category       : Security Misconfiguration
Description    : The application does not enforce HTTPS using HSTS.
Recommendation : Configure the Strict-Transport-Security header.
----------------------------------------------------------------------

Title          : Missing Content-Security-Policy Header
Severity       : Medium
Category       : Security Misconfiguration
Description    : The application does not define a Content Security Policy.
Recommendation : Configure the Content-Security-Policy header.
----------------------------------------------------------------------

Title          : Missing X-Content-Type-Options Header
Severity       : Low
Category       : Security Misconfiguration
Description    : Browsers may MIME-sniff responses.
Recommendation : Configure the X-Content-Type-Options header.
----------------------------------------------------------------------
```

---

# Milestone 8 - CVE Lookup

## Features Completed

- NIST NVD API integration
- CVE search
- CVE response parsing
- CVE data modeling
- Product matching
- Version matching
- CVSS score extraction
- Severity extraction
- Published date extraction
- Last modified date extraction
- Vulnerability enumeration

## CVE Data

Each CVE contains:

```text
CVE ID
Description
Severity
CVSS Score
Published Date
Last Modified Date
```

## Sample Output

```text
Known Vulnerabilities
======================================================================

gws Unknown
----------------------------------------------------------------------

CVE ID      : CVE-2000-0720
Severity    : MEDIUM
CVSS Score  : 5.0
Published   : 2000-10-20T04:00:00.000
Description : news.cgi in GWScripts News Publisher does not properly
authenticate requests...
----------------------------------------------------------------------

CVE ID      : CVE-2014-1962
Severity    : MEDIUM
CVSS Score  : 5.0
Published   : 2014-02-14T15:55:07.500
Description : Gwsync in SAP CRM 7.02 EHP 2 allows remote attackers...
----------------------------------------------------------------------
```

---

# Milestone 9 - Risk Assessment

## Features Completed

- RiskSummary model
- CVSS score analysis
- Severity counting
- Critical count
- High count
- Medium count
- Low count
- Informational count
- Total CVE count
- Average CVSS calculation
- Overall risk calculation

## Risk Summary

The scanner converts CVE information into an overall security risk assessment.

## Sample Output

```text
Risk Summary
======================================================================
Critical       : 0
High           : 0
Medium         : 3
Low            : 0
Informational  : 0
Total CVEs     : 3
Average CVSS   : 5.17
Overall Risk   : Medium
```

Example risk result:

```text
RiskSummary(
    critical=2,
    high=5,
    medium=4,
    low=1,
    informational=0,
    total=12,
    average_cvss=8.1,
    overall_risk='High'
)
```

---

# Milestone 10 - HTML Reporting

## Features Completed

- HTML report generation
- Timestamped report filenames
- Reports directory
- Target information
- Service information
- Security findings
- Known vulnerabilities
- CVSS information
- Risk summary
- Human-readable security report

## Sample Output

```text
Report Created:

reports/google.com_20260806_092025.html
```

## HTML Report Contents

```text
Target Information
        ↓
Scan Information
        ↓
Detected Services
        ↓
Security Findings
        ↓
Known Vulnerabilities
        ↓
Risk Summary
```

HTML reports are intended for human-readable security assessment results.

---

# Milestone 11 - JSON Reporting

## Features Completed

- JSON report generation
- Timestamped JSON filenames
- Target information export
- Scan timestamp export
- Service information export
- Security findings export
- CVE information export
- CVSS score export
- Risk summary export
- Overall risk export
- Machine-readable report
- Integration with the main scanner

## JSON Report Structure

```text
JSON Report
│
├── target
├── generated_at
├── services
│   ├── port
│   ├── service
│   ├── product
│   └── version
│
├── security_findings
│   ├── title
│   ├── severity
│   ├── category
│   ├── description
│   └── recommendation
│
├── known_vulnerabilities
│   ├── cve_id
│   ├── severity
│   ├── cvss_score
│   ├── published
│   ├── last_modified
│   └── description
│
└── risk_summary
    ├── critical
    ├── high
    ├── medium
    ├── low
    ├── informational
    ├── total
    ├── average_cvss
    └── overall_risk
```

## Sample JSON Report

```json
{
    "target": "google.com",
    "generated_at": "2026-08-07T20:22:58.978707",
    "services": [
        {
            "port": 22,
            "service": "SSH",
            "product": "OpenSSH",
            "version": "6.6.1p1"
        },
        {
            "port": 80,
            "service": "HTTP",
            "product": "Apache",
            "version": "2.4.7"
        }
    ],
    "security_findings": [
        {
            "title": "Missing CSP",
            "severity": "Medium",
            "category": "Security Misconfiguration",
            "description": "Content Security Policy header is missing.",
            "recommendation": "Configure the Content-Security-Policy header."
        },
        {
            "title": "Missing HSTS",
            "severity": "Medium",
            "category": "Security Misconfiguration",
            "description": "HSTS header is missing.",
            "recommendation": "Configure the Strict-Transport-Security header."
        }
    ],
    "known_vulnerabilities": [
        {
            "cve_id": "CVE-2021-44228",
            "severity": "CRITICAL",
            "cvss_score": 10.0,
            "published": "2021-12-10",
            "last_modified": "2021-12-15",
            "description": "Example critical vulnerability."
        },
        {
            "cve_id": "CVE-2024-12345",
            "severity": "HIGH",
            "cvss_score": 8.8,
            "published": "2024-01-15",
            "last_modified": "2024-02-01",
            "description": "Example high severity vulnerability."
        }
    ],
    "risk_summary": {
        "critical": 1,
        "high": 1,
        "medium": 0,
        "low": 0,
        "informational": 0,
        "total": 2,
        "average_cvss": 9.4,
        "overall_risk": "Critical"
    }
}
```

---

# Complete Scanner Output

A complete scan can produce results across all major assessment stages.

```text
Enter an IP address or domain: google.com

Resolving 'google.com'...

Resolved Addresses:
 - 192.178.158.100
 - 192.178.158.101
 - 192.178.158.102
 - 192.178.158.113
 - 192.178.158.138
 - 192.178.158.139
 - 2404:6800:4002:81a::200e

Scanning TCP ports on 192.178.158.100...
Please wait...

========================================================================
PORT    SERVICE        PRODUCT             VERSION
========================================================================
80      HTTP           gws                 Unknown
443     Unknown        Unknown             Unknown
========================================================================
Total Open Ports Found: 2

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

Security Findings
======================================================================
Title          : Missing Strict-Transport-Security Header
Severity       : Medium
Category       : Security Misconfiguration
Description    : The application does not enforce HTTPS using HSTS.
Recommendation : Configure the Strict-Transport-Security header.
----------------------------------------------------------------------

Title          : Missing Content-Security-Policy Header
Severity       : Medium
Category       : Security Misconfiguration
Description    : The application does not define a Content Security Policy.
Recommendation : Configure the Content-Security-Policy header.
----------------------------------------------------------------------

TLS Analysis
--------------------------------------------------
TLS Version        : TLSv1.3
Issuer             : Google Trust Services
Subject            : *.google.com
Valid From         : Jun 29 08:37:25 2026 GMT
Valid Until        : Sep 21 08:37:24 2026 GMT
Certificate Status : Valid
Days Remaining     : 46

Known Vulnerabilities
======================================================================

gws Unknown
----------------------------------------------------------------------

CVE ID      : CVE-2000-0720
Severity    : MEDIUM
CVSS Score  : 5.0
Published   : 2000-10-20T04:00:00.000
Description : Example vulnerability description...
----------------------------------------------------------------------

Risk Summary
======================================================================
Critical       : 0
High           : 0
Medium         : 3
Low            : 0
Informational  : 0
Total CVEs     : 3
Average CVSS   : 5.17
Overall Risk   : Medium

HTML Report Created:
reports/google.com_20260806_092025.html

JSON Report Created:
reports/google.com_20260807_XXXXXX.json
```

---

# Reports

SentinelRecon generates two report formats.

```text
reports/
│
├── google.com_20260806_092025.html
├── google.com_20260807_XXXXXX.html
└── google.com_20260807_XXXXXX.json
```

## HTML Report

The HTML report is designed for human-readable security analysis.

It contains:

- Target information
- Scan information
- Detected services
- Open ports
- HTTP analysis
- TLS analysis
- Security findings
- Known vulnerabilities
- CVSS information
- Risk summary

## JSON Report

The JSON report is designed for machine-readable security data.

It contains:

- Target
- Timestamp
- Services
- Security findings
- Known vulnerabilities
- CVE metadata
- CVSS scores
- Risk summary
- Overall risk

JSON reports can later be used for:

- Security dashboards
- Automation
- Data processing
- API integrations
- SIEM integrations
- Vulnerability management systems

---

# Technologies Used

- Python 3
- Socket Programming
- SSL/TLS
- ThreadPoolExecutor
- Logging
- Regular Expressions
- Dataclasses
- HTTP
- NIST NVD API
- JSON
- HTML5
- CSS3
- pathlib

---

# Cybersecurity Concepts Covered

- Network Reconnaissance
- Network Enumeration
- DNS Resolution
- IPv4
- IPv6
- TCP/IP
- TCP Port Scanning
- TCP Socket Programming
- Banner Grabbing
- Service Fingerprinting
- HTTP Protocol
- HTTPS
- HTTP Headers
- Security Headers
- TLS Handshake
- TLS Versions
- X.509 Certificates
- Certificate Validation
- Security Misconfiguration
- Vulnerability Assessment
- CVE
- NIST National Vulnerability Database
- CVSS
- Severity Classification
- Risk Assessment
- Security Reporting
- Machine-Readable Security Reports

---

# Installation

## Requirements

- Python 3
- Internet connection for NVD API queries
- Permission to scan the target system

## Clone Repository

```bash
git clone https://github.com/rahulkmr1502/SentinelRecon.git
```

## Enter Project Directory

```bash
cd SentinelRecon
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Run the main scanner:

```bash
python src/main.py
```

Enter a domain or IP address:

```text
Enter an IP address or domain: example.com
```

SentinelRecon will automatically perform the complete assessment workflow.

---

# Test Modules

The project also contains individual test files for specific components.

## CVE Parser Test

```bash
python src/test_cve_parser.py
```

## HTTP Analyzer Test

```bash
python src/test_http.py
```

## TLS Analyzer Test

```bash
python src/test_tls.py
```

## JSON Report Test

```bash
python src/test_json_report.py
```

These tests help verify individual modules before integrating them into the main scanner.

---

# Learning Objectives

This project is designed to understand:

- Network reconnaissance
- TCP socket programming
- DNS resolution
- Port scanning
- Concurrent programming
- HTTP internals
- HTTPS internals
- TLS communication
- X.509 certificates
- Service fingerprinting
- Security header analysis
- Security misconfiguration detection
- CVE intelligence
- CVSS scoring
- Risk assessment
- Vulnerability reporting
- HTML report generation
- JSON report generation
- Data serialization
- Modular Python architecture
- Software engineering practices
- Cybersecurity assessment workflows

---

# Project Progress

| Milestone | Description | Status |
|---|---|---|
| 1 | Project Setup | ✅ Completed |
| 2 | DNS Resolution | ✅ Completed |
| 3 | TCP Port Scanner | ✅ Completed |
| 4 | Banner Grabbing | ✅ Completed |
| 5 | Code Refactoring | ✅ Completed |
| 6 | HTTP & TLS Analysis | ✅ Completed |
| 7 | Security Misconfiguration Detection | ✅ Completed |
| 8 | CVE Lookup | ✅ Completed |
| 9 | Risk Assessment | ✅ Completed |
| 10 | HTML Report Generation | ✅ Completed |
| 11 | JSON Report Generation | ✅ Completed |

---

# Upcoming Features

- Configuration File Support
- Unit Testing
- Integration Testing
- Docker Support
- GitHub Actions CI/CD
- Logging Improvements
- Multi-target Scanning
- Final Refactoring
- Final Documentation

---

# Responsible Use

SentinelRecon is an educational cybersecurity project intended for:

- Learning
- Research
- Lab environments
- Authorized security testing
- Systems owned by the user
- Systems where explicit testing permission has been granted

Only scan systems that you are authorized to assess.

Unauthorized scanning or vulnerability assessment may violate laws, policies, or terms of service.

The author is not responsible for misuse of this software.

---

# Author

**Rahul Kumar**

GitHub:

https://github.com/rahulkmr1502

---

# License

This project is licensed under the MIT License.