from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError
from dto.dto_common import TokenData
from fastapi import HTTPException
class ServiceJwT:
    def __init__(self):
        self.SECRET_KEY = "edea0d93d4e1fc55734bb64d86924c38a291b11107a3afc10f76e5f382af68df"
        self.ALGORITHM = "HS256"
        self.access_token_expire_minutes = 30
    def create_access_token(self,data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt
    def decode_token(self,token:str):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            return payload
        except InvalidTokenError:
            raise HTTPException(401, "invalid credential")
