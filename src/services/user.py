from src.datalayer.models.user import UserModel
from src.api.exceptions.user import (
    register_already_exception, 
    login_wrong_exception
    )

class UserService:

    def __init__(self):
        pass
    
    async def register(self, name: str, email: str, password: str):
        
        email_exists = await UserModel.filter(email=email).first()
        if email_exists:
            raise register_already_exception()
            
        user = await UserModel.create(
            name = name,
            email = email,
            password = password
        )
        
        return user
    
    async def login(self, email: str, password: str):
        
        user = None
        try:
            user = await UserModel.get(email=email)
        except Exception as e:
            raise login_wrong_exception()
        
        if user.password != password:
            raise login_wrong_exception()
    
        return user
    
    async def get_all_users(self):
        return await UserModel.all()