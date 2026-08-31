# Crie day-023/review.py. O programa deve:

# Uma classe base Shape com:
# __init__ recebendo name e guardando como atributo
# um método area(self) que retorne 0 (a base não sabe calcular, é genérica)
# um método describe(self) que retorne algo como "Shape {name} has area {area}", chamando self.area() por dentro
# Uma classe Rectangle que herde de Shape:
# __init__ com width e height, usando super().__init__("Rectangle") pra passar o nome pra mãe
# sobrescreva o método area(self) pra retornar width vezes height (a fórmula do retângulo)
# Uma classe Circle que herde de Shape:
# __init__ com radius, usando super().__init__("Circle")
# sobrescreva o area(self) pra retornar 3.14 vezes radius ao quadrado
# No corpo principal, crie um Rectangle e um Circle, e chame o describe() de cada um. Repara: 
# o describe está definido só na mãe, mas quando ele chama self.area(), cada objeto usa a SUA própria versão de area.

class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        return 0
    
    def describe(self):
        return f"Shape {self.name} has area {self.area()}."

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

rectangle = Rectangle(10, 13)
print(rectangle.describe())

circle = Circle(10)
print(circle.describe())