# Enunciado (event age calculator)

# Crie day-019/review.py. Importe o que precisar de datetime. O programa deve:

# Uma função days_since(past_date) que receba uma data e retorne quantos dias se passaram dela até hoje. Use return.
# Uma função format_date(some_date, pattern) que receba uma data e um padrão de formatação (string tipo "%d/%m/%Y")
# e retorne a data formatada como texto com strftime. Use return.
# Uma função is_past(some_date) que receba uma data e retorne True se ela já passou (é anterior a hoje) ou False se
# é futura. Dica: você pode comparar duas datas direto com < ou >, igual compara números.
# No corpo principal:
# crie pelo menos duas datas: uma no passado e uma no futuro
# use days_since na data passada e imprima
# use format_date nas duas datas, em pelo menos dois padrões diferentes
# use is_past nas duas datas e imprima o resultado (deve dar True pra passada, False pra futura)

from datetime import datetime

def days_since(past_date):
    today = datetime.now()
    diff = today - past_date
    return diff.days

def format_date(some_date, pattern):
    date = some_date.date()
    result = date.strftime(pattern)
    return result

def is_past(some_date):
    date = some_date
    today = datetime.now()
    return date < today

past_date = datetime(1971, 11, 6)
future_date = datetime(2027, 1, 1)

print(days_since(past_date))
print(format_date(past_date, "%d/%m/%Y"))
print(format_date(future_date, "%B %d, %Y"))
print(is_past(past_date))
print(is_past(future_date))
