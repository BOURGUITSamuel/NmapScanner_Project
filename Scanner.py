# coding: utf-8

import sys
import nmap
import re
import time

# Using the nmap port scanner.
scanner = nmap.PortScanner()

# Regular Expression Pattern to recognise IPv4 addresses.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

# Display the program banner.
print("-------------------")
print("Nmap python scanner")
print("-------------------")

# Ask user to input the ip address he want to scan.
while True:
    ip_addr = input("Please enter the IP address you want to scan: ")
    if ip_add_pattern.search(ip_addr):
        print(f"{ip_addr} is a valid ip address")
        type(ip_addr)
        break
    else:
        print("Invalid IP address !")
        continue

# Ask user which scan he want to do
while True:
    resp = input("""\nPlease enter the type of scan you want to run:
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan \n""")
    print(f"You have selected option {resp}")

    if resp == '1':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024', '-v -sS')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
        time.sleep(10)
        break
    elif resp == '2':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024', '-v -sU')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())
        time.sleep(10)
        break
    elif resp == '3':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
        time.sleep(10)
        break
    elif resp >= '4':
        print("Please enter a valid option. Enter 1-3")
        continue
