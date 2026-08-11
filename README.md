# SentinelRecon

SentinelRecon is a Python-based network reconnaissance and vulnerability assessment tool designed for authorized security testing and educational purposes.

The tool performs target validation, DNS resolution, TCP port scanning, banner grabbing, service fingerprinting, HTTP/HTTPS analysis, TLS certificate inspection, security misconfiguration detection, CVE lookup, risk analysis, and automated HTML/JSON report generation.

> Disclaimer: SentinelRecon should only be used against systems that you own or have explicit permission to test.

## Features

### 1. Target Validation

- IPv4 validation
- IPv6 validation
- Domain validation
- Invalid target detection

### 2. DNS Resolution

- Resolves domains to IP addresses
- Supports IPv4 and IPv6
- Removes duplicate addresses
- Sorts resolved addresses

### 3. TCP Port Scanning

- TCP port scanning
- Configurable port range
- Configurable timeout
- Concurrent scanning using ThreadPoolExecutor
- Configurable maximum workers

### 4. Banner Grabbing

- Connects to discovered services
- Retrieves service banners
- Sends HTTP requests to HTTP services
- Handles connection failures

### 5. Service Fingerprinting

- Detects common services
- Identifies products
- Identifies versions
- Parses service information from banners

### 6. HTTP Analysis

The HTTP analyzer checks:

- HTTP status code
- Server information
- Content-Type
- HTTP response headers

Security headers checked:

- Strict-Transport-Security
- Content-Security-Policy
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy

### 7. TLS Analysis

The TLS analyzer checks:

- TLS version
- Certificate issuer
- Certificate subject
- Certificate validity
- Certificate expiration
- Remaining validity days
- Certificate status

### 8. Security Misconfiguration Detection

SentinelRecon detects missing security headers and generates structured findings containing:

- Title
- Severity
- Category
- Description
- Recommendation

### 9. CVE Lookup

SentinelRecon integrates with the NIST National Vulnerability Database (NVD).

The CVE module can retrieve:

- CVE ID
- Severity
- CVSS score
- Published date
- Last modified date
- Vulnerability description

### 10. Risk Analysis

The risk analyzer calculates:

- Critical vulnerabilities
- High vulnerabilities
- Medium vulnerabilities
- Low vulnerabilities
- Informational vulnerabilities
- Total CVEs
- Average CVSS score
- Overall risk level

### 11. Configuration Support

Scanner configuration is supported through config.json.

Example configuration:

    {
        "scanner": {
            "start_port": 80,
            "end_port": 443,
            "timeout": 2.0,
            "max_workers": 20
        }
    }

Configuration options:

| Option | Description |
|--------|-------------|
| start_port | First TCP port to scan |
| end_port | Last TCP port to scan |
| timeout | Socket connection timeout |
| max_workers | Maximum concurrent workers |

If config.json does not exist or contains invalid JSON, SentinelRecon automatically uses the default configuration.

### 12. HTML Reports

SentinelRecon generates timestamped HTML reports.

Reports contain:

- Target information
- Open services
- Security findings
- Known vulnerabilities
- Risk summary
- Generation timestamp

Reports are saved in:

    reports/

Example:

    reports/google.com_20260808_175326.html

### 13. JSON Reports

SentinelRecon generates structured JSON vulnerability assessment reports.

The JSON report contains:

- Target
- Generation timestamp
- Services
- Security findings
- Known vulnerabilities
- Risk summary

Example:

    {
        "target": "example.com",
        "generated_at": "2026-08-08T17:53:26",
        "services": [
            {
                "port": 80,
                "service": "HTTP",
                "product": "Apache",
                "version": "2.4.7"
            }
        ],
        "security_findings": [],
        "known_vulnerabilities": [],
        "risk_summary": {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "informational": 0,
            "total": 0,
            "average_cvss": 0.0,
            "overall_risk": "None"
        }
    }

JSON reports are saved in:

    reports/

## Project Architecture

The SentinelRecon scanning pipeline is:

    User Input
        |
        v
    Target Validation
        |
        v
    DNS Resolution
        |
        v
    TCP Port Scanning
        |
        v
    Banner Grabbing
        |
        v
    Service Fingerprinting
        |
        +-------------------+
        |                   |
        v                   v
    HTTP Analysis       TLS Analysis
        |                   |
        v                   v
    Security            Certificate
    Findings            Analysis
        |                   |
        +---------+---------+
                  |
                  v
             CVE Lookup
                  |
                  v
             Risk Analysis
                  |
            +-----+-----+
            |           |
            v           v
        HTML Report  JSON Report

## Project Structure

    netrecon/
    |
    ├── src/
    │   ├── core/
    │   │   ├── __init__.py
    │   │   ├── banner_grabber.py
    │   │   ├── config.py
    │   │   ├── config_factory.py
    │   │   ├── config_loader.py
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
    │   └── main.py
    │
    ├── tests/
    │   ├── test_banner_grabber.py
    │   ├── test_config.py
    │   ├── test_cve.py
    │   ├── test_cve_parser.py
    │   ├── test_dns.py
    │   ├── test_finding.py
    │   ├── test_http.py
    │   ├── test_json_report.py
    │   ├── test_matcher.py
    │   ├── test_misconfig.py
    │   ├── test_nvd.py
    │   ├── test_port_scanner.py
    │   ├── test_report_generator.py
    │   ├── test_risk_analyzer.py
    │   ├── test_risk_summary.py
    │   ├── test_severity.py
    │   ├── test_tls.py
    │   └── test_validator.py
    │
    ├── reports/
    ├── config.json
    ├── requirements.txt
    └── README.md

## Requirements

- Python 3.10+
- Linux, macOS, or Windows
- Internet connection for NVD CVE lookups
- Permission to scan the target system

Python dependency:

    requests

Most scanner functionality uses Python's standard library.

## Installation

Clone the repository:

    git clone <your-repository-url>
    cd netrecon

Create a virtual environment:

    python3 -m venv .venv

Activate the virtual environment on Linux/macOS:

    source .venv/bin/activate

Activate the virtual environment on Windows:

    .venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

## Usage

Run SentinelRecon with:

    PYTHONPATH=src python src/main.py

The scanner will ask for a target:

    Enter an IP address or domain: example.com

The scanner performs:

1. Target validation
2. DNS resolution
3. TCP port scanning
4. Banner grabbing
5. Service fingerprinting
6. HTTP analysis
7. TLS analysis
8. Security misconfiguration detection
9. CVE lookup
10. Risk analysis
11. HTML report generation
12. JSON report generation

## Example Output

    Enter an IP address or domain: example.com

    Resolving 'example.com'...

    Resolved Addresses:

    - 93.184.216.34

    Scanning TCP ports on 93.184.216.34...
    Please wait...

    Total Open Ports Found: 2

    ## HTTP Analysis

    Status Code : 200
    Server      : ExampleServer
    Content-Type: text/html

    ## TLS Analysis

    TLS Version        : TLSv1.3
    Issuer             : Example CA
    Subject            : example.com
    Certificate Status : Valid

    # Known Vulnerabilities

    No known vulnerabilities found.

    # Risk Summary

    Critical       : 0
    High           : 0
    Medium         : 0
    Low            : 0
    Informational  : 0
    Total CVEs     : 0
    Average CVSS   : 0.0
    Overall Risk   : None

    HTML Report Created:
    reports/example.com_YYYYMMDD_HHMMSS.html

    JSON Report Created:
    reports/example.com_YYYYMMDD_HHMMSS.json

## Testing

SentinelRecon uses Python's built-in unittest framework.

Run the complete test suite with:

    PYTHONPATH=src python -m unittest discover -s tests -v

Current test result:

    ----------------------------------------------------------------------
    Ran 46 tests in 0.055s

    OK

All 46 automated tests currently pass successfully.

### Integration Testing

SentinelRecon includes integration tests that verify multiple components working together.

The integration test suite currently covers:

- Target validation → DNS resolution → port scanning
- Port scanning → banner grabbing → service fingerprinting
- HTTP analysis → security misconfiguration detection
- CVE lookup → risk analysis
- TLS certificate analysis
- Risk analysis → JSON report generation

Integration tests are located in:

    tests/test_integration.py

Current result:

    Ran 6 tests
    OK

Combined unit and integration test suite:

    Ran 52 tests
    OK

### Tested Components

The test suite covers:

- Target validation
- IPv4 validation
- IPv6 validation
- Domain validation
- DNS resolution
- TCP port scanning
- Banner grabbing
- Service fingerprinting
- HTTP analysis
- HTTP security headers
- TLS analysis
- Security misconfiguration detection
- CVE model
- CVE parsing
- CVE matching
- NVD API client
- Severity classification
- Risk analysis
- Risk summary
- Configuration loading
- Configuration factory
- HTML report generation
- JSON report generation

### Test Structure

All tests are located inside:

    tests/

The project currently contains 46 automated tests.

Network-dependent functionality is tested using mocks so that the test suite does not require real connections to external systems.

## Development Milestones

- [x] Milestone 1 — Project Setup
- [x] Milestone 2 — Logging
- [x] Milestone 3 — Target Validation
- [x] Milestone 4 — DNS Resolution
- [x] Milestone 5 — TCP Port Scanner
- [x] Milestone 6 — Banner Grabbing
- [x] Milestone 7 — Service Fingerprinting
- [x] Milestone 8 — Concurrent Scanning
- [x] Milestone 9 — HTTP/HTTPS Analysis
- [x] Milestone 10 — TLS Certificate Inspection
- [x] Milestone 11 — Misconfiguration Detection
- [x] Milestone 12 — CVE Lookup
- [x] Milestone 13 — CVSS / Risk Analysis
- [x] Milestone 14 — HTML Report Generation
- [x] Milestone 15 — JSON Export
- [x] Milestone 16 — Configuration File Support
- [x] Milestone 17 — Unit Tests
- [x] Milestone 18 — Integration Tests

## Technologies Used

- Python
- Socket Programming
- ThreadPoolExecutor
- HTTP
- TLS/SSL
- DNS
- NIST NVD API
- CVE
- CVSS
- JSON
- HTML
- unittest
- unittest.mock
- Git
- GitHub

## Security Considerations

SentinelRecon performs active network connections against targets.

Only scan:

- Systems you own
- Lab environments
- CTF environments
- Systems where you have explicit authorization

Do not use SentinelRecon to scan unauthorized systems or networks.

## Future Improvements

Potential future enhancements include:

- More service fingerprints
- Additional HTTP security checks
- More comprehensive TLS analysis
- Improved CVE matching
- CVSS v3/v4 support
- CLI argument support
- Better logging
- Integration tests
- Docker support
- GitHub Actions CI/CD
- Improved error handling
- Performance optimization
- Additional report visualizations

## Disclaimer

SentinelRecon is an educational security assessment project.

The author is not responsible for misuse of this software.

Always obtain proper authorization before performing security scans against a target.