from fastapi import APIRouter,Depends
from dto.dto_transaksi import InputTransaction
from service.service_transaction import ServiceTransaction
from enums.enum_tipe import Tipe
from typing import Optional
from dto.dto_common import TokenData
from service.service_common import oauth2_scheme, get_current_user
from typing_extensions import Annotated
from typing import List
from fastapi.responses import StreamingResponse
from datetime import datetime
from model.model_common import InputDatetime

router_transaction=APIRouter(prefix="/api/v1",tags=["transaction"])

@router_transaction.post("/transaction")
def insert_new_transaction(
    input_transaction:InputTransaction,
    current_user: Annotated[TokenData, Depends(get_current_user)],
    service_transaction:ServiceTransaction=Depends()):
    return service_transaction.insert_new_transaction(input_transaction,current_user)

@router_transaction.get("/transaction")
def get_list_transaction(
    current_user: Annotated[TokenData, Depends(get_current_user)],
    tipe:Optional[Tipe]=None,
    page:int=1,
    size:int=10,
    service_transaction:ServiceTransaction=Depends()):
    return service_transaction.get_list_transaction(current_user,tipe,page,size)   

@router_transaction.post("/export")
def export_history_transaction(
    current_user: Annotated[TokenData, Depends(get_current_user)],
    start_date:Optional[InputDatetime]=None,
    end_date: Optional[InputDatetime]=None,
    tipe:Optional[Tipe]=None,
    service_transaction:ServiceTransaction=Depends()):
    content_file = service_transaction.export_history_transaction(
        tipe,
        start_date,
        end_date,
        current_user
        )
    
    headers = {
        "Content-Disposition": 'attachment; filename="export.csv"'
    }
    return StreamingResponse(
        iter([content_file]), 
        media_type="text/csv", 
        headers=headers
    )

    
