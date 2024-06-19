A validação de números de telefone utilizando expressões regulares (regex) pode variar dependendo do formato dos números de telefone que você deseja validar. Vou fornecer alguns exemplos comuns de como você pode usar regex para essa tarefa:

### Exemplos de Padrões de Números de Telefone

1. **Formato básico de 10 dígitos**: Este formato é comum em muitos países, incluindo os EUA.
   - Exemplo: `1234567890`
   - Regex: `^\d{10}$`

2. **Formato com hífens ou espaços**: Este formato permite hífens ou espaços como separadores.
   - Exemplo: `123-456-7890` ou `123 456 7890`
   - Regex: `^\d{3}[-\s]?\d{3}[-\s]?\d{4}$`

3. **Formato com parênteses e espaços**: Este formato é comum para números de telefone dos EUA com o código de área entre parênteses.
   - Exemplo: `(123) 456-7890`
   - Regex: `^\(\d{3}\)\s\d{3}-\d{4}$`

4. **Formato internacional**: Este formato permite o código do país com o sinal de mais (+).
   - Exemplo: `+1-123-456-7890` ou `+12 123 456 7890`
   - Regex: `^\+\d{1,3}[-\s]?\d{1,4}[-\s]?\d{1,4}[-\s]?\d{1,9}$`

### Exemplo de Código Python

Aqui está um exemplo de como usar regex em Python para validar diferentes formatos de números de telefone:

```python
import re

# Lista de exemplos de números de telefone
numeros_telefone = [
    "1234567890",
    "123-456-7890",
    "123 456 7890",
    "(123) 456-7890",
    "+1-123-456-7890",
    "+12 123 456 7890"
]

# Padrões regex para diferentes formatos
padroes = [
    r'^\d{10}$',
    r'^\d{3}[-\s]?\d{3}[-\s]?\d{4}$',
    r'^\(\d{3}\)\s\d{3}-\d{4}$',
    r'^\+\d{1,3}[-\s]?\d{1,4}[-\s]?\d{1,4}[-\s]?\d{1,9}$'
]

def validar_telefone(numero):
    for padrao in padroes:
        if re.match(padrao, numero):
            return True
    return False

# Validar e imprimir resultados
for numero in numeros_telefone:
    if validar_telefone(numero):
        print(f"{numero}: Válido")
    else:
        print(f"{numero}: Inválido")
```

### Explicação dos Padrões

1. **^\d{10}$**:
   - `^`: Início da string.
   - `\d{10}`: Exatamente 10 dígitos.
   - `$`: Fim da string.

2. **^\d{3}[-\s]?\d{3}[-\s]?\d{4}$**:
   - `\d{3}`: Três dígitos.
   - `[-\s]?`: Opcional hífen ou espaço.
   - `\d{3}`: Três dígitos.
   - `[-\s]?`: Opcional hífen ou espaço.
   - `\d{4}`: Quatro dígitos.

3. **^\(\d{3}\)\s\d{3}-\d{4}$**:
   - `\(\d{3}\)`: Três dígitos entre parênteses.
   - `\s`: Um espaço.
   - `\d{3}`: Três dígitos.
   - `-`: Um hífen.
   - `\d{4}`: Quatro dígitos.

4. **^\+\d{1,3}[-\s]?\d{1,4}[-\s]?\d{1,4}[-\s]?\d{1,9}$**:
   - `\+`: Sinal de mais.
   - `\d{1,3}`: Um a três dígitos.
   - `[-\s]?`: Opcional hífen ou espaço.
   - `\d{1,4}`: Um a quatro dígitos (repetido duas vezes).
   - `\d{1,9}`: Um a nove dígitos.

Dessa forma, você pode adaptar os padrões de regex conforme necessário para outros formatos específicos de números de telefone que você precisa validar.