import subprocess
from datetime import datetime
from pathlib import Path

def dump_database():
    output_dir = Path("/opt/ntl-systoolbox/outputs/backups")
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = output_dir / f"wms_{datetime.now().strftime('%Y%m%d_%H%M')}.sql"

    cmd = [
        "mysqldump",
        "-h", "192.168.10.21",
        "-u", "wmsuser",
        "-pAdmin1234@",
        "--single-transaction",
        "--quick",
        "wms"
    ]

    with open(filename, "w") as f:
        result = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode())

    return str(filename)
