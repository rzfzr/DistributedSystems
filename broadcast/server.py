import socket
import time
import datetime
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

server.settimeout(0.2)
server.bind(("", 44444))
while True:
    message = b(str(("sistemas distribuidos"+datetime.datetime.now())))
    server.sendto(message, ('<broadcast>', 37020))
    print("message sent!")
    time.sleep(1)