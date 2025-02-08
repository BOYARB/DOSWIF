# DOSWIF
# Network Attack Tool

It is a tool designed to perform 
Distributed Denial of Service (DOS)
attacks on a specific target device 
or an entire network. The tool uses 
UDP flooding to flood the target by 
sending a large number of packets to 
it.

## Features:
- **Attack a specific device**: Perform a DDoS attack on a specific target device by providing its IP and port.
- **Attack an entire network**: Perform a DDoS attack on all devices within a given network (e.g., 192.168.0.1/24).
- **Multiple processes**: Utilizes multiple processes to increase the attack intensity.
- **Customizable packet size**: The tool sends large UDP packets (8192 bytes) for a stronger attack.

## Requirements:
- Root privileges to run the tool (must be executed as root).

## Usage:
1. Choose whether to attack a specific device or an entire network.
2. Enter the target IP address and port (for device attacks).
3. Enter the network IP (in CIDR format) and port (for network attacks).

## Warning:
This tool is intended for educational purposes and should only be used in environments where you have explicit permission to test the network. Unauthorized use of this tool on networks without permission is illegal and unethical.

## License:
This tool is free for personal use and is not intended for commercial purposes. Please read the license file
