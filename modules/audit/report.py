import json
from modules.audit.scan import scan_network
from modules.audit.eol import check_eol
from datetime import datetime

OUTPUT = "/opt/ntl-systoolbox/outputs/audit/audit_eol.json"

def generate_report():
    scan = scan_network("192.168.10.0/24")
    report = {
        "timestamp": datetime.now().isoformat(),
        "hosts": []
    }

    for h in scan:
        report["hosts"].append({
            "ip": h["ip"],
            "os": h["os"],
            "eol": check_eol(h["os"])
        })

    with open(OUTPUT, "w") as f:
        json.dump(report, f, indent=4)

    return report
