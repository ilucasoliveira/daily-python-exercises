# Um test_bank.py com:
# uma @pytest.fixture que retorne uma BankAccount pronta (exemplo: owner "Lucas", balance 100)
# um teste que use a fixture pra testar um depósito válido
# um teste que use a fixture pra testar um saque válido
# um teste com pytest.raises pra verificar que sacar mais que o saldo levanta ValueError
# um teste com pytest.raises pra depósito inválido (valor negativo)

import pytest
from bank import BankAccount

@pytest.fixture
def account():
    return BankAccount("Lucas", 1000)

def test_deposit(account):
    account.deposit(100)
    assert account.balance == 1100

def test_withdraw(account):
    account.withdraw(50)
    assert account.balance == 950

def test_deposit_error(account):
    with pytest.raises(ValueError):
        account.deposit(-150)

def test_withdraw_error(account):
    with pytest.raises(ValueError):
        account.withdraw(1500)