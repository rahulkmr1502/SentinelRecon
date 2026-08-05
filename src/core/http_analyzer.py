import socket


def analyze_http(host: str, port: int = 80) -> dict:
    """
    Analyze an HTTP service by sending a raw HTTP GET request.
    """

    request = (
        f"GET / HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        "User-Agent: SentinelRecon\r\n"
        "Connection: close\r\n\r\n"
    )

    response = ""

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(3)
            client.connect((host, port))

            client.sendall(request.encode())

            while True:
                data = client.recv(4096)

                if not data:
                    break

                response += data.decode(errors="ignore")

    except Exception:
        return {
            "status_code": "Unknown",
            "server": "Unknown",
            "content_type": "Unknown",
            "headers": {},
            "security_headers": {},
        }

    headers = response.split("\r\n\r\n")[0].split("\r\n")

    status_code = "Unknown"
    server = "Unknown"
    content_type = "Unknown"

    if headers:
        first_line = headers[0].split()

        if len(first_line) >= 2:
            status_code = first_line[1]

    header_dict = {}

    for line in headers[1:]:

        if ":" not in line:
            continue

        key, value = line.split(":", 1)

        header_dict[key.strip()] = value.strip()

    server = header_dict.get("Server", "Unknown")
    content_type = header_dict.get("Content-Type", "Unknown")

    security_headers = analyze_security_headers(header_dict)

    return {
        "status_code": status_code,
        "server": server,
        "content_type": content_type,
        "headers": header_dict,
        "security_headers": security_headers,
    }


def analyze_security_headers(headers: dict[str, str]) -> dict[str, bool]:
    """
    Analyze common HTTP security headers.
    """

    required_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy",
    ]

    results = {}

    for header in required_headers:
        results[header] = header in headers

    return results