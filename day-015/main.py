# Enunciado do exercício (file notes manager)

# Crie day-015/main.py. O programa deve, nesta ordem:

# Abrir um arquivo em modo escrita e gravar pelo menos 3 linhas nele (exemplo: uma lista de tarefas)
# Abrir o mesmo arquivo em modo leitura e imprimir todo o conteúdo
# Abrir o arquivo em modo append e adicionar mais 1 linha no fim
# Abrir de novo em leitura e imprimir o conteúdo final, mostrando a linha nova incluída
# Usar with em todas as aberturas

with open("note.txt", "w") as file:
    file.write("Task's List\n")
    file.write("1. Take the children to the dentist.\n")
    file.write("2. Go to walk with tobby at afternoon.\n")

with open("note.txt", "r") as file:
    content = file.read()
    print(content)

with open("note.txt", "a") as file:
    file.write("3. Go to the market to buy clean products and some meat to the dinner tonight.\n")

with open("note.txt", "r") as file:
    content = file.read()
    print(content)