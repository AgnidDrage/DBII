import pandas as pd
import time

with open("titleId.tsv", encoding="utf8") as fd:
    rd = pd.read_csv(fd, sep="\t",encoding="utf-8", low_memory=False)
    titleId = rd.titleId
    fd.close()
print(titleId)
#titleId.to_csv("titleId.tsv", sep="\t", encoding="utf-8")



# data = requests.get("http://www.omdbapi.com/?apikey=333860bc&i=" + moviesID[5] + "&plot=full")
# data = data.json()
# print(data)