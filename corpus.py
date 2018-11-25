class Corpus:
    def __init__(self):
        # ID + Tweet
        self.tweets = {}

    def extract_paraphrases(self):
        pass

    def get_tweet(self, _id):
        return self.tweets[_id]

    def get_id(self, tweet):
        for key, value in self.tweets.items():
            if value == tweet:
                return key

    def add_tweet(self, _id, tweet):
        if _id not in self.tweets:
            self.tweets[_id] = tweet

    def filter_all_tweets(self, *args):
        pass

    def add_tweets_from_file(self, file):
        # delete duplicates
        pass

    def load_corpus_from_file(self, file):
        pass

    def save_corpus_to_file(self, file):
        pass


