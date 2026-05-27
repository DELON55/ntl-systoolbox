import paramiko
import json
import socket
from datetime import datetime

def diagnostic_linux_ssh(ip, user, ssh_key, timeout=10):
    """
    Exécute un diagnostic Linux à distance via SSH.
    Retourne un dictionnaire Python (JSON-ready).
    """

    result = {
        "ip": ip,
        "reachable": False,
        "error": None,
        "data": None
    }

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            hostname=ip,
            username=user,
            key_filename=ssh_key,
            timeout=timeout
        )

        command = """
python3 - << 'EOF'
import psutil, platform, socket, json
from datetime import datetime

data = {
    "timestamp": datetime.now().isoformat(),
    "hostname": socket.gethostname(),
    "os": platform.platform(),
    "uptime_seconds": int(psutil.boot_time()),
    "cpu_percent": psutil.cpu_percent(interval=1),
    "ram_percent": psutil.virtual_memory().percent,
    "disk_percent": psutil.disk_usage('/').percent,
    "status": "OK"
}

if data["disk_percent"] > 85 or data["ram_percent"] > 85:
    data["status"] = "WARNING"
if data["disk_percent"] > 95:
    data["status"] = "CRITICAL"

print(json.dumps(data))
EOF
"""

        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        ssh.close()

        if error:
            result["error"] = error
        else:
            result["reachable"] = True
            result["data"] = json.loads(output)

    except Exception as e:
        result["error"] = str(e)

    return result
import paramiko
import json
import socket
from datetime import datetime

def diagnostic_linux_ssh(ip, user, ssh_key, timeout=10):
    """
    Exécute un diagnostic Linux à distance via SSH.
    Retourne un dictionnaire Python (JSON-ready).
    """

    result = {
        "ip": ip,
        "reachable": False,
        "error": None,
        "data": None
    }

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            hostname=ip,
            username=user,
            key_filename=ssh_key,
            timeout=timeout
        )

        command = """
python3 - << 'EOF'
import psutil, platform, socket, json
from datetime import datetime

data = {
    "timestamp": datetime.now().isoformat(),
    "hostname": socket.gethostname(),
    "os": platform.platform(),
    "uptime_seconds": int(psutil.boot_time()),
    "cpu_percent": psutil.cpu_percent(interval=1),
    "ram_percent": psutil.virtual_memory().percent,
    "disk_percent": psutil.disk_usage('/').percent,
    "status": "OK"
}

if data["disk_percent"] > 85 or data["ram_percent"] > 85:
    data["status"] = "WARNING"
if data["disk_percent"] > 95:
    data["status"] = "CRITICAL"

print(json.dumps(data))
EOF
"""

        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        ssh.close()

        if error:
            result["error"] = error
        else:
            result["reachable"] = True
            result["data"] = json.loads(output)

    except Exception as e:
        result["error"] = str(e)

    return result
