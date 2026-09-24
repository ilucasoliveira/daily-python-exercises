# Enunciado do exercício (password hashing)

# Crie a pasta day-047 com main.py. Instale: pip install "passlib[bcrypt]". O programa deve:

# Configurar o CryptContext com bcrypt.
# Uma função hash_password(password: str) -> str que receba uma senha e retorne o hash.
# Uma função verify_password(plain: str, hashed: str) -> bool que receba a senha em texto e o hash, e retorne se batem.
# No corpo principal, demonstre:
# crie o hash de uma senha e imprima (repara que é irreversível e diferente do original)
# verifique a senha CORRETA contra o hash (deve dar True)
# verifique uma senha ERRADA contra o hash (deve dar False)
# gere o hash da MESMA senha duas vezes e mostre que os hashes são diferentes (por causa do salt), mas ambos verificam True
import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())

hash1 = hash_password("Lucas123456@")
hash2 = hash_password("Lucas123456@")

print(hash1)
print(hash2)

print("are they equal?", hash1 == hash2)
print("does hash1 verify?", verify_password("Lucas123456@", hash1))
print("does hash2 verify?", verify_password("Lucas123456@", hash2))  

