# String múltiplas linhas
'''String de múltiplas linhas são definidas informando 3 aspas
simples ou duplas durante a atribuição. elas podem ocupar
várias linhas do código , e todos os espaços em branco são 
incluidos na string final.'''

nome = 'guilherme'
mensagem =f""" oi, 
meu 
    nome 
             é 
                {nome}."""
print(mensagem)

pagina_texto = """
==================================================
                  Página Inicial                   
==================================================

Bem-vindo à nossa aplicação! Aqui estão algumas 
informações importantes:

- Opção 1: Visualizar dados
- Opção 2: Atualizar informações
- Opção 3: Sair

Por favor, escolha uma das opções acima para 
continuar.

==================================================
"""

print(pagina_texto)
