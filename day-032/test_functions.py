from functions import sum_numbers, is_even_number, upside_down

def test_sum_numbers():
    assert sum_numbers(12, 13) == 25
    assert sum_numbers(1950, 50) == 2000
    assert sum_numbers(0, 0) == 0
    assert sum_numbers(-5, 5) == 0

def test_is_even_number():
    assert is_even_number(4) == "it is even"
    assert is_even_number(5) == "it is not even"
    assert is_even_number(0) == "it is even"

def test_upside_down():
    assert upside_down("python") == "nohtyp"
    assert upside_down("nohtyp") == "python"
    assert upside_down("a") == "a"
    assert upside_down("") == ""