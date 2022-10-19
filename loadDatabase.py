import pymongo
import json
from datetime import datetime


def main():
    global db, colPeli, colDir, colAct, colNames, colGen
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["the_film_library"]
    colPeli = db["films"]
    colDir = db["directors"]
    colAct = db["actors"]
    colGen = db["genres"]
    colNames = db["names"]
    for i in range(6):
        fd = "./data/titleData"+str(i+1)+".json"
        print("Cargando archivo: " + fd+"\n")
        data = getData(fd)
        for title in data:
            colPeli.insert_one(createFilm(title))
        print("Archivo cargado\n")

    #update directors and actors titles
    print("Actualizando titulos de directores y actores\n")
    for director in colDir.find():
        titles = []
        for title in colPeli.find({"director": director["_id"]}):
            titles.append(title["_id"])
        colDir.update_one({"_id": director["_id"]}, {"$set": {"titles": titles}})
    for actor in colAct.find():
        titles = []
        for title in colPeli.find({"actors": actor["_id"]}):
            titles.append(title["_id"])
        colAct.update_one({"_id": actor["_id"]}, {"$set": {"titles": titles}})
    print("Actualizados los títulos de los directores y actores\n")


def getData(path):
    with open(path, 'r') as fd:
        data = json.load(fd)
        fd.close()
    data = data["titleList"]
    return data


def createFilm(json):
    print("Creando pelicula\n")
    cleanJson = {
        "title": json["Title"],
        "year":  int(json["Year"]),
        "released": formatDatetime(json["Released"]),
        "runtime": json["Runtime"],
        "genre": genresManager(json["Genre"]),
        "director": directorManager(json["Director"]),
        "actors": actorsManager(json["Actors"]),
        "plot": json["Plot"],
        "country": json["Country"],
        "rating": (float(json["imdbRating"]) if json["imdbRating"] != "N/A" else "N/A"),
    }
    return cleanJson


def directorManager(director):
    global colDir
    dir = colDir.find_one({"full-name": director})
    if dir is None:
        # Creates director if not found
        print("Director no encontrado, creando director\n")
        dir = createDir(director)
        if dir is None:
            print("Director no encontrado en col names")
            return "N/A"
        colDir.insert_one(dir)
        print("Director creado y cargado a la DB \n")
        dir = colDir.find_one({"full-name": director})
    print("Director encontrado, id: " + str(dir["_id"]) + "\n")
    return dir["_id"]


def createDir(director):
    global colNames
    dir = colNames.find_one({"primaryName": director})
    if dir is not None:
        dir = {
            "full-name": dir['primaryName'],
            "birthYear": (int(dir['birthYear']) if dir['birthYear'] != "\\N" else "N/A"),
            "deathYear": (int(dir['deathYear']) if dir['deathYear'] != "\\N" else "N/A"),
            "primaryProfession": dir['primaryProfession'],
            "titles": []
        }
    return dir


def actorsManager(actors):
    global colAct
    actToFilm = []
    actors = actors.split(", ")
    for actor in actors:
        act = colAct.find_one({"full-name": actor})
        if act is None:
            # Creates actor if not found
            print("Actor no encontrado, creando actor\n")
            act = createAct(actor)
            if act is None:
                print("Actor no encontrado en col names")
                return "N/A"
            colAct.insert_one(act)
            print("Actor creado y cargado a la DB \n")
            act = colAct.find_one({"full-name": actor})
        print("Actor encontrado, id: " + str(act["_id"]) + "\n")
        actToFilm.append(act["_id"])
    return actToFilm


def createAct(actor):
    global colNames
    act = colNames.find_one({"primaryName": actor})
    if act is not None:
        act = {
            "full-name": act['primaryName'],
            "birthYear": (int(act['birthYear']) if act['birthYear'] != "\\N" else "N/A"),
            "deathYear": (int(act['deathYear']) if act['deathYear'] != "\\N" else "N/A"),
            "primaryProfession": act['primaryProfession'],
            "titles": []
        }
    return act


def genresManager(genres):
    global colGen
    genreList = []
    genres = genres.split(", ")
    for genre in genres:
        gen = colGen.find_one({"name": genre})
        if gen is None:
            # Creates genre if not found
            print("Genero no encontrado, creando genero\n")
            gen = createGen(genre)
            colGen.insert_one(gen)
            print("Genero creado y cargado a la DB \n")
            gen = colGen.find_one({"name": genre})
        print("Genero encontrado, id: " + str(gen["_id"]) + "\n")
        genreList.append(gen["_id"])
    return genreList


def createGen(genre):
    gen = {
        "name": genre
    }
    return gen


def formatDatetime(date):
    if date != "N/A":
        release = datetime.strptime(date, '%d %b %Y').replace(microsecond=0)
        return release
    return "N/A"


if __name__ == "__main__":
    main()
