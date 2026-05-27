EOL = {
    "Windows Server 2012": "2023-10",
    "Windows Server 2016": "2027-01",
    "Ubuntu 18.04": "2023-04",
    "Ubuntu 20.04": "2025-04"
}

def check_eol(os_name):
    return EOL.get(os_name, "UNKNOWN")
