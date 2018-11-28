from random import randrange
from tweet import Tweet
from file_manager import load_tracker, save_tracker
from os import listdir
import spacy
import sys
import json
import csv
import itertools



nlp = spacy.load('es_core_news_md')

#SAVE ner SO WE DONT HAVE TO RUN IT EVERYTIME. rIGHT NOW ITS GETTING OVERWRITTEN
def filter_entities(doc, _id, dictionary):
    for ent in doc.ents:
        key = str((ent.label_, ent.text))
        if key not in dictionary:
            dictionary[key] = [_id]

        # Exclude duplicated tweets
        else:
            if _id not in dictionary[key]:
                dictionary[key].append(_id)


def group_entities(input_dir, limit=0):
    """ Group tweets by entities. Set limit to 0 to check all files """

    # Set number of files to check
    if limit == 0:
        limit = len(listdir(input_dir))
    counter = 0

    tracker = load_tracker(input_dir, "ner", "tracker.json")
    ner_dict = load_tracker(input_dir, "ner", "grouped_entities.json")

    corpus_dir = input_dir + "corpus/"

    for filename in listdir(corpus_dir):
        if filename.endswith(".csv") and filename not in tracker:
            counter += 1
            print(f"Checking NER in {filename}")
            input_path = corpus_dir + filename

            with open(input_path) as file_in:
                reader = csv.DictReader(file_in)
                for row in reader:
                    _id = row["id"]
                    t = Tweet(row["tweet"]).spacyfy("clean", "*")
                    filter_entities(t, _id, ner_dict)
            tracker[filename] = None

        save_tracker(input_dir, "ner", "grouped_entities.json", ner_dict)
        save_tracker(input_dir, "ner", "tracker.json", tracker)
    print("All entities grouped")
    return ner_dict



if __name__ == "__main__":
    main()





