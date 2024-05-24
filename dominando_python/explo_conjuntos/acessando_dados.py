"""conjuntos em python não suportam indexação e nem fatiamento, 
caso queira acessar os seus valores é necessário converter
o conjunto para lista."""
numeros = (1, 2, 3, 2)
#print(numeros[0]) ira dar erro

numeros = list(numeros)
print(numeros[0])

#interar conjuntos
"""a forma mais comum para percorrer ps dados de um conjunto
é utilizandoo comando for"""
carros ={"gol", "celta", "fiat"}
for carro in carros:
    print(carros)

#função enumerate: para saber o numero do indice

frutas ={"uva", "caja", "laranja"}
for indice, fruta in enumerate(frutas):
    print(f"{indice}:{frutas}")