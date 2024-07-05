Em Python, você pode manipular fuso horário utilizando a biblioteca `pytz` junto com o módulo `datetime`. Abaixo estão alguns exemplos de como fazer isso:

1. **Instalar a biblioteca `pytz`**:
   Primeiro, você precisa instalar a biblioteca `pytz` se ainda não tiver feito isso. Você pode instalar usando `pip`:
   ```bash
   pip install pytz
   ```

2. **Trabalhar com fusos horários**:
   Aqui está um exemplo de como obter a data e hora atual em diferentes fusos horários:

   ```python
   from datetime import datetime
   import pytz

   # Fuso horário UTC
   utc_zone = pytz.utc
   utc_time = datetime.now(utc_zone)
   print("UTC:", utc_time)

   # Fuso horário específico (exemplo: América/São_Paulo)
   sao_paulo_zone = pytz.timezone('America/Sao_Paulo')
   sao_paulo_time = utc_time.astimezone(sao_paulo_zone)
   print("São Paulo:", sao_paulo_time)

   # Fuso horário específico (exemplo: Europa/Londres)
   london_zone = pytz.timezone('Europe/London')
   london_time = utc_time.astimezone(london_zone)
   print("Londres:", london_time)
   ```

3. **Converter entre fusos horários**:
   Você pode converter uma data e hora de um fuso horário para outro. Aqui está um exemplo:

   ```python
   from datetime import datetime
   import pytz

   # Fuso horário América/São_Paulo
   sao_paulo_zone = pytz.timezone('America/Sao_Paulo')
   sao_paulo_time = sao_paulo_zone.localize(datetime(2024, 7, 2, 15, 0, 0))
   print("Hora em São Paulo:", sao_paulo_time)

   # Converter para fuso horário UTC
   utc_time = sao_paulo_time.astimezone(pytz.utc)
   print("Hora em UTC:", utc_time)

   # Converter para fuso horário Europa/Londres
   london_zone = pytz.timezone('Europe/London')
   london_time = sao_paulo_time.astimezone(london_zone)
   print("Hora em Londres:", london_time)
   ```

4. **Lista de todos os fusos horários disponíveis**:
   Você pode listar todos os fusos horários disponíveis na biblioteca `pytz` com o seguinte código:

   ```python
   import pytz

   for tz in pytz.all_timezones:
       print(tz)
   ```

Usando essas técnicas, você pode manipular datas e horários em diferentes fusos horários em Python de maneira eficaz.