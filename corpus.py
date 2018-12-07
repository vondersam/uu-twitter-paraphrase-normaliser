from tweet import Tweet
from clean_corpus import clean_corpus
from name_entity_recognition import group_entities
from similarity import calculate_similarity
from file_manager import load_tracker
from collections import OrderedDict
from os import path, makedirs
import json
import csv


class Corpus:
    def __init__(self):
        self.tweet = None

    def create_corpus(self, input_dir, output_dir, language, foreign=False):
        """ Create a corpus from a directory of json tweet files """
        clean_corpus(input_dir, output_dir, language, foreign)


    def get_tweets_by_entity(self, file_path):
        with open(file_path, 'r') as f:
            return json.load(f)


    def group_by_entity(self, input_directory):
        """ Group all tweets by entity """
        return group_entities(input_directory)


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
            list_of_tweets.append(Tweet(t).filter("*"))

        return list_of_tweets


    def extract_paraphrases(self, input_directory, similarity_type, threshold):
        print("Calculating similarities in tweets...")
        results = {}
        grouped_entities = self.group_by_entity(input_directory)
        inverted_tracker = load_tracker(input_directory, "cleaning", "inv_tracker.json")

        for entity, id_list in grouped_entities.items():
            tweets_list = self.get_tweets_by_ids(id_list, input_directory, inverted_tracker)
            paraphrases = calculate_similarity(tweets_list, similarity_type, threshold)
            for paraphrase_pair in paraphrases:
                results[paraphrase_pair[0]] = paraphrase_pair[1]

        paraphrases_path = input_directory + "paraphrases.json"


        with open(paraphrases_path, 'w') as fout:
            json.dump(results, fout)
        print("All paraphrases extracted")
