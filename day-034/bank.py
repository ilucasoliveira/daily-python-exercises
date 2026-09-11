# Enunciado do exercício (fixtures and class tests)

# Crie a pasta day-034 com dois arquivos:

# Um bank.py com uma classe BankAccount:
# __init__ recebendo owner (str) e balance (float, começa em 0 se não passar)
# método deposit(amount) que soma ao balance (levante ValueError se amount for negativo ou zero)
# método withdraw(amount) que subtrai do balance (levante ValueError se amount for maior que o saldo)
# método __str__ pra representação legível

class BankAccount:
    def __init__(self, owner: str, balance: float = 0) -> None:
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount: float) -> float:
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance = self.balance - amount
        return self.balance
    
    def __str__(self) -> str:
        return f"{self.owner}: ${self.balance:.2f}"