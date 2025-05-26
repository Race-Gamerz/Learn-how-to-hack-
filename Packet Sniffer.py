from scapy.all import *

def packet_sniffer(interface="eth0", count=10):
    print(f"Sniffing on {interface}...")
    packets = sniff(iface=interface, count=count)
    for packet in packets:
        print(packet.summary())

interface = input("Enter interface (e.g., eth0, wlan0): ")
packet_sniffer(interface)
