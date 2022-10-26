import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["the_film_library"]
colPeli = db["films"]
colDir = db["directors"]
colAct = db["actors"]
colGen = db["genres"]


def searchTitle(title):
    data = colPeli.find({"title": {"$regex": title, "$options": "i"}})
    data = list(data)
    dataList = []
    for i in range(len(data)):
        tolist = []
        film = data[i]
        tolist.append(film["title"])
        tolist.append((film["released"].strftime("%d/%m/%Y")) if film["released"] != "N/A" else "N/A")
        tolist.append(film["runtime"])
        tolist.append((searchGenreArray(film["genre"]) if film["genre"] != "N/A" else "N/A"))
        tolist.append((searchDirectorById(film["director"] if film["director"] != "N/A" else "N/A")))
        tolist.append(film["rating"])
        dataList.append(tolist)
    return dataList


def searchDirector(director):
    return colDir.find({"full-name": {"$regex": director, "$options": "i"}})


def searchDirectorById(id):
    data = colDir.find_one({"_id": id})
    if data is None:
        return "N/A"
    return data["full-name"]


def searchActor(actor):
    return colAct.find({"full-name": {"$regex": actor, "$options": "i"}})


def searchGenre(genre):
    return colGen.find({"name": {"$regex": genre, "$options": "i"}})


def searchGenreArray(arrayId):
    data = []
    for i in range(len(arrayId)):
        data.append(colGen.find_one({"_id": arrayId[i]})["name"])
        if data is None:
            continue
    if len(data) == 0:
        return "N/A"
    return data


if __name__ == "__main__":
    print(searchTitle("Clown"))
