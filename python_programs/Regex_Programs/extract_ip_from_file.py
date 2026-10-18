import ipaddress
import re
from pathlib import Path

def extract_ips(filename):
    text = Path(filename).read_text(encoding="utf-8", errors="replace")
    candidates = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)
    result = []
    for candidate in candidates:
        try:
            result.append(str(ipaddress.ip_address(candidate)))
        except ValueError:
            pass
    return result

if __name__ == "__main__":
    print(extract_ips(input("File path: ")))
