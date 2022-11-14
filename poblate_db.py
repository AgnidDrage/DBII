import pymongo
import json
from pymongo import MongoClient
from bson.json_util import loads, dumps

client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb+srv://AgnidDrage:Lunitamia123123@thefilmlibrary.krwlk51.mongodb.net/?retryWrites=true&w=majority', 27017)
global films, actors, directors, genres, countries

def load_files():
    global films, actors, directors, genres, countries
    print('[ LOADING JSON FILES ]')

    with open('./dbData/films.json', encoding="utf8") as f:
        films = json.load(f)
    with open('./dbData/actors.json', encoding="utf8") as f:
        actors = json.load(f)
    with open('./dbData/directors.json', encoding="utf8") as f:
        directors = json.load(f)
    with open('./dbData/genres.json', encoding="utf8") as f:
        genres = json.load(f)
    with open('./dbData/countries.json', encoding="utf8") as f:
        countries = json.load(f)

    poblate_db()

def poblate_db():
    global films, actors, directors, genres, countries
    print('[ CREATING DATABASE ]')
    db = client['the_film_library']
    print('[ CREATING COLLECTIONS ]')

    collection_films = db['films']
    collection_actors = db['actors']
    collection_directors = db['directors']
    collection_genres = db['genres']
    collection_countries = db['countries']

    films = dumps(films) # Se convierte la lista de JSON en str sin formato
    films = loads(films) # Se convierten los $oid en ObjectId
    actors = dumps(actors)
    actors = loads(actors)
    directors = dumps(directors)
    directors = loads(directors)
    genres = dumps(genres)
    genres = loads(genres)
    countries = dumps(countries)
    countries = loads(countries)
    
    try:
        collection_films.insert_many(films)
        collection_actors.insert_many(actors)
        collection_directors.insert_many(directors)
        collection_genres.insert_many(genres)
        collection_countries.insert_many(countries)
    except pymongo.errors.BulkWriteError as error:
        print('[ ERROR AL POBLAR BASE DE DATOS ]')
        print(error.details)

    print('[ DATABASE POBLATED ]')


if __name__ == '__main__':
    load_files()
