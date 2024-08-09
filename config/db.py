from pymongo import MongoClient

MONGO_DETAILS =  "mongodb://localhost:27017/prueba"

client = MongoClient(MONGO_DETAILS)
database = client.prueba

users_collection = database.get_collection("users")



