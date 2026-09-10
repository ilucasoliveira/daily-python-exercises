# No test_validators.py, crie:

# Um teste parametrizado pro validate_age com casos VÁLIDOS: passa várias idades boas (0, 25, 120) e verifica que a função retorna a mesma idade.
# Um teste parametrizado usando pytest.raises pros casos INVÁLIDOS: passa idades ruins (-1, -50, 121, 200) e verifica que 
# cada uma levanta ValueError. Dica: dá pra combinar parametrize com o pytest.raises, passando só as entradas inválidas e checando que todas levantam o erro.
# Um teste parametrizado pro classify_age cobrindo as três categorias e os limites (12 vira child, 13 vira teen, 17 vira 
# teen, 18 vira adult). Os limites são o mais importante aqui.
import pytest

from validators import validate_age, classify_age

@pytest.mark.parametrize("bad_age", [-1, -50, 121, 300])
def test_validate_age_invalid(bad_age):
    with pytest.raises(ValueError):
        validate_age(bad_age)

@pytest.mark.parametrize("age, classify", [
    (12, "child"),
    (13, "teen"),
    (17, "teen"),
    (18, "adult"),
    (20, "adult"),
])
def test_classify_age(age, classify):
    assert classify_age(age) == classify