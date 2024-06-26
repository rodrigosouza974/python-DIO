'''# break
while True:
    numero = int(input("Informe  o numero: "))

    if numero == 10 :
        break

print('loop interrompido...')
'''
# retorna somente os numeros impares. continue pula a execução ,o numero nesse caso
for numero in range (100):

    if numero % 2 == 0:
        continue

    print(numero, end =" ")
