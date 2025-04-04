from fastapi import APIRouter
from fastapi import Request
from schemas.User import UserLogin, UserRegister

users = APIRouter(prefix="/api/users",tags=["Пользователи"])


@users.post("/auth/login")
async def login(request:Request, user:UserLogin):
    print(user.email)
     

@users.post("/auth/register")
async def register(request:Request, newUser:UserRegister):
    print(request.client.host)
    print(newUser)

@users.delete("/auth/logout")
async def logout():
    pass 


@users.post("/auth/google_login")
async def google_login():
    pass 


@users.post("/auth/google_register")
async def google_register():
    pass 


@users.get("/get_my_profile_info")
async def google_register():
    pass 
