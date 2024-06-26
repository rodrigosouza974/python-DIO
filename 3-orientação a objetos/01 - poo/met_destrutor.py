"""O método destrutor em Python é um método especial 
chamado `__del__`. Ele é chamado quando um objeto está 
prestes a ser destruído. O destrutor é útil para liberar 
recursos que o objeto possa ter adquirido durante sua vida 
útil, como arquivos abertos, conexões de rede ou outros recursos externos.
"""
### Como Funciona o Método Destrutor

"""- **Nome do Método**: `__del__`
- **Execução**: Chamado automaticamente quando o contador 
de referências de um objeto chega a zero, ou seja, quando 
não há mais referências ao objeto e o Python decide coletar o lixo (garbage collection).
"""
### Exemplo de Uso do Método Destrutor

"""Vamos criar uma classe que utiliza o método destrutor 
para fechar um arquivo quando o objeto for destruído.
"""
class Arquivo:
    def __init__(self, nome_arquivo, modo):
        self.nome_arquivo = nome_arquivo
        self.arquivo = open(nome_arquivo, modo)
        print(f"Arquivo {nome_arquivo} aberto.")

    def escrever(self, conteudo):
        self.arquivo.write(conteudo)
        print(f"Escrito no arquivo {self.nome_arquivo}.")

    def __del__(self):
        self.arquivo.close()
        print(f"Arquivo {self.nome_arquivo} fechado.")

# Uso da classe Arquivo
arquivo = Arquivo("exemplo.txt", "w")
arquivo.escrever("Olá, mundo!")

# Deletando o objeto manualmente para acionar o destrutor
del arquivo

### Explicação

"""1. **Método `__init__`**:
    - Abre um arquivo e inicializa o atributo `arquivo` com a referência ao arquivo aberto.
    - Imprime uma mensagem indicando que o arquivo foi aberto.

2. **Método `escrever`**:
    - Escreve o conteúdo fornecido no arquivo.
    - Imprime uma mensagem indicando que o conteúdo foi escrito.

3. **Método `__del__`**:
    - Fecha o arquivo quando o objeto está prestes a ser destruído.
    - Imprime uma mensagem indicando que o arquivo foi fechado."""

### Uso da Classe `Arquivo`

#- **Criação da Instância**:
   
arquivo = Arquivo("exemplo.txt", "w")
   
   # - Abre o arquivo "exemplo.txt" para escrita e imprime "Arquivo exemplo.txt aberto."

#- **Escrita no Arquivo**:
   
arquivo.escrever("Olá, mundo!")
   
   # - Escreve "Olá, mundo!" no arquivo e imprime "Escrito no arquivo exemplo.txt."

#- **Destruição do Objeto**:
    
del arquivo
    
    #- Fecha o arquivo quando o objeto `arquivo` é deletado, acionando o método `__del__` e imprimindo "Arquivo exemplo.txt fechado."

### Observações Importantes

"""1. **Coleta de Lixo (Garbage Collection)**:
    - O método `__del__` não é garantido de ser chamado imediatamente após o último uso do objeto, pois depende do garbage collector do Python.
    - É uma prática recomendada não depender de `__del__` para liberar recursos críticos. Em vez disso, use métodos de gerenciamento de contexto (`with` statement) ou finalize explicitamente os recursos com métodos específicos (como `close()`).

2. **Alternativa: Gerenciamento de Contexto**:
    - Para recursos como arquivos, o gerenciamento de contexto com a declaração `with` é geralmente preferido.
 """
with open("exemplo.txt", "w") as arquivo:
        arquivo.write("Olá, mundo!")
    
    #- O bloco `with` garante que o arquivo seja fechado corretamente após sua execução, mesmo que ocorra uma exceção.

### Exemplo com Gerenciamento de Contexto

#Para comparação, vamos ver como o exemplo acima ficaria usando gerenciamento de contexto:

class Arquivo:
    def __init__(self, nome_arquivo, modo):
        self.nome_arquivo = nome_arquivo
        self.modo = modo

    def __enter__(self):
        self.arquivo = open(self.nome_arquivo, self.modo)
        print(f"Arquivo {self.nome_arquivo} aberto.")
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.arquivo.close()
        print(f"Arquivo {self.nome_arquivo} fechado.")

# Uso da classe Arquivo com gerenciamento de contexto
with Arquivo("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!")


### Resumo

"""- **Método `__del__`**: Usado para definir ações de limpeza quando um objeto é destruído.
- **Uso Típico**: Liberar recursos como arquivos abertos, conexões de rede, etc.
- **Limitações**: Não é garantido que seja chamado imediatamente após o 
último uso do objeto. Melhor usar `with` statement para gerenciamento de recursos.

O método destrutor pode ser útil, mas devido à natureza do garbage 
collection em Python, é importante conhecer suas limitações e preferir
 outras práticas de gerenciamento de recursos quando apropriado."""