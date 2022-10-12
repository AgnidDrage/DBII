import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["the_film_library"]
directores = db["directores"]
print(directores.find_one({"name": "Steven Spielberg"}))