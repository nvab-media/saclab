from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def serve_pdf():
    return send_from_directory(directory='sql', path='SecuriryLab.pdf')


@app.route("/alive")
def alive():
    return "Keep alive"

# Linux command list
linux_cmds = ["hostname", "ping", "netstat", "ifconfig", "nslookup","nmap"]

# Windows command list
windows_cmds = [
    "ipconfig", "ping", "pathping", "hostname", "getmac", "arp",
    "tracert", "netstat", "route", "nslookup", "dig"
]

# Basic command usage database
command_usage = {
    "hostname": "Shows or sets the system hostname (Linux & Windows).",
    "ping": "Checks network connectivity.\nUsage: ping <host>",
    "netstat": "Displays network connections, routing tables, interface stats, etc.",
    "ifconfig": "Configures and displays network interfaces (Linux).",
    "ipconfig": "Displays TCP/IP configuration (Windows).",
    "pathping": "Combines ping and tracert for packet loss/latency (Windows).",
    "getmac": "Displays MAC addresses of network adapters (Windows).",
    "arp": "Displays/modifies ARP cache (Windows).",
    "tracert": "Traces route to a destination (Windows).",
    "route": "Displays or modifies IP routing table (Windows).",
    "nslookup": "Queries DNS records for domains.",
    "whois": "Fetches domain/IP registration info.",
    "dig": "DNS lookup tool (Linux)."
}

# Nmap command dictionary
nmap_commands = {
    "scan_single": "nmap 192.168.1.1 – Scan a single host.",
    "scan_multiple": "nmap 192.168.1.1 192.168.1.2 – Scan multiple IPs.",
    "scan_range": "nmap 192.168.1.1-20 – Scan IP range.",
    "scan_wildcard": "nmap 192.168.1.* – Scan using wildcard.",
    "scan_subnet": "nmap 192.168.1.0/24 – Scan an entire subnet.",
    "input_file": "nmap -iL targets.txt – Read hosts from file.",
    "exclude": "nmap --exclude 192.168.1.5 – Exclude hosts.",
    "os_detect": "nmap -O 192.168.1.1 – Detect OS.",
    "version_detect": "nmap -sV 192.168.1.1 – Detect service versions.",
    "ping_scan": "nmap -sP 192.168.1.0/24 – Discover online hosts.",
    "tcp_scan": "nmap -sT 192.168.1.1 – TCP connect() scan.",
    "syn_scan": "nmap -sS 192.168.1.1 – SYN stealth scan.",
    "udp_scan": "nmap -sU 192.168.1.1 – UDP scan.",
    "ack_scan": "nmap -sA 192.168.1.1 – Firewall test (ACK scan).",
    "window_scan": "nmap -sW 192.168.1.1 – TCP Window scan.",
    "maimon_scan": "nmap -sM 192.168.1.1 – TCP Maimon scan.",
    "null_scan": "nmap -sN 192.168.1.1 – Null scan to bypass firewalls.",
    "fin_scan": "nmap -sF 192.168.1.1 – FIN scan to test firewall rules.",
    "xmas_scan": "nmap -sX 192.168.1.1 – Xmas scan lights up TCP flags.",
    "ip_proto_scan": "nmap -sO 192.168.1.1 – Scan IP protocol support.",
    "decoy_scan": "nmap -D decoy1,decoy2,target – Hide source of scan.",
    "spoof_mac": "nmap --spoof-mac 00:11:22:33:44:55 – Spoof MAC address.",
    "output_txt": "nmap -oN output.txt 192.168.1.1 – Save output to text.",
    "output_xml": "nmap -oX output.xml 192.168.1.1 – Save output to XML.",
    "fast_scan": "nmap -F 192.168.1.1 – Fast scan using top 100 ports.",
    "scan_all_ports": "nmap -p 0-65535 192.168.1.1 – Scan all ports.",
    "interface_list": "nmap --iflist – Show interfaces and routes.",
    "trace_packets": "nmap --packet-trace 192.168.1.1 – Show packets.",
    "top_ports": "nmap --top-ports 10 192.168.1.1 – Scan top 10 ports."
}

@app.route('/')
def home():
    return "Welcome to Command Reference! Use /linux, /window, /nmap or /<command>."

@app.route('/linux')
def linux():
    return "Linux Commands:\n" + "\n".join(linux_cmds)

@app.route('/window')
def windows():
    return "Windows Commands:\n" + "\n".join(windows_cmds)

@app.route('/nmap')
def show_nmap():
    return "Nmap Commands:\n\n" + "\n\n".join(f"{k}:\n{v}" for k, v in nmap_commands.items())

@app.route('/<cmdname>')
def show_command(cmdname):
    cmd = cmdname.lower()
    if cmd in command_usage:
        return f"{cmd.upper()}:\n\n{command_usage[cmd]}"
    elif cmd in nmap_commands:
        return f"NMAP - {cmd}:\n\n{nmap_commands[cmd]}"
    return f"Command '{cmd}' not found."


if __name__ == "__main__":
    app.run()
