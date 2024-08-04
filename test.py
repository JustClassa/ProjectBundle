import pyfiglet
import socket
import sys
from datetime import datetime
from src.utils import custom_input

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)

socket.setdefaulttimeout(0.1)

remoteServer = custom_input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

start_time = datetime.now()
try:
    for port in range(1, 5001):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print(f"Port {port}:   Open")
        sock.close()

except KeyboardInterrupt as e:
    print("Ctrl + C Keyboard Interrupt")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()

end_time = datetime.now()

print(f'Scanning completed in: {end_time - start_time}')
