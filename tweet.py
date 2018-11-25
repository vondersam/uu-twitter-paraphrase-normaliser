import spacy
import re
import emoji

nlp = spacy.load('es_core_news_md')


class Tweet:
    def __init__(self, text):
        self.raw_text = text
        self.clean_text = None
        self.doc = None


    def filter(self, *args):
        """ Apply optional filters 'retweets', 'emoticons', 'handles', 'urls', 'hashtags' and '*' """
        exps = []

        if "retweets" in args:
            exps.append(re.compile("^RT ?(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+):"))
        if "emoticons" in args:
            exps.append("emoticons")
        if "handles" in args:
            exps.append(re.compile("(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+)"))
        if "urls" in args:
            exps.append(re.compile("(https?|ftp)://[^\s/$.?#].[^\s]*"))
        if "hashtags" in args:
            exps.append(re.compile("(?<=^|(?<=[^a-zA-Z0-9-\.À-ÿ\u00f1\u00d1]))#([A-Za-z]+[A-Za-z0-9-À-ÿ\u00f1\u00d1]+)"))

        # Use all filters
        if "*" in args and not exps:
            return self.filter("retweets", "emoticons", "handles", "urls", "hashtags")

        filtering_text = self.raw_text
        for expression in exps:
            if expression == "emoticons":
                filtering_text = ''.join(c for c in filtering_text if c not in emoji.UNICODE_EMOJI)
            else:
                filtering_text = re.sub(expression, "", filtering_text)

        # Remove extra spaces
        self.clean_text = re.sub(r"\s\s+", ' ', filtering_text.strip())
        return self.clean_text


    def spacyfy(self, *args):
        """ Create and saves a spacy doc of the tweet. Choose 'raw' or 'clean' """
        if "raw" in args:
            return nlp(self.raw_text)
        if "clean" in args:
            print(args)
            return self.filter(*args)
            #return nlp(self.filter(args))

# feature engineering
# time sleep








