from nltk.tokenize import TweetTokenizer
#from  file_manager import load_tracker
#from corpus import Corpus
#from tweet import Tweet
#import csv

'''
with open ("experiment1/corpus/tweets.20181119-223357.csv", 'r') as f:
    data = csv.DictReader(f)
    for i in data:
        t = i["tweet"]
        try:
            print(Tweet(t).spacyfy("clean", "*"))
        except Exception as e:
            print(e)
            print(i["tweet"])
'''

t = "Hoy hablamos sobre @maria la #polémica surgida en #OTDirecto29OCT con #Miki y #María por su intención de #cambiar La #estupidez por la #mariconez."
results = TweetTokenizer().tokenize(t)
print(" ".join(results))
