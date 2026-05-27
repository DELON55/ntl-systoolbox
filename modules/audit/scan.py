import nmap

def scan_network(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments="-O")

    hosts = []
    for h in nm.all_hosts():
        os = nm[h]['osmatch'][0]['name'] if nm[h]['osmatch'] else "Unknown"
        hosts.append({"ip": h, "os": os})

    return hosts
