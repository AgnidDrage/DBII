import json
from os import path
import pandas as pd
import pickle
import requests


def main():
    tsv = tsvScrapper("titleId.tsv")
    keys = ["6b053336", "333860bc", "c6d9565f",
            "3e563fe7", "90e7a4", "bec86365", "1f9ba3da"]
    titleId = tsv.titleId
    titleData = requestData(keys, titleId)
    dataToJson(titleData)


def requestData(keys, titleId):
    if path.exists("./data/lastIndex.p"):
        index = loadLastIndex()
        print("Last index: " + str(index))
    else:
        index = 0
    titleData = []
    #key = keys[3]
    for key in keys:
        for i in range(1000):
            id = titleId[index]
            print("http://www.omdbapi.com/?apikey="+key+"&i="+id)
            data = requests.get("http://www.omdbapi.com/?apikey="+key+"&i="+id)
            if data.status_code != 200:
                print("Error en la peticion, codigo: " + str(data.status_code))
                continue
            else:
                print(data)
                titleData.append(data.json())
                index += 1
    print("New last index: " + str(index))
    saveLastIndex(index)
    return titleData


def dataToJson(titleData):
    data = {
        "titleList": titleData
    }
    with open("./data/titleData.json", "w") as fd:
        json.dump(data, fd)


def saveLastIndex(index):
    with open("./data/lastIndex.p", "wb") as fd:
        pickle.dump(index, fd)
        fd.close()


def loadLastIndex():
    with open("./data/lastIndex.p", "rb") as fd:
        index = pickle.load(fd)
        fd.close()
    return index


def tsvScrapper(tsvFile):
    with open(tsvFile, encoding="utf8") as fd:
        tsv = pd.read_csv(fd, sep="\t", encoding="utf-8", low_memory=False)
        fd.close()
    return tsv


if __name__ == "__main__":
    main()
