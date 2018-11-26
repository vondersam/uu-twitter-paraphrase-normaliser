from tweet import Tweet
from clean_corpus import clean_corpus
from name_entity_recognition import group_entities
from similarity import calculate_similarity
import json
import csv


class Corpus:
    def __init__(self):
        # tweet id + filename
        self.tweets = {} # inverted_tracker
        self.tweets_by_entity = {} #dict {ENT: [id1, id2, id3]}
        self.paraphrases = {} # dict {SENT: [paraphrase1, paraphrase2]}


    def create_corpus(self, input_dir, output_dir, language, foreign=False):
        """ Create a corpus from a directory of json tweet files """
        clean_corpus(input_dir, output_dir, language, foreign)
        return self.tweets


    def group_by_entity(self, input_dir, limit, save_in_memory=False):
        """ Group all tweets by entity """
        group_entities(input_dir, limit)


    def get_tweets_by_entity(self, file_path):
        with open(file_path, 'r') as f:
            return json.load(f)


    def get_tweet_by_id(self, _id, input_directory, inverted_tracker):
        filename = inverted_tracker[_id]
        path_to_file = input_directory + filename
        with open(path_to_file, 'r') as f:
            data = csv.DictReader(f)
            for row in data:
                if row["id"] == _id:
                    return row["tweet"]


    def get_tweets_by_ids(self, id_list, input_directory, inverted_tracker):
        list_of_tweets = []
        for _id in id_list:
            t = self.get_tweet_by_id(_id, input_directory, inverted_tracker)
            list_of_tweets.append(Tweet(t).spacyfy("clean", "*"))

        return list_of_tweets


    def get_inverted_tracker(self, input_directory):
        # this can be substituted by function load-tracker
        path_to_file = input_directory + "inverted_tracker.json"
        with open(path_to_file, 'r') as f:
            return json.load(f)


    def extract_paraphrases(self, input_directory, threshold):
        print("Calculating similarities in tweets...")
        results = {}
        file_path = input_directory + "grouped_entities.json"
        grouped_entities = self.get_tweets_by_entity(file_path)
        inverted_tracker = self.get_inverted_tracker(input_directory)

        for entity, id_list in grouped_entities.items():
            tweets_list = self.get_tweets_by_ids(id_list, input_directory, inverted_tracker)
            paraphrases = calculate_similarity(tweets_list, threshold)
            results[ner] = paraphrases

        paraphrases_path = input_directory + "paraphrases.json"

        with open("paraphrases_path", 'w') as fout:
            json.dump(results, fout)
