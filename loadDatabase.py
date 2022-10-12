import pymongo
import json
from datetime import datetime


def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["the_film_library"]
    col = db["peliculas"]
    for i in range(6):
        fd = "./data/titleData"+str(i+1)+".json"
        print("Cargando archivo: " + fd)
        data = getData(fd)
        for title in data:
            uploadToDB(formatData(title), col)
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
        "director": json["Director"],
        "actors": json["Actors"],
        "plot": json["Plot"],
        "country": json["Country"],
        "rating": formatInt(json["imdbRating"]),
    }
    return cleanJson


def formatDatetime(date):
    if date != "N/A":
        release = datetime.strptime(date, '%d %b %Y').replace(microsecond=0)
        return release
    return "N/A"


def formatInt(x):
    return float(x) if x != "N/A" else "N/A"


def uploadToDB(json, col):
    col.insert_one(json)


if __name__ == "__main__":
    main()
