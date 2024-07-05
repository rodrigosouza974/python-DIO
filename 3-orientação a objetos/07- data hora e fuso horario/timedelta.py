Para um esquema de lavagem de carros onde você precisa calcular a data e hora em que o carro ficará pronto, você pode usar o módulo `datetime` para adicionar a duração da lavagem à data e hora de chegada do carro.

Aqui está um exemplo:

1. **Importar a biblioteca necessária**:
   ```python
   from datetime import datetime, timedelta
   ```

2. **Definir a data e hora de chegada do carro e a duração da lavagem**:
   ```python
   chegada = datetime(2024, 7, 2, 10, 0, 0)  # 2 de julho de 2024, às 10:00
   duracao_lavagem = timedelta(hours=2, minutes=30)  # duração de 2 horas e 30 minutos
   ```

3. **Calcular a data e hora de término da lavagem**:
   ```python
   termino = chegada + duracao_lavagem
   ```

4. **Exibir a data e hora de término**:
   ```python
   print("Data e hora de chegada:", chegada)
   print("Duração da lavagem:", duracao_lavagem)
   print("Data e hora de término:", termino)
   ```

Aqui está o código completo:

```python
from datetime import datetime, timedelta

# Definindo a data e hora de chegada do carro e a duração da lavagem
chegada = datetime(2024, 7, 2, 10, 0, 0)  # 2 de julho de 2024, às 10:00
duracao_lavagem = timedelta(hours=2, minutes=30)  # duração de 2 horas e 30 minutos

# Calculando a data e hora de término da lavagem
termino = chegada + duracao_lavagem

# Exibindo a data e hora de chegada, a duração e a data e hora de término
print("Data e hora de chegada:", chegada)
print("Duração da lavagem:", duracao_lavagem)
print("Data e hora de término:", termino)
```

Este exemplo mostra como você pode calcular a data e hora em que a lavagem do carro estará concluída, adicionando a duração da lavagem à data e hora de chegada do carro.