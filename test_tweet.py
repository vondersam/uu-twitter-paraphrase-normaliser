from corpus import Corpus
import time
from clean_corpus import corpus_size


# Complete corpus
#corpus = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/original_twitter_corpus/"
# Corpus MD
corpus = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/test_delete_md/"
final_corpus = "/Users/samuelrodriguezmedina/Documents/classes/research_and_development/uu-twitter-paraphrase-normaliser/experiment_md/"


c = Corpus()
c.create_corpus(corpus, final_corpus, 'es')
c.group_by_entity(final_corpus)

start = time.time()
c.extract_paraphrases(final_corpus, "jaccard", 0.5)
end = time.time()
print(f"It took {end - start} to extract the paraphrases")


#results = corpus_size("/Users/samuelrodriguezmedina/Documents/classes/research_and_development/uu-twitter-paraphrase-normaliser/experiment_final/corpus/")
#print(results)
# Test MD with normal similarity
# 19
# Test MD with ngram similarity
#
