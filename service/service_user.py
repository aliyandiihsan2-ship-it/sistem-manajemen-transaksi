from fastapi import Depends
from repository.repository_user import RepositoryUser
from dto.dto_user import InputUser
from typing import Optional
from model.model_user import User
from dto.dto_user import Inputlogin
from fastapi import HTTPException
from service.service_security import SecurityService
from service.service_jwt import ServiceJwT
from dto.dto_common import TokenData
class ServiceUser:
    def __init__(self,repository_user:RepositoryUser=Depends(),security_service:SecurityService=Depends(),service_jwt:ServiceJwT=Depends()):
        self.repository_user = repository_user
        self.security_service = security_service    
        self.service_jwt = service_jwt

    def insert_new_user(self,input_user:InputUser):
         found_duplicate_usernmae = self.repository_user.find_user_by_username(input_user.username)
         if found_duplicate_usernmae is not None:
             raise HTTPException(status_code=400, detail="username already exists")
         input_user.password = self.security_service.get_password_hash(input_user.password)
         return self.repository_user.insert_new_user(input_user)

    def login_user(self,input_login:Inputlogin):
        found_user = self.repository_user.find_user_by_username(input_login.username)
        if found_user is None:
            raise HTTPException(status_code=404, detail="user not found")
        if not self.security_service.verify_password(input_login.password, found_user.password):
            raise HTTPException(status_code=401, detail="invalid password") 

        jwt_token = self.service_jwt.create_access_token(TokenData(userId=str(found_user.id),name=found_user.name).dict())
        return jwt_token