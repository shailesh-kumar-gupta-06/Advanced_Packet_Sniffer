from scapy.all import sniff, ARP
import time

ip_mac_table = {}

def detect_arp_spoof(packet):
    if packet.haslayer(ARP):
        arp_layer = packet[ARP]

        if arp_layer.op == 2:
            ip = arp_layer.psrc      
            mac = arp_layer.hwsrc    

            if ip in ip_mac_table:
                if ip_mac_table[ip] != mac:
                    print("\n⚠️  ARP SPOOFING DETECTED!")
                    print(f"IP Address : {ip}")
                    print(f"Old MAC    : {ip_mac_table[ip]}")
                    print(f"New MAC    : {mac}")
                    print("Possible Man-in-the-Middle Attack!\n")
            else:
                ip_mac_table[ip] = mac
                print(f"[+] New ARP Entry: {ip} -> {mac}")

def start_sniffing():
    print("=" * 60)
    print(" Advanced Packet Sniffer + ARP Spoofing Detector ")
    print("=" * 60)
    print("[*] Starting packet sniffing...")
    print("[*] Press CTRL + C to stop\n")

    sniff(filter="arp", store=False, prn=detect_arp_spoof)

if __name__ == "__main__":
    try:
        start_sniffing()
    except KeyboardInterrupt:
        print("\n[!] Sniffing stopped by user")
        print("[*] Exiting safely...")
