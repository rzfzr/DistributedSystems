import socket
import sys
import time
import threading












def readTerminal(name):

    while 1:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 10000)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)

        try:
            message = input("To send: ").encode('utf-8')
            print('Sending: {!r}'.format(message))
            sock.sendall(message)

            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print('Received: {!r}'.format(data))

        finally:
            time.sleep(1)
            print('Closing socket')
            
            sock.close()


if __name__ == "__main__":
    x = threading.Thread(target=readTerminal, args=(1,))
    x.start()




