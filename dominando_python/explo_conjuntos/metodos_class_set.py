"""A classe `set` em Python possui diversos métodos que permitem a manipulação e 
operações com conjuntos. A seguir, apresento uma lista abrangente dos
métodos mais comuns da classe `set`, juntamente com exemplos práticos de uso:
"""
### Métodos da Classe `set`

#1. **`add(elem)`**
 #  - Descrição: Adiciona o elemento `elem` ao set.
meu_set = {1, 2, 3}
meu_set.add(4)
print(meu_set)  # Output: {1, 2, 3, 4}

#2. **`clear()`**
  # - Descrição: Remove todos os elementos do set.
meu_set = {1, 2, 3}
meu_set.clear()
print(meu_set)  # Output: set()
#3. **`copy()`**
  # - Descrição: Retorna uma cópia superficial do set.
meu_set = {1, 2, 3}
copia_set = meu_set.copy()
print(copia_set)  # Output: {1, 2, 3}


#4. **`discard(elem)`**
  # - Descrição: Remove o elemento `elem` do set, se estiver presente. Não gera erro se o elemento não estiver no set.
meu_set = {1, 2, 3}
meu_set.discard(2)
print(meu_set)  # Output: {1, 3}

#5. **`pop()`**
  # - Descrição: Remove e retorna um elemento arbitrário do set. Gera um erro se o set estiver vazio.
meu_set = {1, 2, 3}
elemento_removido = meu_set.pop()
print(elemento_removido)  # Output: 1 (ou 2, ou 3, depende do elemento removido)
print(meu_set)  # Output: {2, 3} (ou {1, 3}, ou {1, 2}, depende do elemento removido)

#6. **`remove(elem)`**
   #- Descrição: Remove o elemento `elem` do set. Gera um erro se o elemento não estiver no set.
meu_set = {1, 2, 3}
meu_set.remove(2)
print(meu_set)  # Output: {1, 3}

#7. **`update(*others)`**
  # - Descrição: Atualiza o set adicionando elementos de outros iteráveis.
meu_set = {1, 2}
meu_set.update([3, 4], {5, 6})
print(meu_set)  # Output: {1, 2, 3, 4, 5, 6}

#8. **`union(*others)`**
  # - Descrição: Retorna a união do set com outros iteráveis.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
uniao = set1.union(set2)
print(uniao)  # Output: {1, 2, 3, 4, 5}

#9. **`intersection(*others)`**
   #- Descrição: Retorna a interseção do set com outros iteráveis.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersecao = set1.intersection(set2)
print(intersecao)  # Output: {2, 3}

#10. **`difference(*others)`**
   # - Descrição: Retorna a diferença entre o set e outros iteráveis.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
diferenca = set1.difference(set2)
print(diferenca)  # Output: {1}

#11. **`symmetric_difference(other)`**
  #  - Descrição: Retorna a diferença simétrica entre o set e outro iterável.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
dif_simetrica = set1.symmetric_difference(set2)
print(dif_simetrica)  # Output: {1, 4}
  

#12. **`issubset(other)`**
   # - Descrição: Retorna `True` se o set for um subconjunto de `other`.
      set1 = {1, 2, 3}
      set2 = {1, 2, 3, 4, 5}
      print(set1.issubset(set2))  # Output: True
      ```

#13. **`issuperset(other)`**
    # Descrição: Retorna `True` se o set for um superconjunto de `other`.
      set1 = {1, 2, 3, 4, 5}
      set2 = {1, 2, 3}
      print(set1.issuperset(set2))  # Output: True

#14. **`isdisjoint(other)`**
   # - Descrição: Retorna `True` se o set não tiver elementos em comum com `other`.
      set1 = {1, 2, 3}
      set2 = {4, 5, 6}
      print(set1.isdisjoint(set2))  # Output: True

### Operações com Sets

#Além dos métodos listados, sets suportam operações matemáticas usando operadores:

#**União (`|`)**
 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
uniao = set1 | set2
print(uniao)  # Output: {1, 2, 3, 4, 5}

#**Interseção (`&`)**

    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    intersecao = set1 & set2
    print(intersecao)  # Output: {2, 3}

#**Diferença (`-`)**
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    diferenca = set1 - set2
    print(diferenca)  # Output: {1}
    
 #**Diferença Simétrica (`^`)**
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    dif_simetrica = set1 ^ set2
    print(dif_simetrica)  # Output: {1, 4}
   