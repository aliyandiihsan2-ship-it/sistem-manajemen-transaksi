from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
from fastapi import Depends
from dto.dto_common import TokenData
from service.service_jwt import ServiceJwT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/user/login") 
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],service_jwt:ServiceJwT=Depends()):
    return TokenData.model_validate(service_jwt.decode_token(token))