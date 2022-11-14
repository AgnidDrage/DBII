import pymongo
import json
from pymongo import MongoClient
from bson.json_util import loads, dumps

client = MongoClient('localhost', 27017)
global films, actors, directors, genres

def load_files():
    global films, actors, directors, genres
    print('[ LOADING JSON FILES ]')

    with open('./dbData/films.json', encoding="utf8") as f:
        films = json.load(f)
    with open('./dbData/actors.json', encoding="utf8") as f:
        actors = json.load(f)
    with open('./dbData/directors.json', encoding="utf8") as f:
        directors = json.load(f)
    with open('./dbData/genres.json', encoding="utf8") as f:
        genres = json.load(f)

    poblate_db()

def poblate_db():
    global films, actors, directors, genres
    print('[ CREATING DATABASE ]')
    db = client['the_film_library']
    print('[ CREATING COLLECTIONS ]')

    collection_films = db['films']
    collection_actors = db['actors']
    collection_directors = db['directors']
    collection_genres = db['genres']

    films = dumps(films) # Se convierte la lista de JSON en str sin formato
    films = loads(films) # Se convierten los $oid en ObjectId
    actors = dumps(actors)
    actors = loads(actors)
    directors = dumps(directors)
    directors = loads(directors)
    genres = dumps(genres)
    genres = loads(genres)
    
    try:
        collection_films.insert_many(films)
        collection_actors.insert_many(actors)
        collection_directors.insert_many(directors)
        collection_genres.insert_many(genres)
    except pymongo.errors.BulkWriteError as error:
        print('[ ERROR AL POBLAR BASE DE DATOS ]')
        print(error.details)

    print('[ DATABASE POBLATED ]')


if __name__ == '__main__':
    load_files()
