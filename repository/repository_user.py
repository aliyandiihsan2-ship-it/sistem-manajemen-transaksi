from fastapi import Depends 
from typing import Any
from model.model_user import User
from pydantic import TypeAdapter
from config.config import get_db_connection   
from dto.dto_user import Inputlogin    
class RepositoryUser():
    def __init__(self,db:Any=Depends(get_db_connection)):
        self.repository = db.get_collection("user")
    def insert_new_user(self,new_user:User):
        user_data = new_user.model_dump(mode='json', exclude_none=True)
        result = self.repository.insert_one(new_user.model_dump(exclude_none=True))
        user_data["id"] = str(result.inserted_id)
        return user_data

    def find_user_by_username(self,username:str):
        result = self.repository.find_one({"username":username})
        if result is not None:
            return TypeAdapter(User).validate_python(result)
        return None

    def find_user_by_username_password(self,input_login:Inputlogin):
        result= self.repository.find_one({"username":input_login.username,"password":input_login.password})
        if result is not None:
            return TypeAdapter(User).validate_python(result)
        return None