#  Em python o bloco é fechado pela indentação

def sacar(valor): # inicio do bloco do método
    saldo = 500

    if saldo >= valor: # inicio do bloco do if

       print("saldo sacado!")
       print("retire seu dinheiro!") 

    #fim do bloco do if

#fim do bloco do método    
sacar(400)

def depositar(valor): # inicio do bloco do método
    saldo = 500
    saldo += valor

