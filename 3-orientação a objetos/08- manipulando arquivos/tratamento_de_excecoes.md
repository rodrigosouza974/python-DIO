Existem vários tipos de exceções relacionadas à manipulação de arquivos em Python, especialmente quando se trata de operações de leitura e escrita. Aqui estão algumas das exceções mais comuns que você pode encontrar:

1. **FileNotFoundError**: Ocorre quando se tenta abrir um arquivo que não existe.
2. **PermissionError**: Ocorre quando o programa não tem permissões necessárias para acessar o arquivo.
3. **IOError**: Erro genérico de entrada/saída. Desde o Python 3.3, é uma subclasse de `OSError`.
4. **OSError**: Erro genérico relacionado ao sistema operacional, pode ocorrer em operações de arquivo.
5. **IsADirectoryError**: Ocorre quando se tenta abrir um diretório como se fosse um arquivo.
6. **NotADirectoryError**: Ocorre quando se espera um diretório, mas encontra um arquivo.
7. **EOFError**: Ocorre quando o final de um arquivo é alcançado inesperadamente.
8. **UnsupportedOperation**: Ocorre quando uma operação não é suportada pelo objeto de arquivo.
9. **UnicodeDecodeError**: Ocorre quando a decodificação de bytes em uma string falha devido a uma incompatibilidade de codificação.
10. **UnicodeEncodeError**: Ocorre quando a codificação de uma string em bytes falha devido a uma incompatibilidade de codificação.
11. **UnicodeError**: Erro genérico relacionado a operações de Unicode.

Aqui está um exemplo de como essas exceções podem ser usadas no contexto de manipulação de arquivos:

```python
try:
    with open('example.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except PermissionError:
    print("Você não tem permissão para acessar este arquivo.")
except IsADirectoryError:
    print("Esperava um arquivo, mas encontrou um diretório.")
except NotADirectoryError:
    print("Esperava um diretório, mas encontrou um arquivo.")
except UnicodeDecodeError:
    print("Erro ao decodificar o arquivo. Verifique a codificação.")
except IOError as e:
    print(f"Ocorreu um erro de I/O: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
else:
    print("O arquivo foi lido com sucesso.")
finally:
    print("Operação de leitura de arquivo concluída.")
```

Ao capturar essas exceções, você pode lidar de maneira mais específica e informativa com diferentes tipos de erros que podem ocorrer durante a manipulação de arquivos em Python.