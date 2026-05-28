import sys
from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        
        # Determine protocol name
        proto_name = "Unknown"
        if proto == 6:
            proto_name = "TCP"
        elif proto == 17:
            proto_name = "UDP"
        elif proto == 1:
            proto_name = "ICMP"

        print(f"\n[+] New Packet: {src_ip} -> {dst_ip} | Protocol: {proto_name}")

        # Extract and display payload data if available
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = bytes(packet[IP].payload)
            if payload:
                # Print readable characters, replace non-readable bytes with dots
                readable_payload = ''.join([chr(b) if 32 <= b < 127 else '.' for b in payload])
                print(f"    Payload Snippet: {readable_payload[:80]}")

def main():
    print("="*60)
    print("        CODEALPHA BASIC NETWORK SNIFFER STARTED        ")
    print("   Listening for network traffic... Press Ctrl+C to stop.  ")
    print("="*60)
    
    try:
        # sniff() captures traffic. count=0 means it runs continuously.
        # prn specifies the callback function to run on every packet.
        # store=0 prevents saving everything in RAM to avoid memory leaks.
        sniff(prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("\n[-] Sniffer stopped by user.")
        sys.exit(0)
    except PermissionError:
        print("\n[!] ERROR: Run this script with Administrator/Root privileges!")
        sys.exit(1)

if __name__ == "__main__":
    main()