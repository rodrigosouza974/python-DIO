# objetivo geral
'''
conhecer métodos úteispara manipular objetos do tipo string,
como interpolar valores de variáveis e entender como funciona o fatiamento.
'''
# Maiúsculas, miúsculas e título

curso ="pYtHon"
print(curso.upper())
print(curso.lower())
print(curso.title())

# Eliminando espaços em branco

curso ="  python  "
print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())

# Junções e centralizações

curso ="python"
print(curso.center(10,"#"))

print(".".join(curso))

