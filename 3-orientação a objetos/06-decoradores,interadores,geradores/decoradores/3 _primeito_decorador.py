def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")
    return envelope

def ola_mundo():
    print("olá mundo")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

#syntactic sugar
""" refere-se a recursos de uma linguagem de programação que não adicionam 
novas funcionalidades à linguagem, mas tornam o código mais fácil de ler, 
escrever e entender. Esses recursos são chamados de "açúcar" porque tornam a sintaxe 
da linguagem mais "doce" ou agradável, sem alterar a funcionalidade subjacente."""

def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")
    return envelope

@meu_decorador
def ola_mundo():
    print("olá mundo")
