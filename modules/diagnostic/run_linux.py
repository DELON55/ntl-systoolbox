from modules.diagnostic.linux import diagnostic_linux
import json
import os

def run():
    result = diagnostic_linux("WMS-DB")

    output_path = "/opt/ntl-systoolbox/outputs/json/linux_diagnostic.json"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=4)

    print(result)
    return result["status"]
