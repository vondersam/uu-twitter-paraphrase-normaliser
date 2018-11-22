import spacy
import sys
import json
import csv
from os import listdir
import itertools
from random import randrange


nlp = spacy.load('es_core_news_md')


def filter_entities(doc, dictionary):
    for ent in doc.ents:
        key = str((ent.label_, ent.text))
        if key not in dictionary:
            dictionary[key] = [doc]

        # Exclude duplicated tweets
        else:
            if doc not in dictionary[key]:
                dictionary[key].append(doc)


def group_entities(input_dir, limit):
    """ Group tweets by entities. Set limit to 0 to check all files """
    ner_dict = dict()
    if limit == 0:
        limit = len(listdir(input_dir))
    counter = 0

    for filename in listdir(input_dir):
        if "_foreign" not in filename:
            if counter < limit:
                counter += 1
                print(f"Checking NER in {filename}")
                input_path = input_dir + filename
                with open(input_path) as file_in:
                    reader = csv.DictReader(file_in)
                    for row in reader:
                        if row["tweet"]:
                            doc = nlp(row["tweet"])
                            filter_entities(doc, ner_dict)
    return ner_dict


def calculate_similarity(docs_list):
    ''' Calculate similarity of all possible pairs in list '''
    # (JK, MN): [((textA, textB), 0.9), ((textA, textB), 0.9)]
    results = list()
    all_combinations = list(itertools.combinations(docs_list, 2))
    for combination in all_combinations:
        each_result = (combination[0].text, combination[1].text), combination[0].similarity(combination[1])
        results.append(each_result)
    return results


def group_similarity(dictionary, threshold):
    ''' Group tweets by similarity '''
    print("Calculating similarities in tweets...")
    results = {}
    for key, docs_list in dictionary.items():
        results[key] = calculate_similarity(docs_list)
    return results


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



if __name__ == "__main__":
    input_path = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/cleanup_twitter_corpus/"
    output_path = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/grouped_ner/"
    results = group_entities(input_path, 1)
    #similarities = group_similarity(results, 1)
    #print(similaritites)
    #save_output(similarities, output_path, 1)




