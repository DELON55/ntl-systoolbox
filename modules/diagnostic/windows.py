import winrm
import json
from datetime import datetime

def diagnostic_windows(ip, user, password):
    result = {
        "ip": ip,
        "reachable": False,
        "error": None,
        "data": None
    }

    try:
        session = winrm.Session(
            target=ip,
            auth=(user, password),
            transport="basic"
        )

        ps_script = """
        $services = @("NTDS","DNS")
        $result = @{}

        foreach ($svc in $services) {
            $s = Get-Service $svc -ErrorAction SilentlyContinue
            if ($s) {
                $result[$svc] = $s.Status
            } else {
                $result[$svc] = "NOT_FOUND"
            }
        }

        $output = @{
            timestamp = (Get-Date).ToString("s")
            hostname = $env:COMPUTERNAME
            services = $result
        }

        $output | ConvertTo-Json
        """

        r = session.run_ps(ps_script)

        if r.status_code != 0:
            raise Exception(r.std_err.decode())

        result["reachable"] = True
        result["data"] = json.loads(r.std_out.decode())

    except Exception as e:
        result["error"] = str(e)

    return result
