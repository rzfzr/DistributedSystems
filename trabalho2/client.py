import socket


def Main():
	host = '127.0.0.1'
	port = 12342
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))

	while True:
		data = input('\ControleDeComprasSimulator2000:')
		if data =='':data="  "
		s.send(data.encode('ascii'))
		data = s.recv(1024).decode('ascii')
		print(data)


		# if data == 'exit':
		# 	break
	s.close()



if __name__ == '__main__':
	Main()
