import psutil
import platform
import json
import socket
from datetime import datetime
import os

def diagnostic_linux():
    hostname = socket.gethostname()

    data = {
        "timestamp": datetime.now().isoformat(),
        "hostname": hostname,
        "os": platform.platform(),
        "uptime_seconds": int(datetime.now().timestamp() - psutil.boot_time()),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "status": "OK"
    }

    # Logique de seuils
    if data["disk_percent"] > 85 or data["ram_percent"] > 85:
        data["status"] = "WARNING"
    if data["disk_percent"] > 95:
        data["status"] = "CRITICAL"

    return data
