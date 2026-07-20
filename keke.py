import requests

def advanced_vulnerability_scan(domain):
    # Ensure domain includes schema and remove trailing slashes
    if not domain.startswith("http://") and not domain.startswith("https://"):
        domain = "http://" + domain
    domain = domain.rstrip("/")
    
    print(f"\n[*] Starting advanced security assessment on: {domain}")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    # 1. Text-based checks (SQLi, XSS, LFI)
    text_vulns = {
        "SQL Injection": {
            "paths": ["/search.php?id=1'", "/login.php?user=1' OR '1'='1"], 
            "sigs": ["SQL syntax", "mysql_fetch", "Warning: mysql", "PostgreSQL", "ORA-00933"]
        },
        "Cross-Site Scripting (XSS)": {
            "paths": ["/search.php?q=<script>alert(1)</script>"], 
            "sigs": ["<script>alert(1)</script>"]
        },
        "Local File Inclusion (LFI)": {
            "paths": ["/view.php?file=../../../../etc/passwd"], 
            "sigs": ["root:x:0:0:", "bin:x:1:1:"]
        }
    }

    # 2. Status Code checks (Forceful Browsing, Directory Traversal, Open Endpoints)
    status_paths = [
        "/admin/", 
        "/wp-admin/", 
        "/upload.php", 
        "/execute.php", 
        "/upload.php?dir=../etc/"
    ]

    # Execute text-signature scans
    for vuln, data in text_vulns.items():
        for path in data["paths"]:
            url = domain + path
            try:
                res = requests.get(url, headers=headers, timeout=5)
                if any(sig.lower() in res.text.lower() for sig in data["sigs"]): 
                    print(f"[!] POSSIBLE {vuln} detected at: {url}")
            except Exception:
                pass

    # Execute status code discovery scans
    for path in status_paths:
        url = domain + path
        try:
            res = requests.get(url, headers=headers, timeout=5)
            # If a restricted portal or active script returns 200 OK, it's exposed
            if res.status_code == 200:
                print(f"[!] Exposure/Access Granted (HTTP 200) at: {url}")
        except Exception:
            pass

    print("\n[*] Scan completed.")

if __name__ == "__main__":
    target_domain = input("Enter the domain to scan for vulnerabilities: ").strip()
    if target_domain:
        advanced_vulnerability_scan(target_domain)
