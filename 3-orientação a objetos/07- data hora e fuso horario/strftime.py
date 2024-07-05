A função `strftime` em Python é usada para formatar objetos de data e hora como strings. Ela faz parte do módulo `datetime` e permite que você converta objetos `datetime` ou `time` em representações de string usando uma variedade de especificadores de formato.

Aqui está um exemplo básico de como usar `strftime`:

```python
from datetime import datetime

# Obtém a data e hora atual
agora = datetime.now()

# Formata a data e hora usando strftime
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

print(data_formatada)
```

No exemplo acima, a data e hora atual são obtidas usando `datetime.now()`, e então são formatadas como uma string no formato "dia/mês/ano horas:minutos:segundos" usando `strftime`.

Aqui estão alguns dos especificadores de formato mais comuns que você pode usar com `strftime`:

- `%a`: Nome abreviado do dia da semana (Ex: "Mon")
- `%A`: Nome completo do dia da semana (Ex: "Monday")
- `%w`: Dia da semana como um número decimal (0 = Sunday, 6 = Saturday)
- `%d`: Dia do mês como um número decimal (01-31)
- `%b`: Nome abreviado do mês (Ex: "Jan")
- `%B`: Nome completo do mês (Ex: "January")
- `%m`: Mês como um número decimal (01-12)
- `%y`: Ano sem o século (00-99)
- `%Y`: Ano com o século (Ex: "2023")
- `%H`: Hora (00-23)
- `%I`: Hora (01-12)
- `%p`: AM ou PM
- `%M`: Minuto (00-59)
- `%S`: Segundo (00-59)
- `%f`: Microsegundos (000000-999999)
- `%z`: Deslocamento do fuso horário em relação a UTC
- `%Z`: Nome do fuso horário
- `%j`: Dia do ano (001-366)
- `%U`: Número da semana do ano (domingo como o primeiro dia da semana)
- `%W`: Número da semana do ano (segunda-feira como o primeiro dia da semana)
- `%c`: Representação de data e hora apropriada para a localização (Ex: "Tue Aug 16 21:30:00 1988")
- `%x`: Representação de data apropriada para a localização (Ex: "08/16/88")
- `%X`: Representação de hora apropriada para a localização (Ex: "21:30:00")

Você pode combinar esses especificadores para criar a string de data e hora no formato que desejar.