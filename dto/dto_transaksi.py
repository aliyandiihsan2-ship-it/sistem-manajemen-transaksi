from typing import Optional
from pydantic import BaseModel,Field
from enums.enum_tipe import Tipe
from enums.enum_method import Method 
from dto.dto_common import Basepage
from typing import List
from model.model import Transaction
class InputTransaction(BaseModel):
    tipe:Tipe
    amount:int
    notes:Optional[str]
    method:Method

class OutputTransaction(Basepage):
    data:List[Transaction]
    class Config:
        from_attributes = True