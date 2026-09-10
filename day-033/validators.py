# No validators.py, crie:

# Uma função validate_age(age: int) -> int que:
# levante ValueError se a idade for negativa (com raise)
# levante ValueError se a idade for maior que 120 (impossível)
# retorne a própria idade se for válida (entre 0 e 120)
# Uma função classify_age(age: int) -> str que retorne uma categoria: "child" se menor que 13, "teen" se de 13 a 17, "adult" se 18 ou mais. (assuma que a idade já é válida)

def validate_age(age: int) -> int:
    if age < 0 or age > 120:
        raise ValueError("Age cannot be negative or greater than 120.")
    return age

def classify_age(age: int) -> str:
    verify_age = validate_age(age)
    if verify_age < 13:
        return "child"
    if verify_age >= 13 and verify_age <= 17:
        return "teen"
    if verify_age >= 18:
        return "adult"
