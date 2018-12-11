import spacy
import re
import emoji
from nltk.tokenize import TweetTokenizer
import aspell

s = aspell.Speller('lang', 'es')
nlp = spacy.load('es_core_news_md')
tokenize = nlp.tokenizer


class Tweet:
    def __init__(self, text):
        self.raw_text = text
        self.clean_text = None
        self.doc = None


    def filter(self, *args):
        """ Apply optional filters 'retweets', 'emoticons', 'handles', 'urls', 'hashtags' and '*' """
        exps = []

        #this ones can be improved. some are not getting extracted
        if "retweets" in args:
            exps.append(re.compile("^RT ?(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+):"))
        if "emoticons" in args:
            exps.append("emoticons")
        if "flags" in args:
            exps.append(re.compile(u"[\U0001F1E6-\U0001F1FF]"))
        if "handles" in args:
            # Handles at start of string
            exps.append(re.compile("^\s*((?<=^|(?<=[^\S]))@([\S]+)\s*)*"))
            # Handles at end of string
            exps.append(re.compile("\s+((?<=^|(?<=[^\S]))@(\S+)\s*)*$"))
        if "urls" in args:
            exps.append(re.compile("(https?|ftp)://[^\s/$.?#].[^\s]*"))
        if "hashtags" in args:
            # Hastags at start of string
            exps.append(re.compile("^\s*((?<=^|(?<=[^\S]))#([\S]+)\s*)*"))
            # Hashtags at end of string
            exps.append(re.compile("\s+((?<=^|(?<=[^\S]))#(\S+)\s*)*$"))

        # Use all filters
        if "*" in args and not exps:
            return self.filter("retweets", "emoticons", "flags", "handles", "urls", "hashtags")

        filtering_text = self.raw_text
        for expression in exps:
            if expression == "emoticons":
                filtering_text = ''.join(c for c in filtering_text if c not in emoji.UNICODE_EMOJI)
            else:
                filtering_text = re.sub(expression, "", filtering_text)

        # Remove extra spaces
        self.clean_text = re.sub(r"\s\s+", ' ', filtering_text.strip())
        return self.clean_text


    def tokenize(self):
        try:
            tokens = TweetTokenizer().tokenize(self.clean_text)
            return " ".join(tokens)
        except Exception as e:
            print(e)
            print("Cannot tokenize text")


    def spacyfy(self, *args):
        """ Create and saves a spacy doc of the tweet. Choose 'raw' or 'clean' """
        if "raw" in args:
            return nlp(self.raw_text)
        if "clean" in args:
            return nlp(self.filter(*args))

    def oov_words(self):
        """ Return number of out of vocabulary words of the tweet """
        oov = int()
        for word in self.clean_text.split():
            if not s.check(word):
                oov += 1
        return oov

    def tweet_len(self):
        return len(self.clean_text.split())

    def target_filter(self):
        exps = []
        exps.append(re.compile(r"(ja|JA)(?=.*\1)"))
        exps.append(re.compile(r"(\¡)(?=.*\1)"))
        exps.append(re.compile(r"(\!)(?=.*\1)"))
        exps.append(re.compile(r"(\¿)(?=.*\1)"))
        exps.append(re.compile(r"(\?)(?=.*\1)"))
        exps.append(re.compile(r"([aeiouAEIOU])\1{1,}(?=[aeiouAEIOU].*\1)"))

        filtering_text = self.clean_text
        for expression in exps:
            filtering_text = re.sub(expression, "", filtering_text)

        tokens = TweetTokenizer().tokenize(filtering_text)
        return " ".join(tokens).strip(".")

    def source_filter(self):
        tokens = TweetTokenizer().tokenize(self.clean_text)
        return " ".join(tokens).strip(".")

    def word_set(self):
        tokens = TweetTokenizer().tokenize(self.clean_text)
        return set(tokens)



