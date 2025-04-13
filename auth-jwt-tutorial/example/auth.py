import jwt
from fastapi import HTTPException
from datetime import datetime, timedelta

JWT_SECRET = 'jwtsecret'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def generate(username: str):
    expiration = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "username": username,
        "exp": expiration
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm = ALGORITHM)
    return token
    
def verify(token):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms = [ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    