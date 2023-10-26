from pymongo import MongoClient



client = MongoClient("mongodb+srv://alford:alford@cluster0.kljzgft.mongodb.net/?retryWrites=true&w=majority")


db = client.todo_app

collection_name = db["todos_app"]