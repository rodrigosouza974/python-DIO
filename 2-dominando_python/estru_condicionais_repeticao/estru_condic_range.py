'''

range é uma função built-in do python, ela ´w usada para
produzir uma sequência de números inteiros a partir de 
um início (inclusivo) para um fim(exclusivo). se usarmos range(i,f)
será produzido:

i, i+1,i+2,i+3,i+4,...,j+1.
ele recebe 3 argumentos:stop(obrigatorio),start(opcional) e step opicional.

# range(stop) -> range object
# range (start, stop[,step]) -> range object

list(range(4))

'''

# utilizando range com for

for numero in range (0,11):
    print(numero, end =" ")

# exibindo tabuada do 5
for numero in range (0,51,5):
    print(numero, end =" ")
    
    #end =" " deixa os numeros exibibidos um ao lado do outro