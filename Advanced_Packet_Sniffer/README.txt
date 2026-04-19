Advanced Packet Sniffer + ARP Spoofing Detector
=============================================

Project Title:
Advanced Packet Sniffer + ARP Spoofing Detector (Using Scapy)

Description:
This project is a Python-based network security tool designed to capture
network packets in real time and detect ARP Spoofing (ARP Poisoning) attacks.
ARP spoofing is a common Man-in-the-Middle (MITM) technique used by attackers
to intercept or manipulate network traffic on local networks.

Using the Scapy library, this tool monitors ARP packets, tracks IP-to-MAC
address mappings, and identifies suspicious changes that may indicate an
ongoing ARP spoofing attack.

Problem Statement:
In local area networks, ARP spoofing attacks can go unnoticed and allow
attackers to redirect or intercept sensitive data. There is a need for a
real-time monitoring tool that can analyze network packets and detect such
attacks early.

Objectives:
- Capture network packets in real time
- Monitor and analyze ARP packets
- Track IP-to-MAC address mappings
- Detect anomalies indicating ARP spoofing
- Improve understanding of network security and packet analysis

Technologies Used:
- Python
- Scapy Library
- Linux Environment
- Networking Protocols (ARP, IP, Ethernet)

How It Works:
1. The tool continuously sniffs network packets.
2. It extracts ARP responses from the traffic.
3. Maintains a record of legitimate IP-MAC mappings.
4. Compares incoming ARP packets with existing records.
5. If an IP address is associated with multiple MAC addresses,
   the tool flags it as a potential ARP spoofing attack.

Practical Use Cases:
- Real-time ARP spoofing detection on local networks
- Network traffic analysis and forensics
- Educational tool for learning packet structures and ARP protocol
- Security monitoring in labs or small networks

Ethical Notice:
This tool is strictly intended for educational and defensive purposes.
Use it only on networks you own or have explicit permission to monitor.
Unauthorized packet sniffing or network monitoring may be illegal.

How to Run:
1. Install Python and Scapy
2. Run the script with root privileges:
   sudo python3 packet_sniffer.py
3. Monitor alerts for suspicious ARP activity

Future Improvements:
- Logging detected attacks to files
- Email or desktop notifications
- GUI-based dashboard
- Support for other network attacks

Author:
Shailesh

