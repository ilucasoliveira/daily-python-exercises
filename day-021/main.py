# DIA 21 (revisão do 3º ciclo)

# Temas revisados: arquivos, JSON, CSV, try/except, datetime e módulos, tudo num sistema só

# Sem conceito novo hoje. É integração. Você vai construir um mini sistema de registro de 
# despesas que usa quase tudo da semana junto. Ao longo do ciclo, o padrão que mais apareceu como 
# ponto de melhoria foi: filtrar/calcular sobre o dado carregado do arquivo (não sobre a lista original), 
# e retornar valor em vez de imprimir dentro da função. Este exercício cobra os dois.

# Enunciado (expense tracker)

# Crie a pasta com dois arquivos: day-021/expenses.py (o módulo com as funções) e day-021/main.py 
# (que importa e usa). Importe json, datetime e o que precisar.

# No main.py:

# importe as funções do módulo
# comece carregando as despesas do arquivo (que na primeira vez não existe, então volta lista vazia, testando o try/except)
# adicione pelo menos 3 despesas usando add_expense
# salve no arquivo
# carregue de volta do arquivo
# imprima o total gasto, calculado a partir do que foi carregado (não da lista original)

from expenses import add_expense, save_expenses, load_expenses, total_spent

file_name = "expenses.json"
loaded = load_expenses(file_name)

add_expense(loaded, "Hair Cream", 5.85)
add_expense(loaded, "Coca-cola", 3.25)
add_expense(loaded, "Meat", 25.80)

save_expenses(file_name, loaded)

final = load_expenses(file_name)
print(total_spent(final))

