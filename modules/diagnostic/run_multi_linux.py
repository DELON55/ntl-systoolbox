import json
from modules.diagnostic.linux_ssh import diagnostic_linux_ssh
from datetime import datetime

CONFIG_FILE = "/opt/ntl-systoolbox/config/hosts.json"
OUTPUT_FILE = "/opt/ntl-systoolbox/outputs/json/linux_multi_diagnostic.json"

def run():
    with open(CONFIG_FILE) as f:
        hosts = json.load(f)

    results = {
        "timestamp": datetime.now().isoformat(),
        "type": "linux_multi_diagnostic",
        "hosts": []
    }

    for host in hosts:
        print(f"[INFO] Diagnostic {host['name']} ({host['ip']})")

        diag = diagnostic_linux_ssh(
            ip=host["ip"],
            user=host["user"],
            ssh_key=host["ssh_key"]
        )

        results["hosts"].append({
            "name": host["name"],
            "ip": host["ip"],
            "result": diag
        })

    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=4)

    return results
