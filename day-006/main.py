# Enunciado do exercício (dockerized script)

# Crie a pasta day-006 com dois arquivos dentro:

# Um main.py que imprima pelo menos 2 linhas (exemplo: uma saudação e a data atual, ou qualquer coisa sua)
# Um Dockerfile que use uma imagem base de Python, defina a pasta de trabalho, copie o script e rode ele no start

from datetime import datetime

current_time = datetime.now().strftime("%d/%m/%Y")

print("Welcome to my WORLD !!!")
print(current_time)