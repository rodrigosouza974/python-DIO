def meu_decorador(funcao):
    def envelope(*args,**kargs):
        print("faz algo antes de executar")
        resultado = funcao(*args,**kargs)
        print("faz algo depois de executar")
        return resultado
    return envelope

@meu_decorador
def ola_mundo(nome,outro_argumento):
    print(f"olá mundo {nome}")

ola_mundo("rodrigo", 100)