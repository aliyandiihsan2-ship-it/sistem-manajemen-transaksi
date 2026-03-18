from fastapi import APIRouter,Depends,HTTPException
from dto.dto_user import InputUser
from service.service_user import ServiceUser
from dto.dto_user import Inputlogin
from dto.dto_common import StandardResponse
from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from dto.dto_user import OutputLogin
router_user = APIRouter(prefix="/api/v1",tags=["user"])

@router_user.post("/user")
def insert_new_user(input_user:InputUser,service_user:ServiceUser=Depends()):
    service_user.insert_new_user(input_user)
    return StandardResponse(detail="berhasil registrasi")
    
@router_user.post("/user/login")
def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],service_user:ServiceUser=Depends()):
    jwt_token = service_user.login_user(Inputlogin(username=form_data.username,password=form_data.password)) 
    return OutputLogin(access_token=jwt_token)