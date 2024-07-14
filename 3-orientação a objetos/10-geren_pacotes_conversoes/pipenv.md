Pipenv é uma ferramenta para gerenciar dependências de Python e ambientes virtuais, combinando as funcionalidades do `pip` (gerenciamento de pacotes) e do `virtualenv` (gerenciamento de ambientes virtuais). Aqui está um guia básico para usar o Pipenv:

### Instalação do Pipenv

Primeiro, você precisa instalar o Pipenv. Você pode fazer isso usando `pip`:

```sh
pip install pipenv
```

### Criar um Novo Projeto com Pipenv

1. **Navegue até o diretório do seu projeto**:
   ```sh
   cd /caminho/para/seu/projeto
   ```

2. **Crie um novo ambiente virtual e um arquivo `Pipfile`**:
   ```sh
   pipenv install
   ```
   Isso cria um ambiente virtual e um arquivo `Pipfile` no diretório do seu projeto.

3. **Adicionar pacotes ao seu projeto**:
   Para instalar um pacote, use:
   ```sh
   pipenv install nome_do_pacote
   ```
   Por exemplo, para instalar o `requests`:
   ```sh
   pipenv install requests
   ```

4. **Adicionar pacotes de desenvolvimento**:
   Para instalar pacotes que só são necessários durante o desenvolvimento (como linters, testadores, etc.), use:
   ```sh
   pipenv install nome_do_pacote --dev
   ```

### Usar o Ambiente Virtual do Pipenv

Para ativar o ambiente virtual, use:
```sh
pipenv shell
```
Isso ativa o ambiente virtual e permite que você execute comandos no contexto desse ambiente.

Para sair do ambiente virtual, simplesmente digite `exit`.

### Gerenciamento de Dependências

- **Atualizar pacotes**:
  ```sh
  pipenv update
  ```

- **Desinstalar pacotes**:
  ```sh
  pipenv uninstall nome_do_pacote
  ```

### Arquivos Pipfile e Pipfile.lock

- **Pipfile**: Este arquivo lista as dependências do seu projeto.
- **Pipfile.lock**: Este arquivo lista as versões exatas das dependências que foram instaladas. Isso garante que o ambiente seja reproduzível em qualquer máquina.

### Executar Scripts Python com Pipenv

Você pode executar scripts Python diretamente no ambiente do Pipenv sem ativá-lo explicitamente:
```sh
pipenv run python script.py
```

### Exemplo Prático

Aqui está um exemplo simples para criar um projeto com Pipenv:

1. **Crie o diretório do projeto e navegue até ele**:
   ```sh
   mkdir meu_projeto
   cd meu_projeto
   ```

2. **Inicie o ambiente do Pipenv**:
   ```sh
   pipenv install
   ```

3. **Instale uma dependência**:
   ```sh
   pipenv install requests
   ```

4. **Crie um script Python que use a dependência instalada**:
   Crie um arquivo `script.py` com o seguinte conteúdo:
   ```python
   import requests

   response = requests.get('https://api.github.com')
   print(response.json())
   ```

5. **Execute o script**:
   ```sh
   pipenv run python script.py
   ```

Seguindo esses passos, você terá configurado um ambiente virtual isolado para o seu projeto Python, gerenciado suas dependências de forma eficiente e garantido a reprodutibilidade do seu ambiente em qualquer máquina.