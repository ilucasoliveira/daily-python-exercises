import pytest

from functions import divide, get_age, is_even

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_get_age_future():
    with pytest.raises(ValueError):
        get_age(2031)

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (4, True),
    (0, True),
])
def test_is_even(number, expected):
    assert is_even(number) == expected