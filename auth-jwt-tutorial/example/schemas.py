from pydantic import BaseModel

class RegisterSchema(BaseModel):
    name: str = "someoneidk"
    email: str = "someone@something.com"
    username: str = "someoneidk"
    password: str = "somethingidk"
    
class LogInSchema(BaseModel):
    username: str = "someoneidk"
    password: str = "somethingidk"