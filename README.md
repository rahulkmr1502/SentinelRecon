# SentinelRecon 🔎

SentinelRecon is a Python-based network reconnaissance and vulnerability assessment tool designed to perform automated security analysis of authorized IP addresses and domains.

It combines network reconnaissance, service fingerprinting, HTTP/HTTPS analysis, TLS certificate inspection, security misconfiguration detection, CVE lookup, risk analysis, and automated report generation.

## Features

### Target Validation
- IPv4 validation
- IPv6 validation
- Domain validation
- Invalid target detection

### DNS Resolution
- Resolves domains and IP addresses
- Supports IPv4 and IPv6
- Displays resolved addresses

### TCP Port Scanning
- Configurable TCP port range
- Open port detection
- Configurable timeout
- Concurrent scanning using ThreadPoolExecutor
- Configurable worker count

### Service Fingerprinting
- Banner grabbing
- Service detection
- Product identification
- Version extraction
- HTTP banner analysis

### HTTP Analysis
- HTTP status code detection
- Server identification
- Content-Type detection
- Security header analysis

### Security Misconfiguration Detection

Checks for missing security headers:

- Strict-Transport-Security
- Content-Security-Policy
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy

### TLS Analysis
- TLS version detection
- Certificate issuer extraction
- Certificate subject extraction
- Certificate validity checking
- Certificate expiration analysis
- Remaining certificate days

### CVE Lookup
- NIST NVD API integration
- Product and version based CVE lookup
- CVE parsing
- CVSS score extraction
- Severity detection

### Risk Analysis
- Critical, High, Medium, Low and Informational classification
- Total CVE count
- Average CVSS score
- Overall risk calculation

### Report Generation

SentinelRecon generates:

- HTML reports
- JSON reports
- Timestamped report files
- Security findings
- CVE information
- Risk summaries

### Testing
- Unit tests
- Integration tests
- 52 automated tests

Current test result:

    Ran 52 tests
    OK

### Docker Support
SentinelRecon can run inside a Docker container using Python 3.12.

### GitHub Actions CI
The project includes GitHub Actions CI which:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs dependencies
4. Runs the complete test suite

## Project Structure

    SentinelRecon/
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    ├── .dockerignore
    ├── .gitignore
    ├── Dockerfile
    ├── LICENSE
    ├── README.md
    ├── config.json
    ├── requirements.txt
    ├── src/
    │   ├── __init__.py
    │   ├── main.py
    │   └── core/
    │       ├── __init__.py
    │       ├── banner_grabber.py
    │       ├── config.py
    │       ├── config_factory.py
    │       ├── config_loader.py
    │       ├── cve.py
    │       ├── cve_matcher.py
    │       ├── cve_parser.py
    │       ├── dns_resolver.py
    │       ├── findings.py
    │       ├── http_analyzer.py
    │       ├── json_report_generator.py
    │       ├── logger.py
    │       ├── misconfig_detector.py
    │       ├── nvd_client.py
    │       ├── port_scanner.py
    │       ├── report_generator.py
    │       ├── risk_analyzer.py
    │       ├── risk_summary.py
    │       ├── service_fingerprint.py
    │       ├── severity.py
    │       ├── tls_analyzer.py
    │       └── validator.py
    └── tests/
        ├── test_banner_grabber.py
        ├── test_config.py
        ├── test_cve.py
        ├── test_cve_parser.py
        ├── test_dns.py
        ├── test_finding.py
        ├── test_html_report.py
        ├── test_http.py
        ├── test_integration.py
        ├── test_json_report.py
        ├── test_matcher.py
        ├── test_misconfig.py
        ├── test_nvd.py
        ├── test_port_scanner.py
        ├── test_report_generator.py
        ├── test_risk_analyzer.py
        ├── test_risk_summary.py
        ├── test_severity.py
        ├── test_tls.py
        └── test_validator.py

## Technology Stack

- Python 3.12
- Requests
- Socket Programming
- SSL/TLS
- ThreadPoolExecutor
- JSON
- HTML
- Docker
- Git
- GitHub Actions
- Python unittest

## Requirements

- Python 3.12 or later
- Git
- Internet connection for CVE lookup
- Docker (optional)

Install dependencies:

    pip install -r requirements.txt

## Configuration

Scanner configuration is stored in:

    config.json

Configuration options include:

- Start port
- End port
- Connection timeout
- Maximum worker threads

Example configuration:

    {
        "start_port": 80,
        "end_port": 443,
        "timeout": 2.0,
        "max_workers": 20
    }

## Running SentinelRecon

Clone the repository:

    git clone <YOUR_GITHUB_REPOSITORY_URL>
    cd SentinelRecon

Create a virtual environment:

    python3 -m venv .venv

Activate it on Linux:

    source .venv/bin/activate

Activate it on Windows:

    .venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

Run SentinelRecon:

    python src/main.py

The program will ask:

    Enter an IP address or domain:

Enter a target that you own or have explicit authorization to scan.

Example:

    example.com

## Example Scan

Example execution:

    Enter an IP address or domain: example.com

    Scanner Configuration
    --------------------------------------------------
    Start Port  : 80
    End Port    : 443
    Timeout     : 2.0
    Max Workers : 20

    Resolving 'example.com'...

    Resolved Addresses:

     - 104.20.23.154
     - 172.66.147.243

    Scanning TCP ports on 104.20.23.154...
    Please wait...

    Total Open Ports Found: 2

HTTP analysis may display:

    HTTP Analysis
    --------------------------------------------------
    Status Code : 403
    Server      : cloudflare
    Content-Type: text/plain; charset=UTF-8

Security header analysis:

    Strict-Transport-Security           ✗ Missing
    Content-Security-Policy             ✗ Missing
    X-Frame-Options                     ✓ Present
    X-Content-Type-Options              ✗ Missing
    Referrer-Policy                     ✓ Present
    Permissions-Policy                  ✗ Missing

TLS analysis includes:

    TLS Version        : TLSv1.3
    Issuer             : ...
    Subject            : example.com
    Certificate Status : Valid
    Days Remaining     : ...

The final risk summary contains:

    Critical       : ...
    High           : ...
    Medium         : ...
    Low            : ...
    Informational  : ...
    Total CVEs     : ...
    Average CVSS   : ...
    Overall Risk   : ...

## Reports

SentinelRecon automatically creates a reports directory.

Two reports are generated after a successful scan:

    reports/
    ├── target_timestamp.html
    └── target_timestamp.json

### HTML Report

The HTML report contains:

- Target information
- Open services
- Security findings
- Known vulnerabilities
- Risk summary

### JSON Report

The JSON report provides machine-readable information including:

- Target
- Scan timestamp
- Services
- Security findings
- CVEs
- Risk summary

## Running Tests

Run the complete test suite:

    python -m unittest discover -s tests -p "test_*.py" -v

Expected result:

    Ran 52 tests
    OK

The test suite contains both unit and integration tests.

Integration tests verify flows such as:

    Target Validation
           ↓
    DNS Resolution
           ↓
    Port Scanning

    Port Scanning
           ↓
    Banner Grabbing
           ↓
    Service Fingerprinting

    HTTP Analysis
           ↓
    Security Header Detection
           ↓
    Misconfiguration Detection

    CVE Lookup
           ↓
    CVE Parsing
           ↓
    Risk Analysis

    Risk Analysis
           ↓
    JSON Report Generation

## Docker

Build the Docker image:

    docker build -t sentinelrecon .

Run the container:

    docker run --rm -it --user "$(id -u):$(id -g)" sentinelrecon

The --user option runs the container using the current host user's UID and GID. This prevents generated reports and logs from being owned by root.

## GitHub Actions

The project uses GitHub Actions for continuous integration.

Workflow file:

    .github/workflows/ci.yml

The CI pipeline:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs project dependencies
4. Runs all tests

The workflow runs when changes are pushed to main or when a pull request targets main.

## Architecture

SentinelRecon follows a modular architecture:

    User Input
        │
        ▼
    Target Validation
        │
        ▼
    DNS Resolution
        │
        ▼
    TCP Port Scanner
        │
        ▼
    Banner Grabbing
        │
        ▼
    Service Fingerprinting
        │
        ├───────────────┐
        ▼               ▼
    HTTP Analysis     TLS Analysis
        │
        ▼
    Misconfiguration Detection
        │
        ▼
    CVE Lookup
        │
        ▼
    Risk Analysis
        │
        ├───────────────┐
        ▼               ▼
    HTML Report      JSON Report

Core functionality is separated into individual modules under:

    src/core/

This makes the project easier to maintain, test, and extend.

## Security & Ethical Use

SentinelRecon is intended for:

- Educational purposes
- Security research
- Development environments
- Systems you own
- Systems where you have explicit authorization to perform security testing

Do not use SentinelRecon to scan systems or networks without permission.

The user is responsible for ensuring that all scanning activities comply with applicable laws, policies, and authorization requirements.

## Project Status

SentinelRecon has completed its planned development milestones.

    Project Setup                 ✅
    Logging                       ✅
    Target Validation             ✅
    DNS Resolution                ✅
    TCP Port Scanner              ✅
    Banner Grabbing               ✅
    Service Fingerprinting        ✅
    Concurrent Scanning           ✅
    HTTP/HTTPS Analysis           ✅
    TLS Certificate Analysis      ✅
    Misconfiguration Detection    ✅
    CVE Lookup                    ✅
    CVSS/Risk Analysis            ✅
    HTML Report Generation        ✅
    JSON Export                   ✅
    Configuration Support         ✅
    Unit Testing                  ✅
    Integration Testing           ✅
    Docker Support                ✅
    GitHub Actions CI             ✅
    Final Refactoring             ✅
    Final Documentation           ✅

## Future Improvements

Possible future improvements include:

- Additional service fingerprinting
- Expanded security checks
- Improved IPv6 scanning
- More comprehensive TLS analysis
- Additional report formats
- Improved CVE matching
- Configurable scan profiles
- More advanced vulnerability correlation
- Improved CLI interface
- Additional automated security checks

## License

This project is licensed under the MIT License.

See the LICENSE file for details.

## Author

Developed as a cybersecurity and network reconnaissance project using Python.

SentinelRecon — Network Reconnaissance & Vulnerability Assessment Tool