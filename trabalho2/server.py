import socket
from _thread import *
import threading



import sys
import random

import os
import multiprocessing
import datetime
import time
import json
import demjson


# users = []

class User:
  def __init__(self, name, gold):
    self.name = name
    self.gold = gold


print_lock = threading.Lock()
def threaded(c):
	while True:
		users=LoadBD()
		data = c.recv(1024).decode('ascii')
		response='Aguardando requisicao'
		print('recebido', data)
		# print('users',users)
		for user in users:
			if data == user.name:
				print('match')
				user = user
				c.send(('Saldo disponivel:'+str(user.gold)).encode('ascii'))
				draw = float(c.recv(1024).decode('ascii'))

				if draw<=user.gold:
					print(user.name,user.gold-draw)
					SaveBD(user.name,user.gold-draw)
					response = 'saldo atualizado: '+ str(user.gold-draw)
				else:
					print('nope')
					response ='saldo insuficiente'
			else:
				print('no match found')

				# print('printed here',data)

		# if selection == '':
		# 	data = 'Esse cara nao existe'
		# if response != '':
		c.send(response.encode('ascii'))
		if not data:
			print('Bye')
			print_lock.release()
			break
	c.close()


def Main():
	host = ""
	port = 12342
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print("socket binded to post", port)
	s.listen(5)
	print("socket is listening")
	while True:
		c, addr = s.accept()
		print_lock.acquire()
		print('Connected to :', addr[0], ':', addr[1])
		start_new_thread(threaded, (c,))
	s.close()

def LoadBD():
	users=[]
	try:
		with open('db.json') as data_file:
			data = json.load(data_file)
			for e in data:
				users.append(User(e['name'],e['gold']))
			for user in users:
				print(user.name,'tem',user.gold,'dinheiros')
			# data_file.close()
			return users
	except (ValueError, KeyError, TypeError):
		print("JSON format error")
		return False

def SaveBD(name, gold):
	try:
		with open('db.json', 'r+') as data_file:
			data = json.load(data_file)
			print(data)
			for e in data:
				if e['name']==name:
					e['gold']=float(gold)
					print('newgold',e['gold'])

			print(data)

			data_file.seek(0)
			json.dump(data,data_file, indent = 4)
			data_file.truncate()
			# data_file.close()
		return True
	except (ValueError, KeyError, TypeError):
		print("JSON format error",ValueError,KeyError,TypeError)
		return False



if __name__ == '__main__':
	if LoadBD():
		print('done')
		Main()
		LoadBD()
