from fastapi import Depends
from typing import Any
from model.model import Transaction
from pydantic import TypeAdapter
from config.config import get_db_connection      
from typing import List
 
class RepositoryTransaksi():
    def __init__(self,db:Any=Depends(get_db_connection)):
        self.repository = db.get_collection("transaction")

    def insert_new_transaction(self,new_transaction:Transaction):
        transaction_data = new_transaction.model_dump(mode='json', exclude_none=True)
        result = self.repository.insert_one(new_transaction.model_dump(exclude_none=True))
        transaction_data["id"] = str(result.inserted_id)
        return transaction_data

    def get_list_transaction (self,match_filter:dict,skip:int,size:int):
        result= self.repository.find(match_filter).skip(skip).limit(size)
        result = list(result)
        return TypeAdapter(list[Transaction]).validate_python(result)

    def count_transaction (self,match_filter:dict):
        return self.repository.count_documents(match_filter)

    def export_transaction(self,match_filter:dict,projection_stage:dict):
        result= self.repository.find(match_filter,projection_stage)
        result = list(result)
        return result
    
    # #kalo mau masukin data banyak banget pake ini
    # def insert_new_transaction(self, new_transactions: List[Transaction]):
    #     # 1. Ubah setiap objek Transaction dalam list menjadi dictionary
    #     items = [item.model_dump(exclude_none=True, exclude={"id"}) for item in new_transactions]
        
    #     # 2. Gunakan insert_many karena data yang dikirim adalah list
    #     result = self.repository.insert_many(items)
        
    #     # 3. Masukkan ID yang baru dibuat ke masing-masing data
    #     for i, inserted_id in enumerate(result.inserted_ids):
    #         new_transactions[i].id = str(inserted_id)
            
    #     # 4. Kembalikan semua data dalam bentuk list
    #     return [item.model_dump(mode='json', exclude_none=True) for item in new_transactions]
    # def get_list_transaction (self,match_filter:dict,skip:int,size:int):
    #     result= self.repository.find(match_filter).skip(skip).limit(size)
    #     result = list(result)
    #     return TypeAdapter(list[Transaction]).validate_python(result)