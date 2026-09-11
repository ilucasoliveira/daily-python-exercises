# No test_inventory.py:

# Uma fixture que use yield: antes do yield, cria um Inventory com alguns itens já adicionados; 
# depois do yield, imprime "cleanup done" (o teardown). Retorne (via yield) o inventory pronto.
# Um teste que adiciona um item e verifica o total.
# Um teste que remove um item e verifica o total.
# Um teste com pytest.raises pra remover um item que não existe (KeyError).
# Um teste parametrizado pra adicionar várias quantidades e verificar.

import pytest
from inventory import Inventory

@pytest.fixture
def dict_inv():
    inv = Inventory()
    inv.add("pencils", 45)
    inv.add("pens", 15)
    inv.add("glue", 5)
    inv.add("eraser", 10)
    yield inv
    print("cleanup done")

def test_add(dict_inv):
    dict_inv.add("notebook", 10)
    assert dict_inv.total() == 85

def test_remove(dict_inv):
    dict_inv.remove("glue")
    assert dict_inv.total() == 70

def test_add_error(dict_inv):
    with pytest.raises(ValueError):
        dict_inv.add("post-it", -10)

def test_remove_error(dict_inv):
    with pytest.raises(KeyError):
        dict_inv.remove("blackbord")

@pytest.mark.parametrize("name, quantity", [
    ("stapler", 3),
    ("marker", 8),
    ("ruler", 12),
])
def test_add_various(dict_inv, name, quantity):
    dict_inv.add(name, quantity)
    assert dict_inv.items[name] == quantity