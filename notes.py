# Linux command list
linux_cmds = ["hostname", "ping", "netstat", "ifconfig", "nslookup","nmap"]

# Windows command list
windows_cmds = [
    "ipconfig", "ping", "pathping", "hostname", "getmac", "arp",
    "tracert", "netstat", "route", "nslookup", "dig" ,"whois"
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
    "arp": "-a Displays/modifies ARP cache (Windows).",
    "tracert": "<google.com>   (Windows).",
    "route": "<print>    Displays or modifies IP routing table (Windows).",
    "nslookup": "<link>  Queries DNS records for domains.",
    "whois": "-v <link> Fetches domain/IP registration info.",
    "dig": "<link>  DNS lookup tool (Linux)."
}

# Nmap command dictionary
nmap_commands = {
"nmap <ip>":"Scan a single host",
"nmap <ip/24>":"Scan multiple ipaddress or subnet",
"nmap <ip/24 --exclude ip>":"Scan a subset by excluding host",
"echo <ip> target.txt":"Scan by reading a list of ip address from a file",
"nmap -iL target.txt":"open file",
"nmap -A <ip>":"Os and SV detection",
"nmap -O -sV <ip>":" second option for os and sv detection",
"nmap -sA <ip>":"find if the host is protected by firewall",
"nmap -PN <ip>":"Scan a host when protect by firewall",
"nmap -6 -PN scan.nmap.org":"Scan ipv6 host",
"nmap -sP <ip/24>":"Scan a network and find when service and host are up",
"nmap -F <ip>":"performe fast scan",
"nmap --reason <ip>":"Reason why port is in particular state",
"nmap --open <ip>":"show only open ports",
"nmap --packet-trace <ip>":"Show all packets during an nmap scan",
"nmap --iflist":"show host interface/routing info",
"nmap -PO <ip>":"Scan a host using ip protocol ping",
"nmap -p 80 <ip>":"do specific port scan",
"nmap -O <ip>":"detect remote os",
"nmap -sV <ip>":"detect service version",
"nmap -sO <ip>":"Scan for ip protocols(like temp,tcp,udp,etc..)",
"nmap <ip>>outuput.txt":"save the o/p of scan toa text file",
"cat output.txt":" view",
"nmap -oX outuput.xml <ip>":"save output to an xmlfile",
"nmap -PA <ip>":"TCP ACK scan",
"nmap -PS <ip>":"TCP SYN Scan",
"nmap -sS <ip>":"Sleath scan/half open scan",
"nmap -sT <ip>":"TCP connect scan",
"nmap -sW <ip>":"TCP WIndow Scan",
"nmap -sM <ip>":"TCP Maimon",
"nmap -sN <ip>":"Tcp Null Scan to bypass firewall and identify port stats",
"nmap -sF <ip>":"TCP FIN Scan- to bypass firewall by using FIN flag",
"nmap -sX <ip>":"TCP Xmas scan - test port by evading firewall detection",
"nmap -su <ip>":"Udp scn",
"nmap -PU <ip>":"UDP ping scan",
"nmap -f <ip>":"Scan by fragmentary ip packets",
"nmap -D RND,RND,ME <ip>":"Scan with decoys",
"nmap -PN --spoof-mac O <ip>":"spoof mac address during a scan",
"sudo nmap -p- -T4 <ip>":"faster scan for all parts",
"nmap -T4 <ip/24>":"fastest way to scan all devices on the network"
}

vul = {
"nmap -sS <ip>":"basic port scan",
"nmap -O -sV <ip>":"Os and sV detection",
"nmap --script vuln <ip>":"all vuln detetction"
}
index = {
"✨ /vul": " vul scan \n",
"✨ /nmap":"For nmap scan\n",
"✨ /linux":"For Linux\n",
"✨ /windows":"For windows \n"
}
