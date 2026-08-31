# Crie day-023/main.py. O programa deve:

# Uma classe base (exemplo: Vehicle, Employee, Shape, tema livre) com __init__ 
# recebendo pelo menos 1 atributo e ao menos 1 método que use esse atributo
# Uma classe filha que herde da base (com a sintaxe class Filha(Base):)
# A filha deve ter seu próprio __init__ que use super().__init__(...) pra 
# aproveitar a mãe e adicionar pelo menos 1 atributo novo
# A filha deve ter pelo menos 1 método próprio, além dos herdados
# No corpo principal, criar um objeto da filha e chamar tanto um método herdado da 
# mãe quanto um método próprio da filha, mostrando que os dois funcionam
from datetime import datetime

class Employee:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
    
    def greeting(self):
        today = datetime.now().year
        age = today - self.birth_date.year
        return f"Hello, I am {self.name} and I am {age} years old."

class Manager(Employee):
    def __init__(self, name, birth_date, occupation):
        super().__init__(name, birth_date)
        self.occupation = occupation
    
    def valid_credentials(self):
        if self.occupation.upper() == "BOSS":
            return f"Authorized Credentials! You can pass Mister {self.name}."
        return f"Unauthorized Credentials! You cannot pass Mister {self.name}."

joseph = Manager("Joseph", datetime(1951, 7, 17), "Operator")
marcus = Manager("Marcus", datetime(2001, 3, 14), "Boss")

print(joseph.greeting())
print(joseph.valid_credentials())

print(marcus.greeting())
print(marcus.valid_credentials())