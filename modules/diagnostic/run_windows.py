import json
from modules.diagnostic.windows import diagnostic_windows

OUTPUT = "/opt/ntl-systoolbox/outputs/json/windows_diagnostic.json"

def run():
    result = diagnostic_windows(
        ip="192.168.10.10",
        user="Administrateur",
        password="Admin1234@"
    )

    with open(OUTPUT, "w") as f:
        json.dump(result, f, indent=4)

    return result
