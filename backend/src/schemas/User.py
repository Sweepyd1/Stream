from pydantic import BaseModel, EmailStr


class UserLogin(BaseModel):
    email:EmailStr
    password:str
    
    
    
class UserRegister(BaseModel):
    email:EmailStr
    password:str
    username:str 
    
    