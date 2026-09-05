# (revisão do 4º ciclo)

# Temas revisados: POO (classe, herança, override, __str__), geradores e decoradores, tudo junto

# Enunciado (mini inventory system)

# Crie day-028/main.py. Um mini sistema de inventário de produtos que junta os temas do ciclo.

# Um decorador log_action que imprima "Action: {nome da função}" antes de executar, aceite *args, **kwargs, e retorne o resultado. 
# Dica pra pegar o nome da função: func.__name__.
# Uma classe base Product com:
# __init__ recebendo name e price
# um método __str__ que retorne uma linha legível (exemplo: "name - $price")
# um método discount(self, percent) que retorne o preço com o desconto aplicado (não altera o preço guardado, só calcula e retorna)
# Uma classe PerishableProduct que herde de Product:
# __init__ com name, price e days_to_expire, usando super().__init__(...)
# sobrescreva o __str__ pra incluir a validade (override)
# Uma função geradora cheap_products(products, max_price) que receba uma lista de produtos e produza com yield só os que custam menos que max_price.
# Uma função decorada com @log_action que crie e retorne uma lista de produtos (mistura de Product e PerishableProduct).

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Action: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper
    
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
    
    def discount(self, percent):
        result_percent = self.price * (percent / 100)
        result = round(self.price - result_percent, 2)
        return result

class PerishableProduct(Product):
    def __init__(self, name, price, day_to_expire):
        super().__init__(name, price)
        self.day_to_expire = day_to_expire
    
    def __str__(self):
        return super().__str__() + f", expire: {self.day_to_expire}"

def cheap_products(products, max_price):
    for product in products:
        if product.price < max_price:
            yield product

@log_action
def create_list_products():
    return [
        Product("milk", 2.99),
        Product("tomato", 0.99),
        PerishableProduct("soda", 3.59, 7)
    ]

products_list = create_list_products()

for product in products_list:
    print(product)

for cheap in cheap_products(products_list, 3.00):
    print(cheap)

for product in products_list:
    print(product.discount(50))