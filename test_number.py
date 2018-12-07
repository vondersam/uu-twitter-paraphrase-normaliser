from tweet import Tweet
import csv

original= ["tweets.20181026-184718.csv",
"tweets.20181026-185922.csv",
"tweets.20181026-190116.csv",
"tweets.20181026-190858.csv",
"tweets.20181103-103830.csv",
"tweets.20181103-105835.csv",
"tweets.20181103-110122.csv",
"tweets.20181103-112609.csv",
"tweets.20181103-113221.csv",
"tweets.20181103-125524.csv",
"tweets.20181103-125820.csv",
"tweets.20181103-133224.csv",
"tweets.20181103-185848.csv",
"tweets.20181103-190057.csv",
"tweets.20181103-190158.csv",
"tweets.20181103-190937.csv",
"tweets.20181103-192901.csv",
"tweets.20181103-201749.csv",
"tweets.20181103-213238.csv"]

tracker = {"tweets.20181026-190858.csv": None,
  "tweets.20181026-185922.csv": None,
  "tweets.20181103-185848.csv": None,
  "tweets.20181103-113221.csv": None,
  "tweets.20181103-190937.csv": None,
  "tweets.20181103-190158.csv": None,
  "tweets.20181103-213238.csv": None,
  "tweets.20181103-125524.csv": None,
  "tweets.20181103-201749.csv": None,
  "tweets.20181103-133224.csv": None,
  "tweets.20181026-184718.csv": None,
  "tweets.20181103-112609.csv": None,
  "tweets.20181103-105835.csv": None,
  "tweets.20181103-192901.csv": None,
  "tweets.20181103-110122.csv": None,
  "tweets.20181026-190116.csv": None,
  "tweets.20181103-190057.csv": None,
  "tweets.20181103-125820.csv": None}

for i in original:
    if i not in tracker:
        filename = i

with open("/Users/samuelrodriguezmedina/Documents/classes/research_and_development/uu-twitter-paraphrase-normaliser/corpus/tweets.20181103-103830.csv") as f:
    data = csv.DictReader(f)
    for row in data:
        print(row)
        #t = Tweet(row["tweet"])
        #print(t.spacyfy("clean", "*"))

for i in rage(10):
    print(i)


