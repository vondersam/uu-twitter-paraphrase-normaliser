import spacy
import json
import itertools
from nltk import jaccard_distance

'''
nlp = spacy.load('es_core_news_md')

d = ["Mi madre", "Mi padre", "Mi hermano"]
t = []
for i in d:
    t.append(nlp(i))

results = list(itertools.combinations(t, 2))
for i in results:
    print("RESULT:")
    print(i, i[0].similarity(i[1]))
'''
sent1 = set("It might help to re-install Python if possible.")
sent2 = set("It can help to install Python again if possible.")
sent3 = set("It can be so helpful to reinstall C++ if possible.")
sent4 = set("help It possible Python to re-install if might.") # This has the same words as sent1 with a different order.
sent5 = set("I love Python programming.")

jd_sent_1_2 = jaccard_distance(sent1, sent2)
jd_sent_1_3 = jaccard_distance(sent1, sent3)
jd_sent_1_4 = jaccard_distance(sent1, sent4)
jd_sent_1_5 = jaccard_distance(sent1, sent5)


print(jd_sent_1_2, 'Jaccard Distance between sent1 and sent2')
print(jd_sent_1_3, 'Jaccard Distance between sent1 and sent3')
print(jd_sent_1_4, 'Jaccard Distance between sent1 and sent4')
print(jd_sent_1_5, 'Jaccard Distance between sent1 and sent5')



