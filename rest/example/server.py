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

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


class User:
    def __init__(self, name, gold):
        self.name = name
        self.gold = gold


def LoadBD():
    users = []
    try:
        with open('b1.json') as data_file:
            data = json.load(data_file)
            for e in data:
                users.append(User(e['name'], e['gold']))
            for user in users:
                print(user.name, 'tem', user.gold, 'dinheiros')
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
                if e['name'] == name:
                    e['gold'] = float(gold)
                    print('newgold', e['gold'])

            print(data)

            data_file.seek(0)
            json.dump(data, data_file, indent=4)
            data_file.truncate()
            # data_file.close()
        return True
    except (ValueError, KeyError, TypeError):
        print("JSON format error", ValueError, KeyError, TypeError)
        return False


app = Flask(__name__)
api = Api(app)

ACCOUNTS = {
    'charlie': {'gold': '333'},
    'zamilson': {'gold': '222'},
}


def abort_if_account_doesnt_exist(account_id):
    if account_id not in ACCOUNTS:
        abort(404, message="Client {} doesn't exist".format(account_id))


parser = reqparse.RequestParser()
parser.add_argument('account')


# shows a single account item and lets you delete a account item
class Account(Resource):
    def get(self, account_id, op, gold):
        if op == 0:

            abort_if_account_doesnt_exist(account_id)
            return ACCOUNTS[account_id]
        elif op == 1:
            users = LoadBD()
            for user in users:
                if user.name == name:
                    if user.gold >= gold:
                        if SaveBD(name, user.gold-gold):
                            print('withdraw ok')
                            return True
                    # return ('Saldo'+ str(user.gold))
            return False

    def delete(self, account_id):
        abort_if_account_doesnt_exist(account_id)
        del ACCOUNTS[account_id]
        return '', 204

    def put(self, account_id):
        args = parser.parse_args()
        account = {'account': args['account']}
        ACCOUNTS[account_id] = account
        return account, 201

    # def withdraw(self, name, gold):
    #     users = LoadBD()
    #     for user in users:
    #         if user.name == name:
    #             if user.gold >= gold:
    #                 if SaveBD(name, user.gold-gold):
    #                     print('withdraw ok')
    #                     return True
    #             # return ('Saldo'+ str(user.gold))
    #     return False
# AccountList
# shows a list of all accounts, and lets you POST to add new accounts


class AccountList(Resource):
    def get(self):
        return ACCOUNTS

    def post(self):
        args = parser.parse_args()
        account_id = int(max(ACCOUNTS.keys()).lstrip('account')) + 1
        account_id = 'account%i' % account_id
        ACCOUNTS[account_id] = {'account': args['account']}
        return ACCOUNTS[account_id], 201


##
# Actually setup the Api resource routing here
##
api.add_resource(AccountList, '/accounts')
api.add_resource(Account, '/accounts/<account_id>')


if __name__ == '__main__':
    app.run(debug=True)
