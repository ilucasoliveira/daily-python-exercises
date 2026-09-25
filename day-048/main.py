# Enunciado do exercício (jwt tokens)

# Crie a pasta day-048 com main.py. Instale: pip install pyjwt. O programa deve:

# Uma SECRET_KEY (pode ser uma string fixa no exercício; em produção viria do .env).
# Uma função create_token(username: str) -> str que gere um JWT com o sub (username) e um exp (expiração, ex: 30 minutos). Retorne o token.
# Uma função verify_token(token: str) -> dict que decodifique o token e retorne o payload. Trate os erros: token expirado 
# (jwt.ExpiredSignatureError) e token inválido (jwt.InvalidTokenError), retornando uma mensagem de erro em cada caso.
# No corpo principal, demonstre:
# crie um token pra um usuário e imprima (repara que é um texto longo com três partes separadas por ponto)
# verifique o token válido (deve retornar o payload com o username)
# verifique um token adulterado (muda um caractere do token na mão) e veja o erro de inválido
import os
import jwt

from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM","HS256")
EXPIRE_TOKEN = int(os.getenv("EXPIRE_TOKEN", 30))

def create_token(username: str) -> str:
    exp = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE_TOKEN)
    payload = {
        "sub": username,
        "exp": exp
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> dict:
    
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError as e:
        return {"error": str(e)}
    except jwt.InvalidTokenError as i:
        return {"error": str(i)}
    
    return decoded

print(create_token("ilucasoliveira"))
print(verify_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJpbHVjYXNvbGl2ZWlyYSIsImV4cCI6MTc5MDMzODkyOH0.bLZADhNJm9W31VG-U9t41XlTDyrJnTU5Fl_t1GcJaGA"))
print(verify_token("eyJzdWIiOiJpbHVjYXNvbGl2ZWlyYSIsImV4cCI6MTc5MDMzODkyOH0.bLZADhNJm9W31VG-U9t41XlTDyrJnTU5Fl_t1GcJaGA"))