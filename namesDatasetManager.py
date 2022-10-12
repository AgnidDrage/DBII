import pymongo
import pandas
import json
from getJsonFromApi import tsvScrapper


def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["the_film_library"]
    directores = db["directores"]
    peliculas = db["peliculas"]
    tsv = tsvScrapper("names.tsv")
    for peli in peliculas.find():
        update(peli, tsv, directores, peliculas)

def update(peli, tsv, directores, peliculas):
    pelicula = json.loads(peli)
    peliDirector = pelicula["director"]
    for director in tsv.primaryName:
        if director == peliDirector:
            if directores.find_one({"name": director}) != None:
                updatePeli()
            createDirector(director, pelicula)

def createDirector(dir, pelicula):
    director = {
        "name": dir['primaryName'],
        "birthYear": int(dir['birthYear']),
        "deathYear": (int(dir['deathYear']) if dir['deathYear'] != "\\N" else "N/A"),
        "primaryProfession": dir['primaryProfession'],
        "titles": [pelicula['_id']]

    }

def updatePeli():
    pass


if __name__ == "__main__":
    main()
