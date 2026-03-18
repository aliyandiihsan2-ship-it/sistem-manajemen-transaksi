import pymongo
client = pymongo.MongoClient("mongodb+srv://aliyandiihsan2_db_user:ihsan2026@ihsanali.gq42sfo.mongodb.net/?appName=ihsanali")
db = client.get_database("fastapi-tutorial")

def get_db_connection():
    return db