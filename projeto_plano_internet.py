'''
Desafio
Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'. Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.

Planos Oferecidos:

- Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
- Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
- Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.

Entrada
Como entrada solicite o consumo médio mensal de dados em GB (float).

Saída
Retorne o plano ideal para o cliente de acordo com o consumo informado na entrada.
'''

# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
# função input
consumo_medio_mensal = input("Qual o seu consumo de internet por mês:")

    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
consumo_medio_mensal = "sucesso" if saldo >= saque else "falha"

consumo_medio_mensal = int(input("Informe uma opção: [1]sacar \n [2]Extrato"))
if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print(' Exibindo o extrato...')
else :
    print('Opção Inválida')

# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))