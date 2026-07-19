import requests

def stealthy_vulnerability_scan(domain):
    vulnerabilities = {
        "SQL Injection": [
            f"{domain}/search.php?id={id}",
            f"{domain}/login.php?user=1'&",
            f"{domain}/register.php?username=1'&",
            f"{domain}/forgot_password.php?id=1'&",
        ],
        "Cross-Site Scripting (XSS)": [
            f"{domain}/search.php?q=<script>alert('XSS')</script>",
            f"{domain}/login.php?user=<script>alert('XSS')</script>",
            f"{domain}/register.php?username=<script>alert('XSS')</script>",
            f"{domain}/forgot_password.php?id=<script>alert('XSS')</script>",
        ],
        "Cross-Site Request Forgery (CSRF)": [
            f"{domain}/search.php",
            f"{domain}/login.php",
            f"{domain}/register.php",
            f"{domain}/forgot_password.php",
        ],
        "Remote Code Execution (RCE)": [
            f"{domain}/upload.php",
            f"{domain}/execute.php?code=echo('Hello World');",
        ],
        "Local File Inclusion (LFI)": [
            f"{domain}/view.php?file=../../../../etc/passwd",
            f"{domain}/view.php?file=../../../../etc/hosts",
        ],
        "Directory Traversal (DT)": [
            f"{domain}/upload.php?dir=../etc/",
            f"{domain}/upload.php?dir=../../../etc/",
        ],
        "XML External Entity (XXE)": [
            f"{domain}/xml.php?entity=http://example.com/",
            f"{domain}/xml.php?entity=ftp://example.com/",
        ],
        "Server Side Request Forgery (SSRF)": [
            f"{domain}/search.php?host=http://example.com/",
            f"{domain}/search.php?host=https://example.com/",
        ],
        "Forceful Browsing": [
            f"{domain}/wp-admin/",
            f"{domain}/admin/",
        ],
        "Unrestricted File Upload": [
            f"{domain}/upload.php",
        ],
        "Out-of-Band (OOB) Code Execution": [
            f"{domain}/upload.php?action=download",
        ],
    }

    for vulnerability, urls in vulnerabilities.items():
        for url in urls:
            try:
                response = requests.head(url)
                if vulnerability == "SQL Injection":
                    if "SQL Injection Vulnerability Detected" in response.text:
                        print(f"[!] {vulnerability} vulnerability detected at: {url}")
                    else:
                        print(f"[-] No {vulnerability} vulnerability detected at: {url}")
                elif vulnerability == "Cross-Site Scripting (XSS)":
                    if "Cross-Site Scripting (XSS) Vulnerability Detected" in response.text:
                        print(f"[!] {vulnerability} vulnerability detected at: {url}")
                    else:
                        print(f"[-] No {vulnerability} vulnerability detected at: {url}")
                elif vulnerability == "Cross-Site Request Forgery (CSRF)":
                    if "Cross-Site Request Forgery (CSRF) Vulnerability Detected" in response.text:
                        print(f"[!] {vulnerability} vulnerability detected at: {url}")
                    else:
                        print(f"[-] No {vulnerability} vulnerability detected at: {url}")
                elif vulnerability == "Remote Code Execution (RCE)":
                    if "Remote Code Execution (RCE) Vulnerability Detected" in response.text:
                        print(f"[!] {vulnerability} vulnerability detected at: {url}")
                    else:
                        print(f"[-] No {vulnerability} vulnerability detected at: {url}")
                elif vulnerability == "Local File Inclusion (LFI)":
                    if "Local File Inclusion (LFI) Vulnerability Detected" in response.text:
                        print(f"[!] {vulnerability} vulnerability detected at: {url}")
                    else:
                        print(f"[-] No {vulnerability} vulnerability detected at: {url}")
                elif vulnerability == "Directory Traversal (DT)":
                    if "Directory Traversal (DT) Vulnerability Detected" in response.text:
                        print(f"[!] {vulnerability} vulnerability detected at: {url}")
                    else:
                        print(f"[-] No {vulnerability} vulnerability detected at: {url}")
                elif vulnerability == "XML External Entity (XXE)":
                    if "XML External Entity (XXE) Vulnerability Detected" in response.text:
                        print(f"[!] {vulnerability} vulnerability detected at: {url}")
                    else:
                        print(f"[-] No {vulnerability} vulnerability detected at: {url}")
                elif vulnerability == "Server Side Request Forgery (SSRF)":
                    if "Server Side Request Forgery (SSRF) Vulnerability Detected" in response.text:
                        print(f"[!] {vulnerability} vulnerability detected at: {url}")
                    else:
                        print(f"[-] No {vulnerability} vulnerability detected at: {url}")
                elif vulnerability == "Forceful Browsing":
                    if "Forceful Browsing Vulnerability Detected" in response.text:
                        print(f"[!] {vulnerability} vulnerability detected at: {url}")
                    else:
                        print(f"[-] No {vulnerability} vulnerability detected at: {url}")
                elif vulnerability == "Unrestricted File Upload":
                    if "Unrestricted File Upload Vulnerability Detected" in response.text:
                        print(f"[!] {vulnerability} vulnerability detected at: {url}")
                    else:
                        print(f"[-] No {vulnerability} vulnerability detected at: {url}")
                elif vulnerability == "Out-of-Band (OOB) Code Execution":
                    if "Out-of-Band (OOB) Code Execution Vulnerability Detected" in response.text:
                        print(f"[!] {vulnerability} vulnerability detected at: {url}")
                    else:
                        print(f"[-] No {vulnerability} vulnerability detected at: {url}")
            except requests.exceptions.RequestException as e:
                print(f"[-] Failed to connect to: {url}, Error: {str(e)}")

def main():
    domain = input("Enter the domain to scan for vulnerabilities: ")
    stealthy_vulnerability_scan(domain)

if __name__ == "__main__":
    main()
