import datetime

# Obter a data e hora atuais
agora = datetime.datetime.now()

# Imprimir a data e hora atuais
print("Data e hora atuais:", agora)

# Formatar a data e a hora
formatado_agora = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data e hora formatadas:", formatado_agora)
```

Isso exibirá a data e a hora atuais, bem como uma versão formatada. O formato `"%d/%m/%Y %H:%M:%S"` exibirá a data e a hora no formato `DD/MM/AAAA HH:MM:SS`, que é mais comum em português.