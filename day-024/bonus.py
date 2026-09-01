# Enunciado (abstract payment):

# Crie day-024/bonus.py. O programa deve:

# Uma classe abstrata Payment (herdando de ABC) com um método abstrato pay(self, amount) marcado com @abstractmethod, corpo pass
# Duas filhas concretas: CreditCard e Pix, cada uma herdando de Payment e implementando o próprio pay, 
# retornando uma mensagem diferente (exemplo: "Paid {amount} with credit card" e "Paid {amount} via Pix")
# No corpo principal, crie um objeto de cada filha e chame o pay de cada um
# Tente criar um objeto direto da Payment (a abstrata) e veja o erro que aparece, isso prova que a classe abstrata não pode ser instanciada

from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        return f"{self.name} paid {amount} with credit card"

class Pix(Payment):
    def pay(self, amount):
        return f"{self.name} paid {amount} via PIX"

eliza = CreditCard("Eliza")
print(eliza.pay(302))

jessica = Pix("Jessica")
print(jessica.pay(1099))

try:
    x_error = Payment("Error")
except TypeError as e:
    print(f"Cannot create abstract Payment: {e}")