import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["the_film_library"]
colPeli = db["films"]
colDir = db["directors"]
colAct = db["actors"]
colGen = db["genres"]


def searchTitle(title):
    if title != "":
        data = colPeli.find({"title": {"$regex": title, "$options": "i"}})
        data = list(data)
        dataList = []
        fullData = []
        print(data)
        for i in range(len(data)):
            toDataList = []
            toFullData = []
            film = data[i]

            genre = searchGenreArray(film["genre"])
            director = searchDirectorById(film["director"])

            toDataList.append(film["title"])
            toDataList.append((film["released"].strftime(
                "%d/%m/%Y")) if film["released"] != "N/A" else "N/A")
            toDataList.append(film["runtime"])
            toDataList.append([gen["name"] for gen in genre]
                              if genre != "N/A" else "N/A")
            toDataList.append(director["full-name"]
                              if director != "N/A" else "N/A")
            toDataList.append(film["rating"])
            
            dataList.append(toDataList)

            toFullData.append(film["title"])
            toFullData.append(film["year"] if film["year"] != "N/A" else "N/A")
            toFullData.append(film["released"].strftime("%d/%m/%Y") if film["released"] != "N/A" else "N/A")
            toFullData.append(film["runtime"])
            toFullData.append([gen for gen in genre] if genre != "N/A" else "N/A")
            toFullData.append(director if director != "N/A" else "N/A")
            toFullData.append(searchActorById(film["actors"]) if film["actors"] != "N/A" else "N/A")
            toFullData.append(film["plot"])
            toFullData.append(film["country"])
            toFullData.append(film["rating"])

            fullData.append(toFullData)
     
        return dataList, fullData
    return []


def searchDirector(director):
    return colDir.find({"full-name": {"$regex": director, "$options": "i"}})


def searchDirectorById(id):
    data = colDir.find_one({"_id": id})
    if data is None:
        return "N/A"
    return data


def searchActor(actor):
    return colAct.find({"full-name": {"$regex": actor, "$options": "i"}})


def searchActorById(id):
    data = []
    for i in range(len(id)):
        data.append(colAct.find_one({"_id": id[i]}))
        if data is None:
            continue
    if len(data) == 0:
        return "N/A"
    return data


def searchGenre(genre):
    return colGen.find({"name": {"$regex": genre, "$options": "i"}})


def searchGenreArray(arrayId):
    data = []
    for i in range(len(arrayId)):
        data.append(colGen.find_one({"_id": arrayId[i]}))
        if data is None:
            continue
    if len(data) == 0:
        return "N/A"
    return data


if __name__ == "__main__":
    print(searchTitle("Clown"))
