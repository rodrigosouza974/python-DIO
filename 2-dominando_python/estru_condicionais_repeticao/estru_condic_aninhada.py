# if aninhado
'''
podemos criar estruturas condicionais aninhadas, para isso basta 
adicionar estruturas if/elif/else dentro do blocom de sódigo de estruturas if/elif/else.
''' 
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("saque realizado")
    elif saque <= (saldo + cheque_especial):
            print("saque realizado com uso do cheque especial")
elif conta_universitaria:
    if saldo >=  saque :
            print("saque realizado com sucesso")
    else:
            print("saque insuficiente!")
   