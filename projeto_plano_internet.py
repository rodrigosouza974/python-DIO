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
consumo_medio_mensal = 0

print("""
========================================
 Solicitação de Consumo de Internet 
========================================

Planos Oferecidos:
      
- Plano Essencial Fibra - 50Mbps:
      
     Recomendado para um consumo médio de até 10 GB.
      
- Plano Prata Fibra    - 100Mbps: 
      
      Recomendado para um consumo médio acima de 10 GB até 20 GB.
      
- Plano Premium Fibra  - 300Mbps: 
      
      Recomendado para um consumo médio acima de 20 GB.

============================================================

      Por favor, informe seu consumo médio de internet em GB:

      """)
# Solicita ao usuário que insira o consumo médio mensal de dados:
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
def obter_consumo_mensal():
    while True:
        try:
            # Tenta converter o input para float
            consumo_medio_mensal = float(input("Qual o seu consumo de internet por mês: "))
            return consumo_medio_mensal
        except ValueError:
            # Se a conversão falhar, exibe uma mensagem de erro e pede novamente
            print("Por favor, insira um número válido.")

obter_consumo_mensal()

# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo_medio_mensal):
    if consumo_medio_mensal < 10.0:
        return " O Plano recomendado  é O Essencial Fibra - 50Mbps"
    elif 10.0 < consumo_medio_mensal < 20.0:
        return " O Plano recomendado  é O Plano Prata Fibra - 100Mbps"
    else:
        return " O Plano recomendado  é O Plano Premium Fibra  - 300Mbps"
    
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
# TODO: Retorne o plano de internet adequado:
resultado = recomendar_plano(consumo_medio_mensal)
print(resultado)