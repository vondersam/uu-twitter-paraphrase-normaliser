import csv

fil = "/home/samuel/Documents/result_test_corpus/tweets.20181126-080916.csv"

with open(fil, 'r') as f:
    data = csv.DictReader(f)
    for i in data:
        print(i["id"])
