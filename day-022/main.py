# Enunciado do exercício (first class)

# Crie day-022/main.py. O programa deve:

# Criar uma classe (tema livre: Person, Car, Book, o que preferir) com um __init__ que receba pelo menos 2 atributos
# A classe deve ter pelo menos 2 métodos além do __init__, e cada método deve usar self pra acessar os atributos e retornar algo com return
# No corpo principal, criar pelo menos 2 objetos diferentes a partir da classe
# Chamar os métodos de cada objeto e imprimir os resultados, mostrando que cada objeto tem seus próprios dados

class Person:
    def __init__(self, name, age, birthday_date):
        self.name = name
        self.age = age
        self.birthday_date = birthday_date
        
    def show_name(self):
        return f"Hello, I am {self.name}."
    
    def show_age(self):
        return f"and I am {self.age} year old. I was born in {self.birthday_date}."

geraldo = Person("Geraldo", 75, "30/05/1951")
silvana = Person("Silvana", 54, "06/11/1971")

print(geraldo.show_name())
print(silvana.show_name())

print(geraldo.show_age())
print(silvana.show_age())