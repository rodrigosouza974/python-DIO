`venv` é um módulo embutido no Python a partir da versão 3.3, que pode ser usado para criar ambientes virtuais. Ele é uma alternativa mais simples e direta ao `virtualenv`. Aqui está como você pode usar `venv` para gerenciar ambientes virtuais:

### Passo 1: Criar um Ambiente Virtual
Primeiro, navegue até o diretório do seu projeto e execute o seguinte comando para criar um novo ambiente virtual:

```sh
python -m venv nome_do_ambiente
```

Substitua `nome_do_ambiente` pelo nome que você deseja dar ao seu ambiente virtual.

### Passo 2: Ativar o Ambiente Virtual
Para ativar o ambiente virtual, use o seguinte comando:

- No Windows:

  ```sh
  nome_do_ambiente\Scripts\activate
  ```

- No macOS ou Linux:

  ```sh
  source nome_do_ambiente/bin/activate
  ```

Quando o ambiente virtual estiver ativado, você verá o nome dele no início do prompt do terminal, indicando que ele está ativo.

### Passo 3: Instalar Pacotes
Com o ambiente virtual ativo, você pode instalar pacotes específicos do projeto usando `pip`:

```sh
pip install nome_do_pacote
```

### Passo 4: Desativar o Ambiente Virtual
Para desativar o ambiente virtual, basta executar:

```sh
deactivate
```

### Passo 5: Gerar e Usar o `requirements.txt`
É uma boa prática salvar as dependências do seu projeto em um arquivo `requirements.txt`. Para gerar este arquivo, execute:

```sh
pip freeze > requirements.txt
```

Para instalar as dependências listadas em um `requirements.txt` em um novo ambiente virtual, use:

```sh
pip install -r requirements.txt
```

### Exemplo Prático
Aqui está um exemplo completo de como você pode configurar e usar um ambiente virtual com `venv`:

1. **Criar um novo ambiente virtual chamado `meu_ambiente`**:

   ```sh
   python -m venv meu_ambiente
   ```

2. **Ativar o ambiente virtual**:

   - No Windows:

     ```sh
     meu_ambiente\Scripts\activate
     ```

   - No macOS ou Linux:

     ```sh
     source meu_ambiente/bin/activate
     ```

3. **Instalar pacotes necessários**:

   ```sh
   pip install numpy pandas
   ```

4. **Salvar as dependências em `requirements.txt`**:

   ```sh
   pip freeze > requirements.txt
   ```

5. **Desativar o ambiente virtual**:

   ```sh
   deactivate
   ```

6. **Para recriar o ambiente em outro local, ative o ambiente e instale as dependências**:

   ```sh
   python -m venv novo_ambiente
   source novo_ambiente/bin/activate
   pip install -r requirements.txt
   ```

Seguindo esses passos, você poderá usar `venv` para gerenciar seus projetos Python de maneira eficiente e organizada.