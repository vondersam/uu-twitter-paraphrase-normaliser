from corpus import Corpus


original_corpus = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/original_twitter_corpus/"
final_corpus = "/Users/samuelrodriguezmedina/Documents/classes/research_and_development/uu-twitter-paraphrase-normaliser/experiment1/"
c = Corpus()
c.create_corpus(original_corpus, final_corpus, 'es')
c.group_by_entity(final_corpus)
c.extract_paraphrases(final_corpus, "jaccard", 0.001)
