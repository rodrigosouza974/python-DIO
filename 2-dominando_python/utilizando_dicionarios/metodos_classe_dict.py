def main():
    # Criar um dicionário inicial
    meu_dicionario = {'a': 1, 'b': 2, 'c': 3}
    print("Dicionário inicial:", meu_dicionario)

    # Método clear(): Remove todos os itens do dicionário
    copia_dicionario = meu_dicionario.copy()  # Fazendo uma cópia para demonstrar o clear
    copia_dicionario.clear()
    print("Após clear:", copia_dicionario)

    # Método copy(): Retorna uma cópia rasa do dicionário
    copia_dicionario = meu_dicionario.copy()
    print("Cópia do dicionário:", copia_dicionario)

    # Método fromkeys(): Cria um novo dicionário com chaves de um iterável e valores definidos como 'value'
    novo_dicionario = dict.fromkeys(['x', 'y', 'z'], 0)
    print("Dicionário criado com fromkeys:", novo_dicionario)

    # Método get(): Retorna o valor para a chave especificada, ou 'default' se a chave não estiver no dicionário
    valor_a = meu_dicionario.get('a')
    valor_nao_existente = meu_dicionario.get('d', 'padrão')
    print("Valor da chave 'a' com get:", valor_a)
    print("Valor da chave não existente com get:", valor_nao_existente)

    # Método items(): Retorna uma visão dos pares chave-valor do dicionário
    print("Pares chave-valor com items:", list(meu_dicionario.items()))

    # Método keys(): Retorna uma visão das chaves do dicionário
    print("Chaves do dicionário com keys:", list(meu_dicionario.keys()))

    # Método pop(): Remove e retorna o valor para a chave especificada. Se a chave não estiver presente, retorna 'default'
    valor_removido = meu_dicionario.pop('b')
    print("Valor removido da chave 'b' com pop:", valor_removido)
    print("Dicionário após pop:", meu_dicionario)

    # Método popitem(): Remove e retorna um par chave-valor arbitrário do dicionário
    chave, valor = meu_dicionario.popitem()
    print("Par chave-valor removido com popitem:", chave, valor)
    print("Dicionário após popitem:", meu_dicionario)

    # Método setdefault(): Retorna o valor da chave se estiver no dicionário; se não, insere a chave com 'default' e retorna 'default'
    valor_c = meu_dicionario.setdefault('c', 5)
    valor_d = meu_dicionario.setdefault('d', 5)
    print("Valor da chave 'c' após setdefault:", valor_c)
    print("Valor da chave 'd' após setdefault:", valor_d)
    print("Dicionário após setdefault:", meu_dicionario)

    # Método update(): Atualiza o dicionário com os pares chave-valor de outro dicionário ou de um iterável de pares chave-valor
    meu_dicionario.update({'e': 5, 'f': 6})
    print("Dicionário após update:", meu_dicionario)

    # Método values(): Retorna uma visão dos valores no dicionário
    print("Valores do dicionário com values:", list(meu_dicionario.values()))

if __name__ == "__main__":
    main()
