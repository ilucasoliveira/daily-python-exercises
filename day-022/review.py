# Crie day-022/review.py. Importe o que precisar de datetime. O programa deve:

# Criar uma classe Person com __init__ recebendo name e birth_date, onde birth_date é 
# um objeto datetime (não texto). Guarde os dois como atributos. Repara: não guarde a idade, só a data de nascimento.
# Um método current_age(self) que calcule a idade atual a partir da data de nascimento, 
# usando datetime. Retorne o número de anos. Dica pra calcular anos: pega a diferença de 
# dias entre hoje e o nascimento e divide por 365 (aproximação simples serve pro exercício), 
# ou use a lógica de comparar anos. Use return.
# Um método years_until(self, target_year) que receba um ano futuro e retorne quantos anos faltam da 
# idade atual até lá. Exemplo: se a pessoa vai fazer aniversário e você quer saber quantos anos ela terá em determinado ano. 
# Simplifica: retorne target_year - ano_de_nascimento. Use return.
# Um método greeting(self) que retorne uma saudação usando o nome e a idade calculada (chamando o próprio current_age de 
# dentro dele, com self.current_age()). Use return.
# No corpo principal, crie pelo menos 2 pessoas com datas de nascimento diferentes e chame os métodos, imprimindo os resultados.

from datetime import datetime

class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
    
    def current_age(self):
        today = datetime.now()
        age = today.year - self.birth_date.year
        return age
    
    def years_until(self, target_year):
        result = target_year - self.birth_date.year
        return result
    
    def greeting(self):
        age = self.current_age()
        return f"Hello, I am {self.name} and I am {age} years old!"

isabella = Person("Isabella", datetime(2001, 1, 22))
lucas = Person("Lucas", datetime(2003, 6, 17))

print(lucas.current_age())

print(isabella.years_until(2051))

print(lucas.greeting())
print(isabella.greeting())