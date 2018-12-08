from corpus import Corpus
from file_separator import filter_separate

# Complete corpus
corpus = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/original_twitter_corpus/"
# Corpus MD
#corpus = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/test_delete_md/"
final_corpus = "/Users/samuelrodriguezmedina/Documents/classes/research_and_development/uu-twitter-paraphrase-normaliser/experiment1/"
c = Corpus()
c.create_corpus(corpus, final_corpus, 'es')
c.group_by_entity(final_corpus)
c.extract_paraphrases(final_corpus, "jaccard", 0.001)
filter_separate(final_corpus)
