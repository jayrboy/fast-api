from fastapi import FastAPI, Depends, HTTPException

from auth import generate, verify
from schemas import RegisterSchema, LogInSchema

app = FastAPI()

users = []

@app.post("/")
def root(decoded: str = Depends(verify)):
    return {"message": "Authenticated", "username": decoded.username}

@app.post('/register', tags=['auth'])
async def register(request: RegisterSchema):
    for user in users:
        if user.username == request.username:
            raise HTTPException(status_code=400, detail="User already registered")
    users.append(request)
    token = generate(request.username)
    
    for user in users:
        print(user.name, user.username, user.password)
        
    return token

@app.post('/login', tags=['auth'])
def login(request: LogInSchema):
    for user in users:
        if user.username == request.username and user.password == request.password:
            token = generate(user.username)
            
            return token
        else:
            raise HTTPException(status_code=400, detail="Invalid credentials")
    raise HTTPException(status_code=401, detail="Username not registered")