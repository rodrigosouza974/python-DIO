### Definição de Funções
def nome_da_funcao(parametros):
    # Bloco de código da função
    return valor_de_retorno

### Exemplos de Funções

#### 1. Função Simples Sem Parâmetros
def saudacao():
    print("Olá, bem-vindo!")

# Chamando a função
saudacao()

#### 2. Função com Parâmetros
def soma(a, b):
    return a + b

# Chamando a função e imprimindo o resultado
resultado = soma(3, 5)
print("A soma é:", resultado)


#### 3. Função com Valor Padrão para Parâmetros
def potencia(base, expoente=2):
    return base ** expoente

# Chamando a função com e sem o valor padrão
print("2^3:", potencia(2, 3))
print("3^2:", potencia(3))


#### 4. Função com Número Variável de Argumentos
def soma_varios(*numeros):
    return sum(numeros)

# Chamando a função com diferentes números de argumentos
print("Soma de 1, 2, 3:", soma_varios(1, 2, 3))
print("Soma de 4, 5:", soma_varios(4, 5))

#### 5. Função com Parâmetros Nomeados
def exibir_info(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

# Chamando a função com argumentos nomeados
exibir_info(nome="Alice", idade=30)
exibir_info(idade=25, nome="Bob")

#### 6. Função com Retorno de Múltiplos Valores
def operacoes(a, b):
    soma = a + b
    diferenca = a - b
    produto = a * b
    quociente = a / b
    return soma, diferenca, produto, quociente

# Chamando a função e desempacotando os resultados
resultado = operacoes(10, 2)
print("Soma:", resultado[0])
print("Diferença:", resultado[1])
print("Produto:", resultado[2])
print("Quociente:", resultado[3])

# Outra forma de desempacotar
soma, diferenca, produto, quociente = operacoes(10, 2)
print("Soma:", soma)
print("Diferença:", diferenca)
print("Produto:", produto)
print("Quociente:", quociente)

### Funções Lambda (Funções Anônimas)
# Função lambda que soma dois números
soma = lambda a, b: a + b

# Chamando a função lambda
print("Soma usando lambda:", soma(3, 5))

# Função lambda sem parâmetros
ola_mundo = lambda: "Olá, mundo!"

# Chamando a função lambda sem parâmetros
print(ola_mundo())

### Funções como Argumentos
def aplicar_operacao(a, b, operacao):
    return operacao(a, b)

# Funções normais
def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

# Usando as funções como argumentos
resultado_soma = aplicar_operacao(5, 3, soma)
resultado_mult = aplicar_operacao(5, 3, multiplicacao)

print("Resultado da soma:", resultado_soma)
print("Resultado da multiplicação:", resultado_mult)

# Usando lambda como argumento
resultado_lambda = aplicar_operacao(5, 3, lambda a, b: a - b)
print("Resultado da subtração com lambda:", resultado_lambda)


