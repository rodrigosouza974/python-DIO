A biblioteca `pytz` em Python é usada para manipular fusos horários. Ela fornece implementações corretas e completas para fusos horários, permitindo a conversão entre diferentes fusos horários e o tratamento adequado de horários de verão (Daylight Saving Time).

Aqui está um exemplo básico de como usar `pytz`:

1. **Instalação**:
   Primeiro, você precisa instalar a biblioteca `pytz` se ainda não a tiver instalada:

   ```sh
   pip install pytz
   ```

2. **Uso Básico**:
   Em seguida, você pode usá-la para converter datas e horas entre diferentes fusos horários. Aqui está um exemplo que demonstra como fazer isso:

   ```python
   from datetime import datetime
   import pytz

   # Obtém a hora atual no fuso horário UTC
   utc_now = datetime.now(pytz.utc)
   print("Hora atual em UTC:", utc_now)

   # Converte a hora atual para o fuso horário de Nova York
   ny_tz = pytz.timezone('America/New_York')
   ny_time = utc_now.astimezone(ny_tz)
   print("Hora atual em Nova York:", ny_time)

   # Converte a hora atual para o fuso horário de São Paulo
   sp_tz = pytz.timezone('America/Sao_Paulo')
   sp_time = utc_now.astimezone(sp_tz)
   print("Hora atual em São Paulo:", sp_time)
   ```

3. **Listar Todos os Fusos Horários**:
   Você pode listar todos os fusos horários disponíveis usando:

   ```python
   for tz in pytz.all_timezones:
       print(tz)
   ```

4. **Trabalhando com Horários Localizados**:
   Ao criar um objeto `datetime`, você pode associá-lo a um fuso horário específico usando `pytz`. Isso é chamado de "localização" do objeto `datetime`.

   ```python
   # Cria um objeto datetime não localizado
   naive_dt = datetime(2024, 7, 2, 12, 0, 0)
   print("Datetime não localizado:", naive_dt)

   # Localiza o datetime no fuso horário de Nova York
   localized_dt = ny_tz.localize(naive_dt)
   print("Datetime localizado em Nova York:", localized_dt)
   ```

5. **Tratamento de Horário de Verão**:
   A biblioteca `pytz` trata automaticamente os horários de verão ao converter entre fusos horários.

   ```python
   # Hora em Nova York no horário de verão
   dt_summer = datetime(2024, 6, 15, 12, 0, 0)
   ny_summer_time = ny_tz.localize(dt_summer)
   print("Hora de verão em Nova York:", ny_summer_time)

   # Hora em Nova York no horário padrão
   dt_winter = datetime(2024, 12, 15, 12, 0, 0)
   ny_winter_time = ny_tz.localize(dt_winter)
   print("Hora padrão em Nova York:", ny_winter_time)
   ```

Esses exemplos devem te ajudar a começar a usar `pytz` para manipular datas e horas em diferentes fusos horários em Python.