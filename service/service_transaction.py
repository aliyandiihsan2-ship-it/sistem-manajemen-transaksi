from fastapi import Depends
from repository.repository_transaksi import RepositoryTransaksi
from dto.dto_transaksi import InputTransaction
from enums.enum_tipe import Tipe
from typing import Optional
from model.model import Transaction
from dto.dto_common import TokenData
from dto.dto_transaksi import OutputTransaction
import math
from datetime import datetime,timedelta
import pandas as pd
from fastapi import HTTPException

class ServiceTransaction:
    def __init__(self,
    repository_transaction:RepositoryTransaksi=Depends()):
        self.repository_transaction = repository_transaction

    def insert_new_transaction(self,
    input_transaction:InputTransaction, 
    current_user: TokenData):
        new_transaction = Transaction(
            tipe=input_transaction.tipe,
            amount=input_transaction.amount,
            notes=input_transaction.notes,
            method=input_transaction.method,
            userId=current_user.userId
        )
        return self.repository_transaction.insert_new_transaction(new_transaction)

    def get_list_transaction(self,
    current_user:TokenData,
    tipe:Optional[Tipe]=None,
    page:int=1,size:int=10):
        match_filter={"userId":current_user.userId}
        if tipe is not None:
            match_filter ["tipe"]=tipe
        skip = (page-1)*size
        total_data = self.repository_transaction.count_transaction(match_filter)
        list_transaction = self.repository_transaction.get_list_transaction(match_filter,skip,size)
        total_page = math.ceil(total_data/size)
        return OutputTransaction(
            data=list_transaction,
            page=page,size=size,
            total_data=total_data,
            total_page=total_page)

    def export_history_transaction(self,
    tipe:Optional[Tipe],
    start_date:Optional[str],
    end_date:Optional[str],
    current_user:TokenData):
        match_filter = {"userId": current_user.userId}
        if tipe is not None:
            match_filter["tipe"] = tipe
        if start_date is not None and end_date is not None:
            match_filter["created_time"] = {
                "$gte": start_date,
                "$lte": end_date +timedelta(days=1)
            }
        projection_stage = Transaction.project_export()
        result = self.repository_transaction.export_transaction(match_filter, projection_stage)
        
        if len (result)==0:
            raise HTTPException(status_code=400, detail="tidak ada data")
        df = pd.DataFrame(result)  
        df = df.fillna("")
        
        return df.to_csv(index=False, sep=";")
        