# Crie day-015/review.py. O programa deve:

# Uma função save_grades(filename, grades) que receba um nome de arquivo e uma lista de notas (números), e escreva cada nota numa linha do arquivo. Use with e modo escrita. Não precisa retornar nada.
# Uma função read_grades(filename) que abra o arquivo, leia as linhas, e retorne uma lista com as notas convertidas de volta para número (cuidado: o que você lê de um arquivo vem como texto, então vai precisar converter). Use with e modo leitura.
# Uma função average(grades) que receba a lista de notas e retorne a média (soma dividida pela quantidade). Use return.
# No corpo principal: salve uma lista de notas num arquivo, leia de volta com a função de leitura, calcule a média das notas lidas, e imprima a lista e a média.

def save_grades(filename, grades):
    with open(filename, "w") as file:
        for grade in grades:
            file.write(f"{grade}\n")

def read_grades(filename):
    result = []
    
    with open(filename, "r") as file:
        for line in file:
            result.append(float(line.strip()))
    
    return result

def average(grades):
    average_grade = sum(grades) / len(grades)
    return round(average_grade, 2)

grade_list = [1.0, 2.5, 5.7, 6.0, 8.7, 6.9, 6.7, 10.0, 9.3]

save_grades("grades_list.txt", grade_list)
loaded = read_grades("grades_list.txt")

print(loaded)
print(average(loaded))
