from tweet import Tweet
from clean_corpus import clean_corpus
from name_entity_recognition import group_entities
from similarity import calculate_similarity
from file_manager import load_tracker, write_final_files
from collections import OrderedDict
from os import path, makedirs
import json
import csv
import sys
from multiprocessing import Pool



class Corpus:
    def __init__(self):
        self.tweet = None

    def create_corpus(self, input_dir, output_dir, language, foreign=False):
        """ Create a corpus from a directory of json tweet files """
        clean_corpus(input_dir, output_dir, language, foreign)


    def group_by_entity(self, input_directory):
        """ Group all tweets by entity """
        return group_entities(input_directory)


    def get_tweets_by_entity(self, file_path):
        with open(file_path, 'r') as f:
            return json.load(f)


    def get_tweet_by_id(self, _id, input_directory, inverted_tracker):
        filename = inverted_tracker[_id]
        path_to_file = input_directory + "corpus/" + filename
        with open(path_to_file, 'r') as f:
            data = csv.DictReader(f)
            for row in data:
                if row["id"] == _id:
                    return row["tweet"]


    def get_tweets_by_ids(self, id_list, input_directory, inverted_tracker):
        list_of_tweets = []
        for _id in id_list:
            t = self.get_tweet_by_id(_id, input_directory, inverted_tracker)
            list_of_tweets.append(Tweet(t))

        return list_of_tweets


    def split_dict_equally(self, input_dict, chunks=2):
        """ http://enginepewpew.blogspot.com/2012/03/splitting-dictionary-into-equal-chunks.html
        """
        # Splits dict by keys. Returns a list of dictionaries.
        # prep with empty dicts
        return_list = [dict() for idx in range(chunks)]
        idx = 0
        for k,v in input_dict.items():
            return_list[idx][k] = v
            if idx < chunks-1:  # indexes start at 0
                idx += 1
            else:
                idx = 0
        return return_list


    def extract_paraphrases(self, input_directory, similarity_type, threshold):

        print("Calculating similarities in tweets...")
        results = {}

        # Get all entities
        entities = self.group_by_entity(input_directory)
        inverted_tracker = load_tracker(input_directory, "cleaning", "inv_tracker.json")
        #number_of_splits = 8
        #print("Dictionary has been split")
        #list_of_dicts = self.split_dict_equally(entities, number_of_splits)
        #list_of_numbers = list(range(number_of_splits))


        #for grouped_entities in list_of_dicts:
        #current = str(list_of_numbers.pop(0))
        #print(f"{current}/{str(number_of_splits)} processed similarities")

        # Multiprocessing pool to extract paraphrases faster
        p = Pool()
        paraphrases_results = [p.apply_async(calculate_similarity, args=(self.get_tweets_by_ids(id_list, input_directory, inverted_tracker),similarity_type, threshold,)) for entity, id_list in entities.items()]


        # Write output in source and target files
        write_final_files(input_directory, paraphrases_results, "final")
        p.close()
        p.join()
        print("All paraphrases extracted")

if __name__ == '__main__':
    main()


