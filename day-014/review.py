# Enunciado do exercício (student report generator)

# Crie day-014/review.py. Monte um mini gerador de relatório de alunos, combinando os temas:

# Uma função collect_grades(*grades) que receba qualquer quantidade de notas (números) e retorne uma lista com elas (retorne a lista, não a soma, lembra do day-010)
# Uma função build_students(**students) que receba pares nomeados no formato nome=nota_média e retorne o dicionário desses pares
# A partir de um dicionário de alunos (nome: média), use uma dict comprehension para criar um novo dicionário só com os aprovados, os que têm média maior ou igual a 6 (filtro exato, só a condição pedida, lembra do day-009)
# A partir da mesma fonte, use uma list comprehension para criar uma lista só com os nomes dos alunos (as chaves), todos em maiúsculas
# No corpo principal, chame as funções e imprima cada resultado com rótulo claro, sempre imprimindo fora das funções

def collect_grades(*grades):
    return list(grades)

def build_students(**students):
    return students

students = build_students(Lucas=8.5, Marco=7.0, Rosalia=5.9, Silvana=6.0)
approved = {key:values for key, values in students.items() if values >= 6.0}

list_aproved = [student.lower() for student in approved]

print(collect_grades(5.0, 6.9, 7.0, 4.8, 0.5, 4.0))
print(students)
print(approved)
print(list_aproved)