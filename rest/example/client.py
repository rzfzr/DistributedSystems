from requests import put, get

ans = True
while ans:

    name = input("Nome da conta: ")
    if True:  # client.service.exists(name):
        # print('Usuario cadastrado nesse banco!')

        print("""
        1.Consultar cadastro
        # 2.Alterar cadastro
        3.Saque
        4.Saldo
        5.Transferencia de valor
        # 6.Transferencia de banco
        7.Sair
        """)
        ans = input("Sua escolha: ")
        if ans == "1":
            print(get('http://localhost:5000/accounts/'+name).json())

            # print('Cadastro:', client.service.consult(name))
        # elif ans=="2":

        elif ans == "3":
            gold = input("Quantia a ser sacada: ")
            print(get('http://localhost:5000/accounts/'+name, gold).json())

            if (client.service.withdraw(name, float(gold))):
                print('Ok')
            else:
                print('Saldo nao suficiente')

        elif ans == "4":
            print('Saldo:', client.service.balance(name))

        elif ans == "5":
            gold = input("Quantia a ser transferida: ")

            if (client.service.withdraw(name, float(gold))):
                print('Saldo Ok')
                targetName = input("Conta de destino: ")
                if client.service.exists(name):
                    print('Usuario de destino cadastrado nesse banco!')
                    client.service.deposit(targetName, float(gold))
                    print('Transacao OK!')
                    # selver.withdraw(name)
            else:
                print('Saldo nao suficiente')

            print('Valor :', client.service.balance(name))
        elif ans == "6":

            altserver.AddAcc(name, float(client.service.balance(name)))
            client.service.DelAcc(name)

        elif ans == "7":
            print("\n Goodbye")
        elif ans != "":
            print("\n Not Valid Choice Try again")
    else:
        print('Usuario nao cadastrado nesse banco!')


# put('http://localhost:5000/account', data={'gold': '1000'}).json()
