import spacy
import sys
import json
import csv
import pycld2 as cld2
from textblob import TextBlob

#nlp = spacy.load('es_core_news_md')

# Preprocessing
# filter out text not in Spanish
# delete duplicates
# not taking out mention

def jaccard():
    ''' Calculate jaccard distance of two strings '''

'''
def ner(doc, dictionary):
    for ent in doc.ents:
        if (ent.label_, ent.text) not in dictionary:
            dictionary[ent.text] = [doc.text]
        else:
            dictionary[ent.text].append(doc.text)
    return dictionary


def process(files_path):
    """ Name Entity Recognition """
    ner_dict = dict()

    with open("tweets_text.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row["text"]:
                doc = nlp(row["text"])
                ner(doc, ner_dict)

    return json.dumps(ner_dict)
'''

def metrics():
    ''' Retrieve the metrics of the corpus '''
    pass

'''
def identify_language(file_path):
    #detectedLangName, detectedLangCode, isReliable, textBytesFound, details = cld2.detect("This is my sample text", pickSummaryLanguage=True, removeWeakMatches=False)
    #print(cld2.LANGUAGES)
    with open(file_path) as json_file:
        for line in json_file:
            data = json.loads(line)
            results = cld2.detect(data["text"].encode(), isPlainText=True) # Encode to bytes with default UTF-8 as required by cld2
            print(data["text"])
            print(results)
'''




# The output look lie so:
#  detected: ENGLISH
#  reliable: True
#  textBytes: 25
#  details: [('ENGLISH', 'en', 64, 20.25931928687196), ('FRENCH', 'fr', 36, 8.221993833504625)]



if __name__ == "__main__":
    #print(process("/home/samuel/Documents/Classes/research_and_development/twitter-corpus"))
    identify_language("/home/samuel/twitter-files/tweets.20181112-143850.json")




