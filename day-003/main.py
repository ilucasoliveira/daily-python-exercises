# Enunciado do exercício (student record)

# Crie day-003/main.py. O programa deve, nesta ordem:

# Criar um dicionário representando um aluno, com pelo menos 3 chaves (exemplo: name, age, course)
# Imprimir o valor de uma chave específica (só o valor, não o dicionário inteiro)
# Atualizar o valor de uma chave existente
# Adicionar uma chave nova que não existia
# Percorrer o dicionário com um for e imprimir cada par no formato chave: valor
# Imprimir quantas chaves o dicionário tem no final (use len)

student = {
    "name":"Lucas",
    "age":23,
    "course":"Computer Science"
}

print(student["name"])

student["course"] = "Computer Science - 6th semester"

student["city"] = "Barbacena"

for key, value in student.items():
    print(f"{key}: {value}")

print(len(student))