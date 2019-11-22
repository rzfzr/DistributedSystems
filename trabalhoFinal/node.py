import socket
import sys
# import curses
# import msvcrt
import asyncio


archive =["ReceitaBolo", "PlanosEspaciais","LordoftheRings"]
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)   
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

task1 = asyncio.create_task(
    say_after(1, 'hello'))

while True:
    # Wait for a connection
    asyncio.run(test())
    print('Waiting for a connection')
    # if msvcrt.kbhit():
    #     print("hit")
    connection, client_address = sock.accept()
    print("testthisballs")
    try:
        print('Connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(archive[int(data)].encode('utf-8'))
                # connection.close()
            else:
                print('no data from', client_address)
                break



    finally:
        print("Clean up the connection")
        connection.close()
