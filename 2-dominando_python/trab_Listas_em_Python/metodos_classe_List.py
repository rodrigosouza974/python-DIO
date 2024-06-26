#  []. append adiciona o elemento a lista

lista = []
lista.append(2)
lista.append("rodrigo")
lista.append([20,34,37])

print(lista)

#  []. clear elimina o elemento a lista

lista.clear()
print(lista)

#  []. copy faz uma copia da lista

lista2 = lista.copy()
print(lista2)
print(id(lista2),id(lista))# mostra que são dois objetos diferentes

#  [].count quantas vezes um objeto aparece dentro da minha lista
numeros = [1,2,7,3,4,8,4,7,2,5,2,7,3]
print(numeros.count(4))

#  [].extend  juntar duas listas
palavras =["rodrigo","ana" ,"rafael"]
palavras.extend([1,2,5,2,7,3])
print(palavras)

#  [].index  em  qual posição está
palavras =["rodrigo","ana" ,"rafael"]
print(palavras.index("ana"))

#  [].pop  retira o ultimo elemento adicionado, como o modelo pilha em estrutura de dados
palavras =["rodrigo","ana" ,"rafael"]
palavras.pop()
print(palavras)



