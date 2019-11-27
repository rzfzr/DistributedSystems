import socket
import sys
import time
import threading


portServer=10000
portClient=10000



def server(name):
    archive =["ReceitaBolo", "PlanosEspaciais","LordoftheRings"]
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ('localhost', portServer)   
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)
    sock.listen(1)
    while True:
        print('Waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('Connection from', client_address)
            while True:
                data = connection.recv(16)
                print('received {!r}'.format(data))
                if data:
                    print('sending data back to the client')
                    connection.sendall(archive[int(data)].encode('utf-8'))
                else:
                    print('no data from', client_address)
                    break
        finally:
            print("Clean up the connection")
            connection.close()

def readTerminal(name):

    while 1:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', portClient)
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
    x = threading.Thread(target=server, args=(1,))
    x.start()




