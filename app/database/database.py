from bson import ObjectId
from datetime import datetime, timedelta
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import ConnectionFailure
from pymongo.results import InsertOneResult
from pydantic import BaseModel, Field
from pymongo import MongoClient
from bson.objectid import ObjectId
from .models import NewTable

client = MongoClient("mongodb+srv://pcalvanelli:<password>@cluster0.uzhg1.mongodb.net/?retryWrites=true&w=majority")
db = client["Cluster0"]
users_collection = db['users']
tokens_collection = db['tokens']

class NewTableDB:
    def __init__(self, db_uri: str, db_name: str, collection_name: str):
        client = MongoClient(db_uri)
        self.collection = client[db_name][collection_name]

    def get_by_id(self, id: str) -> NewTable:
        doc = self.collection.find_one({'_id': ObjectId(id)})
        return NewTable(**doc)
