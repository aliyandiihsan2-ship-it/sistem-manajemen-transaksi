from typing import Optional
from datetime import datetime
from pydantic import BaseModel,Field
from enums.enum_tipe import Tipe
from enums.enum_method import Method    
from bson import ObjectId
from model.model_common import PyObjectId

class Transaction(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    created_time:datetime=Field(default_factory=datetime.now)
    tipe:Tipe
    amount:int
    notes:Optional[str]
    method:Method
    userId: str

    @classmethod
    def project_export(cls):
        return {
            "_id": 0,
            "Tanggal": "$created_time",
            "Tipe": "$tipe",
            "Jumlah": "$amount",
            "Catatan": "$notes",
            "Metode": "$method"
        }
