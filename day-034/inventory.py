# No inventory.py, crie uma classe Inventory:

# __init__ com um dicionário vazio de produtos (self.items = {})
# método add(name: str, quantity: int) -> None que adiciona um produto (levante ValueError se quantity for negativa)
# método remove(name: str) -> None que remove um produto (levante KeyError se não existir)
# método total(self) -> int que retorna a soma das quantidades

class Inventory:
    def __init__(self):
        self.items = {}
    
    def add(self, name: str, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.items[name] = quantity
    
    def remove(self, name: str) -> None:
        if name not in self.items:
            raise KeyError("Name not found")
        del self.items[name]
    
    def total(self) -> int:
        counter = 0
        for value in self.items.values():
            counter += value
        return counter