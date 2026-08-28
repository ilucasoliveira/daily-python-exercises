# Enunciado (date validator module)

# Crie day-020/review.py (o módulo com as funções) e day-020/review_main.py (que importa e usa). Importe o que precisar de datetime.

# No review.py, crie três funções:

# parse_date(text): recebe um texto de data no formato "dd/mm/aaaa" (tipo "15/06/2003") e tenta converter
# pra objeto datetime usando datetime.strptime(text, "%d/%m/%Y"). Protege com try/except: se o texto estiver 
# num formato inválido, captura ValueError e retorna None. Use return.
# days_between(date1, date2): recebe duas datas e retorna a quantidade de dias entre elas (em valor absoluto, 
# use abs() pra nunca dar negativo). Use return.
# is_valid_date(text): recebe um texto e retorna True se for uma data válida no formato esperado, False se não. 
# Dica: pode reaproveitar a parse_date aqui dentro, se ela retornar None é porque não é válida.
from datetime import datetime
from review import parse_date, days_between, is_valid_date

text_date = "17/06/2003"
text_wrong = "17.06.2003"

date1 = datetime.now().date()
date2 = datetime(1951, 5, 30).date()

print(parse_date(text_date))
print(parse_date(text_wrong))
print(days_between(date1, date2))
print(is_valid_date(text_date))
print(is_valid_date(text_wrong))
