import pymongo


def main():
    global db, colPeli, colDir, colAct, colCountr, colGen
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["the_film_library"]
    colPeli = db["films"]
    colDir = db["directors"]
    colAct = db["actors"]
    colGen = db["genres"]
    colCountr = db["countries"]
    i = -1
    for peli in colPeli.find():
        i += 1
        print("Update: " + str(i))
        if peli["director"] != "N/A":
            colPeli.update_one({"_id": peli["_id"]}, {
                               "$set": {"director": addDirNameInPeli(peli)}})
        if peli["country"] != "N/A":
            colPeli.update_one({"_id": peli["_id"]}, {
                               "$set": {"country": addCountryInCol(peli)}})
        if peli["genre"] != "N/A":
            genre = []
            for gen in peli["genre"]:
                genre.append(colGen.find_one({"_id": gen})["name"])
            colPeli.update_one({"_id": peli["_id"]}, {
                               "$set": {"genre": genre}})


def addDirNameInPeli(peli):
    dir = colDir.find_one({"_id": peli["director"]})
    newData = {
        "_id": peli["director"],
        "full-name": dir["full-name"],
    }
    return newData


def addCountryInCol(peli):
    country = colCountr.find_one({"name": peli["country"]})
    if country is None:
        colCountr.insert_one({"name": peli["country"]})
        country = colCountr.find_one({"name": peli["country"]})
        data = {
            "_id": country["_id"],
            "name": country["name"]
        }
        return data
    else:
        data = {
            "_id": country["_id"],
            "name": country["name"]
        }
        return data


if __name__ == "__main__":
    main()
