import imp
import pymongo
import json
from datetime import datetime
import pickle
from getJsonFromApi import tsvScrapper


def main():
    global db, colPeli, colDir, tsv
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["the_film_library"]
    colPeli = db["peliculas"]
    colDir = db["directores"]
    tsv = tsvScrapper("names.tsv")
    for i in range(6):
        fd = "./data/titleData"+str(i+1)+".json"
        print("Cargando archivo: " + fd)
        data = getData(fd)
        for title in data:
            colPeli.insert_one(formatData(title))
        print("Archivo cargado")


def getData(path):
    with open(path, 'r') as fd:
        data = json.load(fd)
        fd.close()
    data = data["titleList"]
    return data

def formatData(json):
    cleanJson = {
        "title": json["Title"],
        "year":  int(json["Year"]),
        "released": formatDatetime(json["Released"]),
        "runtime": json["Runtime"],
        "genre": json["Genre"],
        "director": directorManager(json["Director"]),
        "actors": json["Actors"],
        "plot": json["Plot"],
        "country": json["Country"],
        "rating": formatInt(json["imdbRating"]),
    }
    return cleanJson

def directorManager(director):
    global colDir
    dir = colDir.find_one({"full-name": director})
    if dir is None:
        dir = formatDir(director)


def formatDir(name):
    global tsv
    #find director in tsv
    dirData = tsv['primaryName'] == name
    dirJson = {
        "full-name": json["Name"]
    }
    return dirJson

def formatDatetime(date):
    if date != "N/A":
        release = datetime.strptime(date, '%d %b %Y').replace(microsecond=0)
        return release
    return "N/A"


def formatInt(x):
    return float(x) if x != "N/A" else "N/A"

    
if __name__ == "__main__":
    main()
