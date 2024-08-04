from typing import List
import socket

from src.utils import custom_input

# Project 46: Port Scanner
def proj_port_scanner():
    remoteServer, port_range = custom_input(["Enter the host to scan:", 
                                     "Enter the port range to scan (e.g., 20-80)"])
    start_port, end_port = map(int, port_range.split('-'))
    open_ports = port_scanner(remoteServer, start_port, end_port)
    print(f'Open ports on {remoteServer}: {open_ports}')

def port_scanner(remoteServer: str, start_port: int, end_port: int) -> List[int]:
    """
    Scans for open ports.

    Args:
        host (str): Host computer to scan.
        start_port (int): Starting point of the scan.
        end_port (int): Ending point of the scan.

    Returns:
        List[int]: A list of open ports.
    """
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((remoteServer, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    return open_ports