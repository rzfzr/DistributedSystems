import socket
# from _thread import *
# import threading
import sys
import random

import os
import multiprocessing
import datetime
import time
import json
import demjson


import copy


import jrpc

class User:
  def __init__(self, name, gold):
    self.name = name
    self.gold = gold




def LoadBD():
	users=[]
	try:
		with open('b2.json') as data_file:
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
		with open('b2.json', 'r+') as data_file:
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

class SimpleService(jrpc.service.SocketObject):

    
    @jrpc.service.method
    def echo(self, msg):
        return msg
        
    # @jrpc.service.method
    # def newAcc(self, name,gold):
    #     SaveBD(name,gold)
        
    #     return True
    
    
    
    @jrpc.service.method
    def exists(self, name):
        users = LoadBD()
        for user in users:
            if user.name == name:
                return True
                # return ('Saldo'+ str(user.gold))
        return False
    
    @jrpc.service.method
    def withdraw(self,name,gold):
        users = LoadBD()
        for user in users:
            if user.name == name:
                if user.gold >= gold:
                    if SaveBD(name,user.gold-gold):
                        print 'withdraw ok'
                        return True
                # return ('Saldo'+ str(user.gold))
        return False
    @jrpc.service.method
    def deposit(self,name,gold):
        users = LoadBD()
        for user in users:
            if user.name == name:
                if SaveBD(name,user.gold +gold):
                    print 'deposit ok'
                    return user.gold+gold
                # return ('Saldo'+ str(user.gold))
        return False
    
        
    @jrpc.service.method
    def consult(self, name):
        users = LoadBD()
        for user in users:
            if user.name == name:
                return (user.name + ' '+ str(user.gold))
        return('Usuario nao encontrado!')
        
    @jrpc.service.method
    def balance(self, name):
        users = LoadBD()
        for user in users:
            if user.name == name:
                return str(user.gold)
        return('Usuario nao encontrado!')


    @jrpc.service.method
    def transferAcc(self,name,gold):
        AddAcc(name,gold)
        DelAcc(name)
        
    @jrpc.service.method
    def DelAcc(self,name):
        try:
    		with open('b2.json', 'r+') as data_file:
    			data = json.load(data_file)
    			print(data)
    			
    			for e in data:
    				if e['name']==name:
    				    data.remove(e)
    				    print 'removed',e['name']
    			data_file.seek(0)
    			json.dump(data,data_file, indent = 4)
    			data_file.truncate()
    			# data_file.close()
    		return True
    	except (ValueError, KeyError, TypeError):
    		print("JSON format error",ValueError,KeyError,TypeError)
    		return False
    
    @jrpc.service.method
    def AddAcc(self,name,gold):
        try:
            with open('b2.json', 'r+') as data_file:
    			data = json.load(data_file)
    			print(data)
    			
    			for e in data:
    			    n = copy.copy(e)
    			    n['name']=name
    			    n['gold']=gold
    			    print 'added',n['name'],n['gold']
    			    data.append(n)
    			    break
    			data_file.seek(0)
    			json.dump(data,data_file, indent = 4)
    			data_file.truncate()
    			# data_file.close()
            return True
    	except (ValueError, KeyError, TypeError):
    		print("JSON format error",ValueError,KeyError,TypeError)
    		return False

        



if __name__ == '__main__':
    print('Banco online!')
    if LoadBD():
        server = SimpleService(50002) #Include the listening port
        server.run_wait()
    


