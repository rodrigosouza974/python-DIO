"""No Python, a partir da versão 3.8, foi introduzida a capacidade de definir parâmetros de função que são apenas posicionais. Isso significa que tais parâmetros não podem ser passados como argumentos nomeados quando a função é chamada. Esse recurso é útil para criar APIs mais claras e prevenir a passagem de argumentos nomeados de maneira incorreta.
"""
### Sintaxe de Parâmetros Apenas Posicionais

"""Para definir parâmetros apenas posicionais, você usa 
a barra `/` na definição da função. Todos os parâmetros
 à esquerda da barra são considerados apenas posicionais.
"""
def funcao(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print(pos1, pos2, pos_or_kwd, kwd1, kwd2)

"""- `pos1` e `pos2` são apenas posicionais.
- `pos_or_kwd` pode ser posicional ou nomeado.
- `kwd1` e `kwd2` são apenas nomeados.
"""
### Exemplos Práticos

#### 1. Parâmetros Apenas Posicionais
def somar(a, b, /):
    return a + b

# Chamadas válidas
print(somar(1, 2))  # Saída: 3

# Chamadas inválidas
# print(somar(a=1, b=2))  
# # TypeError: somar() got some positional-only arguments passed as keyword arguments: 'a, b'

#### 2. Função com Parâmetros Mistos
def funcao_mista(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print(f"pos1: {pos1}, pos2: {pos2}, pos_or_kwd: {pos_or_kwd}, kwd1: {kwd1}, kwd2: {kwd2}")

# Chamadas válidas
funcao_mista(1, 2, 3, kwd1='a', kwd2='b')
# Saída: pos1: 1, pos2: 2, pos_or_kwd: 3, kwd1: a, kwd2: b

funcao_mista(1, 2, pos_or_kwd=3, kwd1='a', kwd2='b')
# Saída: pos1: 1, pos2: 2, pos_or_kwd: 3, kwd1: a, kwd2: b

# Chamadas inválidas
# funcao_mista(1, pos2=2, pos_or_kwd=3, kwd1='a', kwd2='b') 
#  # TypeError: funcao_mista() got some positional-only arguments passed as keyword arguments: 'pos2'

### Vantagens de Usar Parâmetros Apenas Posicionais

"""1. **Clareza na API**: Ao forçar certos parâmetros a 
serem apenas posicionais, você evita a passagem de argumentos
 nomeados que podem causar confusão.
2. **Desempenho**: Funções com parâmetros apenas posicionais
 podem ter um desempenho ligeiramente melhor, pois o Python
   não precisa resolver nomes dos argumentos.
3. **Compatibilidade**: Facilita a criação de funções que 
precisam manter compatibilidade com versões anteriores de APIs
 onde os nomes dos parâmetros podem ter mudado.
"""
### Conclusão

""" parâmetros apenas posicionais são um recurso poderoso
 para controlar como funções são chamadas e garantir que APIs 
 sejam usadas corretamente. Esse recurso adiciona uma camada 
 adicional de robustez e clareza ao design das funções em Python.
   A barra `/` na definição da função especifica claramente quais
     parâmetros devem ser passados sem nomes, ajudando a evitar 
     erros comuns ao passar argumentos.

Aproveitar-se dessa funcionalidade pode tornar seu código mais 
legível e evitar muitos erros relacionados à passagem de 
argumentos, especialmente em APIs complexas."""