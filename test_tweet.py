from tweet import Tweet
from corpus import Corpus

c = Corpus()
print(c)
print("Corpus created correctly")



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
