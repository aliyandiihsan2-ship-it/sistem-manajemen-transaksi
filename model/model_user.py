from pydantic import BaseModel, Field
from model.model_common import PyObjectId
class User(BaseModel):
    id: PyObjectId = Field(alias="_id")
    username:str
    password:str
    name:str