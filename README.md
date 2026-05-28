# CodeAlpha: Basic Network Sniffer

A lightweight, terminal-based packet sniffer developed in Python using the `Scapy` library. This project was built to fulfill **Task 1** of the Cyber Security Internship program at CodeAlpha.

## 📌 Project Overview
This network sniffer intercepts and analyzes live network traffic packets passing through your network interface. It decodes crucial protocol data and payload structures in real-time, helping to understand how data flows across local and external networks.

### Features
* **Live Packet Capture:** Continuous sniffing of active network traffic.
* **Protocol Identification:** Automatically filters and categorizes **TCP**, **UDP**, and **ICMP** protocols.
* **IP Mapping:** Extracts and cleanly displays both **Source** and **Destination** IP addresses.
* **Safe Payload Inspection:** Decodes and showcases readable payload text snippets while filtering out non-printable binary characters to keep the output human-readable.

---

## 🛠️ Prerequisites & Installation

### 1. Requirements
* Python 3.x
* Npcap (For Windows users, usually bundled with Wireshark/Scapy installers)

### 2. Install Dependencies
Install the required network packet manipulation tool via `pip`:
```bash
pip install scapy