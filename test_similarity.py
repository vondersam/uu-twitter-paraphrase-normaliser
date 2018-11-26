import spacy
import json
import itertools

nlp = spacy.load('es_core_news_md')

d = ["Mi madre", "Mi padre", "Mi hermano"]
t = []
for i in d:
    t.append(nlp(i))

results = list(itertools.combinations(t, 2))
for i in results:
    print("RESULT:")
    print(i, i[0].similarity(i[1]))




