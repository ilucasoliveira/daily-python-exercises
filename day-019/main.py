# Enunciado do exercício (date toolkit)

# Crie day-019/main.py. Importe o que precisar de datetime. O programa deve:

# Pegar e imprimir a data e hora atual
# Imprimir só o ano, só o mês e só o dia atuais, separadamente
# Formatar e imprimir a data atual em pelo menos dois formatos diferentes usando strftime (exemplo: "27/08/2026" e "August 27, 2026" com %B pro nome do mês)
# Criar uma data específica (exemplo: uma data de nascimento) e calcular quantos dias se passaram desde ela até hoje
# Imprimir esse número de dias

from datetime import datetime

today = datetime.now()
year = today.year
month = today.month
day = today.day
day_first = today.strftime("%d/%m/%Y")
text_day = today.strftime("%B %d, %Y")

my_birthday = datetime(2003, 6, 17)
diff = today - my_birthday

print(today)
print(year)
print(month)
print(day)
print(day_first)
print(text_day)
print(diff.days)