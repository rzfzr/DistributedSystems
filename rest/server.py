import sys
import random

import os
import multiprocessing
import datetime
import time
import json
import demjson


import copy
import time

from spyne import Application, ServiceBase, Unicode, rpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class User:
  def __init__(self, name, gold):
    self.name = name
    self.gold = gold




def LoadBD():
	users=[]
	try:
		with open('b1.json') as data_file:
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
		with open('b1.json', 'r+') as data_file:
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
		
		
		
class ExampleService(ServiceBase):
    
    @rpc(Unicode, _returns=Unicode)
    def slow_request(ctx, request_id):
        time.sleep(1)
        return u'Request: %s' % request_id


    @rpc(Unicode, _returns=Unicode)
    def ping(ctx, request_id):
        return 'pong'
    
    @rpc(Unicode, _returns=Unicode)
    def exists(self, name):
        users = LoadBD()
        for user in users:
            if user.name == name:
                return True
                # return ('Saldo'+ str(user.gold))
        return False
    
    @rpc(Unicode,Unicode, _returns=Unicode)
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
    @rpc(Unicode,Unicode, _returns=Unicode)
    def deposit(self,name,gold):
        users = LoadBD()
        for user in users:
            if user.name == name:
                if SaveBD(name,user.gold +gold):
                    print 'deposit ok'
                    return user.gold+gold
                # return ('Saldo'+ str(user.gold))
        return False
    
        
    @rpc(Unicode, _returns=Unicode)
    def consult(self, name):
        users = LoadBD()
        for user in users:
            if user.name == name:
                return (user.name + ' '+ str(user.gold))
        return('Usuario nao encontrado!')
        
    @rpc(Unicode, _returns=Unicode)
    def balance(self, name):
        users = LoadBD()
        for user in users:
            if user.name == name:
                return str(user.gold)
        return('Usuario nao encontrado!')


    @rpc(Unicode,Unicode, _returns=Unicode)
    def transferAcc(self,name,gold):
        AddAcc(name,gold)
        DelAcc(name)
        
    @rpc(Unicode, _returns=Unicode)
    def DelAcc(self,name):
        try:
    		with open('b1.json', 'r+') as data_file:
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
    
    @rpc(Unicode,Unicode, _returns=Unicode)
    def AddAcc(self,name,gold):
        try:
            with open('b1.json', 'r+') as data_file:
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

        



application = Application(
    services=[ExampleService],
    tns='http://tests.python-zeep.org/',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11())

application = WsgiApplication(application)

if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, application)
    server.serve_forever()