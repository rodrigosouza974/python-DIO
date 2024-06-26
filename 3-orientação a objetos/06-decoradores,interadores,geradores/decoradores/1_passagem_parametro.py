def mensagem (nome):
    print("executar mensagem")
    return f"oi {nome}"

def mensagem_longa (nome):
    print("executar mensagem longa")
    return f"olá tudo bem com você {nome} ?"

def executar (funcao,nome):
    print("executar executar")
    return funcao (nome)

print(executar(mensagem, "rodrigo"))
print(executar(mensagem_longa, "rodrigo"))
