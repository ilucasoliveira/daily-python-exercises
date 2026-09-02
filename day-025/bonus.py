# Crie day-025/bonus.py. O programa deve:

# Uma classe Book com __init__ recebendo title, author e year
# Um método __str__ que retorne uma descrição legível do livro (exemplo: "1984 by George Orwell (1949)")
# No corpo principal, crie pelo menos 2 livros e dê print direto em cada objeto (sem chamar nenhum método, só print(livro))
# Bônus opcional: crie uma lista com os livros e percorra com um for imprimindo cada um, pra ver o __str__ agindo em cada objeto

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

book1 = Book("Hunger Games", "Suzanne Collins", 2008)
book2 = Book("O Hobbit", "J.R.R Tolkien", 1959)

print(book1)
print(book2)