import json
from os import path
import os.path
from turtle import title
import pandas as pd
import pickle
import requests


def main():
    tsv = tsvWrapper("titleId.tsv")
    keys = ["6b053336", "333860bc", "c6d9565f", "3e563fe7", "90e7a4"]
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
            data = requests.get("http://www.omdbapi.com/?apikey="+key+"&i="+id)
            print(data)
            titleData.append(data.json())
            index += 1
    print("New last index: " + str(index))
    saveLastIndex(index)
    return titleData

def dataToJson(titleData):
    data = {
        "titleList" : titleData
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

def tsvWrapper(tsvFile):
    with open(tsvFile, encoding="utf8") as fd:
        tsv = pd.read_csv(fd, sep="\t",encoding="utf-8", low_memory=False)
        fd.close()
    return tsv

if __name__ == "__main__":
    main()
