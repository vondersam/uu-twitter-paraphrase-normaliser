import spacy
import sys
import json
import csv

nlp = spacy.load('es_core_news_md')

# Preprocessing
# filter out text not in Spanish
# delete duplicates
# not taking out mention

def jaccard():
    ''' Calculate jaccard distance of two strings '''

def ner(doc, dictionary):
    for ent in doc.ents:
        if (ent.label_, ent.text) not in dictionary:
            dictionary[ent.text] = [doc.text]
        else:
            dictionary[ent.text].append(doc.text)
    return dictionary


def process(files_path):
    ''' Name Entity Recognition '''
    ner_dict = dict()

    with open("tweets_text.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row["text"]:
                doc = nlp(row["text"])
                ner(doc, ner_dict)

    return json.dumps(ner_dict)


def metrics():
    ''' Retrieve the metrics of the corpus '''
    pass



if __name__ == "__main__":
    print(process("/Users/samuelrodriguezmedina/twitter-files"))



