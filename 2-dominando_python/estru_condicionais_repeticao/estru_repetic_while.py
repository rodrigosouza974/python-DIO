'''
o comando while é usado para repetir um blocode código
várias vezes. faz sentido usar while quando não sabemos o
número exato de vezes que  nosso bloco e código deve ser executado
'''
 # while

opcao = -1

while opcao != 0:
    opcao = int(input("[1]sacar \n[2]Extrato \n[0]sair \n: "))

    if opcao == 1 :
        print('sacando...')
    elif opcao == 2 :
        print ('exibindo o extrato...')
else: 
    print("obrigado por usar nosso sitema bancário, até logo !")

