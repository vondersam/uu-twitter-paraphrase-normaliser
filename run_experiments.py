from corpus import Corpus
import time
from clean_corpus import corpus_size


# Complete corpus
corpus = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/original_twitter_corpus/"
# Corpus MD
#corpus = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/test_delete_sm/"
final_corpus = "/Users/samuelrodriguezmedina/Documents/classes/research_and_development/uu-twitter-paraphrase-normaliser/new_experiments/"

experiments = ["levenshtein"]
jaccard = [0.5, 0.2]
jaro_winkler = [0.05]
levenshtein = [9, 7, 15, 17]

c = Corpus()
print(c.count(corpus))

'''
c.create_corpus(corpus, final_corpus, 'es')
c.group_by_entity(final_corpus)

def run_experiment(experiment, threshold):
    print(f"{experiment} distance with a {threshold} threshold.")
    start = time.time()
    output_file =  f"{final_corpus}{experiment}_{str(threshold)}_"
    c.extract_paraphrases(final_corpus, output_file, experiment, threshold)
    end = time.time()
    print(f"Done. It took {end - start} to extract the paraphrases.")
    print()

for experiment in experiments:
    if experiment == "jaccard":
        for threshold in jaccard:
            run_experiment(experiment, threshold)

    if experiment == "jaro_winkler":
        for threshold in jaro_winkler:
            run_experiment(experiment, threshold)

    if experiment == "levenshtein":
        for threshold in levenshtein:
            run_experiment(experiment, threshold)

print("The final corpus has these tweets:")
results = corpus_size(final_corpus + "corpus/")
print(results)
'''

# Test MD with normal similarity
# 19
# Test MD with ngram similarity char
#  309.88223695755005 (5 minutes)
# MD ngram similarity word
# 301.5850930213928
