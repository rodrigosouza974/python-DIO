Gerenciar arquivos e diretórios em Python pode ser feito usando a biblioteca padrão `os` e `shutil`. Essas bibliotecas fornecem várias funções para criar, excluir, renomear e mover arquivos e diretórios. Aqui estão alguns exemplos básicos de como usar essas funções.

### Importar Bibliotecas Necessárias

```python
import os
import shutil
```

### Trabalhando com Diretórios

1. **Criar um Diretório:**

```python
os.mkdir('novo_diretorio')
```

2. **Criar Diretórios Recursivamente:**

```python
os.makedirs('novo_diretorio/subdiretorio')
```

3. **Listar Arquivos e Diretórios:**

```python
conteudo = os.listdir('caminho/do/diretorio')
print(conteudo)
```

4. **Mudar o Diretório Atual:**

```python
os.chdir('caminho/do/diretorio')
```

5. **Obter o Diretório Atual:**

```python
diretorio_atual = os.getcwd()
print(diretorio_atual)
```

6. **Remover um Diretório Vazio:**

```python
os.rmdir('diretorio_vazio')
```

7. **Remover Diretórios Recursivamente:**

```python
shutil.rmtree('diretorio_com_arquivos')
```

### Trabalhando com Arquivos

1. **Renomear ou Mover um Arquivo:**

```python
os.rename('arquivo_antigo.txt', 'novo_arquivo.txt')
```

2. **Copiar um Arquivo:**

```python
shutil.copy('arquivo_origem.txt', 'caminho/destino/arquivo_copiado.txt')
```

3. **Remover um Arquivo:**

```python
os.remove('arquivo_para_remover.txt')
```

### Exemplo Completo

Aqui está um exemplo completo que cobre a criação, movimentação e exclusão de arquivos e diretórios:

```python
import os
import shutil

# Criar um novo diretório
os.mkdir('exemplo_diretorio')

# Criar um subdiretório
os.makedirs('exemplo_diretorio/subdiretorio')

# Listar o conteúdo do diretório atual
conteudo = os.listdir('.')
print('Conteúdo do diretório atual:', conteudo)

# Criar um novo arquivo dentro do diretório criado
with open('exemplo_diretorio/arquivo.txt', 'w') as file:
    file.write('Conteúdo do arquivo.')

# Listar o conteúdo do novo diretório
conteudo = os.listdir('exemplo_diretorio')
print('Conteúdo do diretório exemplo_diretorio:', conteudo)

# Mover o arquivo para o subdiretório
os.rename('exemplo_diretorio/arquivo.txt', 'exemplo_diretorio/subdiretorio/arquivo.txt')

# Listar o conteúdo do subdiretório
conteudo = os.listdir('exemplo_diretorio/subdiretorio')
print('Conteúdo do subdiretório:', conteudo)

# Copiar o arquivo de volta para o diretório principal
shutil.copy('exemplo_diretorio/subdiretorio/arquivo.txt', 'exemplo_diretorio/arquivo_copiado.txt')

# Remover o arquivo original
os.remove('exemplo_diretorio/subdiretorio/arquivo.txt')

# Remover o subdiretório
os.rmdir('exemplo_diretorio/subdiretorio')

# Remover o diretório principal e seu conteúdo
shutil.rmtree('exemplo_diretorio')
```

Esses exemplos mostram como realizar operações básicas de gerenciamento de arquivos e diretórios em Python. Se você precisar de funções mais avançadas ou tiver outras perguntas, fique à vontade para perguntar!