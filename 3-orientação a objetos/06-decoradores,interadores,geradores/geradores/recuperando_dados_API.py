Para exemplificar o uso de um gerador em Python para recuperar dados de uma API, vamos criar um gerador que faz requisições a uma API paginada. APIs paginadas retornam resultados em partes (páginas), o que é útil quando se trabalha com grandes conjuntos de dados. O gerador permitirá que você recupere os dados página por página sem carregar todos os dados na memória de uma só vez.

Vamos usar a biblioteca `requests` para fazer as requisições HTTP. Suponha que estamos consultando uma API fictícia que retorna dados paginados sobre usuários.

### Passo 1: Criar o Gerador para Consultar a API Paginada

```python
import requests

def recuperar_usuarios(api_url):
    pagina = 1
    while True:
        response = requests.get(api_url, params={'page': pagina})
        dados = response.json()
        
        usuarios = dados.get('data', [])
        if not usuarios:
            break
        
        for usuario in usuarios:
            yield usuario
        
        pagina += 1

# URL fictícia da API
api_url = 'https://api.exemplo.com/usuarios'

# Usando o gerador
for usuario in recuperar_usuarios(api_url):
    print(usuario)
```

### Explicação

1. **Importar a Biblioteca `requests`**: Primeiro, importamos a biblioteca `requests` que será usada para fazer as requisições HTTP.

2. **Criar o Gerador `recuperar_usuarios`**: A função `recuperar_usuarios` é um gerador que faz requisições à API. Começa na primeira página (`pagina = 1`) e, em cada iteração do loop `while`, faz uma requisição GET à URL da API, passando o número da página como parâmetro.

3. **Processar a Resposta da API**: A resposta da API é convertida para JSON, e os dados dos usuários são extraídos. Se não houver mais usuários (ou seja, a lista `usuarios` estiver vazia), o loop é interrompido.

4. **Iterar sobre os Usuários**: Para cada usuário na lista, o gerador usa `yield` para retornar o usuário. Após processar todos os usuários da página atual, o gerador incrementa o número da página (`pagina += 1`) e continua para a próxima página.

5. **Usar o Gerador**: Finalmente, usamos o gerador em um loop `for` para iterar sobre todos os usuários retornados pela API, imprimindo cada um deles.

### Observação

No exemplo acima, a URL da API (`https://api.exemplo.com/usuarios`) é fictícia. Para usar com uma API real, você precisa substituir essa URL pela URL da API que você deseja consultar e ajustar a estrutura dos dados conforme necessário.

Esta abordagem permite que você recupere dados de uma API paginada de maneira eficiente, evitando carregar todos os dados na memória de uma só vez.