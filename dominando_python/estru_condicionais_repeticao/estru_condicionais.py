# if / elif / else
'''em alguns cenários mais de dois desvios, para isso
podemos utilizar a palavra reservada elif. o elif é 
composto por uma nova expressão lógica, que será testada e caso retorne
verdadeiro o bloco de código do elif será executado.
não existe um numero máximo de elis que podemos utilizar, 
porém evite criar grande estruturas condicionais, pois elas 
aumentam  a complexiadade do código
'''

opcao = int(input("Informe uma opção: [1]sacar \n [2]Extrato"))
if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print(' Exibindo o extrato...')
else :
    print('Opção Inválida')

