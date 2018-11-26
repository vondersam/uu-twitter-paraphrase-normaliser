import spacy
import sys
import json
import csv
from os import listdir
import itertools
from random import randrange
from tweet import Tweet


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


def group_entities(input_dir, limit):
    """ Group tweets by entities. Set limit to 0 to check all files """
    ner_dict = dict()
    if limit == 0:
        limit = len(listdir(input_dir))
    counter = 0

    for filename in listdir(input_dir):
        if ".csv" in filename:
            if counter < limit:
                counter += 1
                print(f"Checking NER in {filename}")
                input_path = input_dir + filename
                with open(input_path) as file_in:
                    reader = csv.DictReader(file_in)
                    for row in reader:
                        _id = row["id"]
                        t = Tweet(row["tweet"]).spacyfy("clean", "*")
                        filter_entities(t, _id, ner_dict)
    save_output(ner_dict, input_dir)


def save_output(dictionary, ouput_dir):
    print(f"Saving results to file...")
    output_path = ouput_dir + "grouped_entities.json"
    with open(output_path, 'w') as f:
        json.dump(dictionary, f)

'''
def save_output(dictionary, ouput_dir, split_limit):
    print(f"Saving results to file...")

    counter = 0
    output_path = ouput_dir + "grouped_entities.json" + str(randrange(10000))
    file_out = open(output_path, 'w')

    for key, value in dictionary.items():
        if counter < split_limit:
            counter += 1
            json.dump(dictionary, file_out)
        else:
            counter = 0
            file_out.close()
            output_path = ouput_dir + "grouped_entities.json" + str(randrange(10000))
            file_out = open(output_path, 'w')
    file_out.close()
'''

if __name__ == "__main__":
    main()
    #input_path = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/cleanup_twitter_corpus/"
    #output_path = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/grouped_ner/"
    #results = group_entities(input_path, 1)
    #similarities = group_similarity(results, 1)
    #print(similaritites)
    #save_output(similarities, output_path, 1)




