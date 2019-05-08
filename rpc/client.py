import jrpc
      

      


ans=True
while ans:
    bank=raw_input("Banco 1 ou 2: ")
    
    if bank =="1": 
        server = None
        server = jrpc.service.SocketProxy(50001) #The server's listening port
        print server.echo("Conexao feita com sucesso!(50001)")
    else:
        server = None
        server = jrpc.service.SocketProxy(50002) #The server's listening port
        print server.echo("Conexao feita com sucesso!(50002)")
            
    if bank =="2": 
        altserver = None
        altserver = jrpc.service.SocketProxy(50001) #The server's listening port
        print altserver.echo("Conexao feita com sucesso!(50001)")
    else:
        altserver = None
        altserver = jrpc.service.SocketProxy(50002) #The server's listening port
        print altserver.echo("Conexao feita com sucesso!(50002)")
            
    name=raw_input("Nome da conta: ")
    if server.exists(name):
        print ('Usuario cadastrado nesse banco!')
        
        print ("""
        1.Consultar cadastro
        # 2.Alterar cadastro
        3.Saque
        4.Saldo
        5.Transferencia de valor
        # 6.Transferencia de banco
        7.Sair
        """)
        ans=raw_input("Sua escolha: ") 
        if ans=="1": 
            print 'Cadastro:', server.consult(name)
        # elif ans=="2":
    
        elif ans=="3":
            gold=raw_input("Quantia a ser sacada: ")
            if (server.withdraw(name,float(gold))):
                print 'Ok'
            else:
                print 'Saldo nao suficiente'
        
        elif ans=="4":
            print 'Saldo:', server.balance(name)
            
        elif ans=="5":
            gold=raw_input("Quantia a ser transferida: ")
            
            if (server.withdraw(name,float(gold))):
                print 'Saldo Ok'
                targetName=raw_input("Conta de destino: ")
                if server.exists(name):
                    print ('Usuario de destino cadastrado nesse banco!')
                    server.deposit(targetName,float(gold))
                    print 'Transacao OK!'
                    # selver.withdraw(name)
                    
            else:
                print 'Saldo nao suficiente'
                
                
                
            print 'Valor :', server.balance(name)
        elif ans=="6":
            
            altserver.AddAcc(name, float(server.balance(name)))
            server.DelAcc(name)
            
            
            
        elif ans=="7":
          print("\n Goodbye") 
        elif ans !="":
          print("\n Not Valid Choice Try again") 
    else:
        print('Usuario nao cadastrado nesse banco!')
        