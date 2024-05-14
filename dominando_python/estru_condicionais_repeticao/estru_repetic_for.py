# estruturas de repetição  -> for / while

# repete trecho do código um determinado numero de vezes

texto = input("Informe um texto: ")

VOGAIS = "AEIOU"

for letra in texto :
    if letra.upper() in VOGAIS:
        print(letra, end=" ")


print()  # adiciona uma quebra de linha   