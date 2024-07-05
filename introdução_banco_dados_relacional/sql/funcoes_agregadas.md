Em um modelo relacional SQL, as funções agregadas são usadas para executar cálculos em um conjunto de valores e retornar um único valor resumido. Aqui estão algumas das funções agregadas mais comuns:

1. **SUM()**: Calcula a soma total de um conjunto de valores.
   ```sql
   SELECT SUM(coluna) FROM tabela;
   ```

2. **AVG()**: Calcula a média de um conjunto de valores.
   ```sql
   SELECT AVG(coluna) FROM tabela;
   ```

3. **COUNT()**: Conta o número de linhas em um conjunto de valores.
   ```sql
   SELECT COUNT(*) FROM tabela;
   SELECT COUNT(coluna) FROM tabela;
   ```

4. **MAX()**: Retorna o valor máximo em um conjunto de valores.
   ```sql
   SELECT MAX(coluna) FROM tabela;
   ```

5. **MIN()**: Retorna o valor mínimo em um conjunto de valores.
   ```sql
   SELECT MIN(coluna) FROM tabela;
   ```

6. **GROUP BY**: Utilizado em conjunto com as funções agregadas para agrupar resultados por uma ou mais colunas.
   ```sql
   SELECT coluna, SUM(outra_coluna)
   FROM tabela
   GROUP BY coluna;
   ```

7. **HAVING**: Filtra resultados após a aplicação da função agregada, semelhante ao WHERE, mas utilizado para filtrar grupos de dados.
   ```sql
   SELECT coluna, SUM(outra_coluna)
   FROM tabela
   GROUP BY coluna
   HAVING SUM(outra_coluna) > valor;
   ```

Essas funções são extremamente úteis para analisar dados e gerar relatórios resumidos a partir de grandes conjuntos de dados em um banco de dados relacional.