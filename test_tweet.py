from corpus import Corpus


original_corpus = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/original_twitter_corpus/"
final_corpus = "/Users/samuelrodriguezmedina/Documents/research/"
c = Corpus()
c.create_corpus(original_corpus, final_corpus, 'es')
c.group_by_entity(final_corpus)
c.extract_paraphrases(final_corpus, 0.99)
#c.extract_paraphrases(final_corpus, "jaccard", 0.20)



'''
t = Tweet("Maravilla de #españistán voz cada dia me gusta más Julia 😍😍 #Otdirecto26OCT https://t.co/ABog7JHrUL")
c.add_tweet(1055863313932926976,t)
print(c.tweets)
print(c.get_id(t))


print("Applying filters...")
print(t.filter("retweets"))
print(t.filter("emoticons"))
print(t.filter("handles"))
print(t.filter("urls"))
print(t.filter("hashtags"))
print(t.filter("*"))
print()
print("Applying Spacy...")
print(t.spacyfy("clean","hashtags"))
print(t.spacyfy("clean","handles"))
print(t.spacyfy("clean","urls"))
print(t.spacyfy("clean","*"))
'''
