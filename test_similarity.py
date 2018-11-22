import spacy
import json
import itertools

nlp = spacy.load('es_core_news_md')

output_path = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/grouped_ner/grouped_entities.json"
with open(output_path) as f:
    data = json.loads(f.read())
    result = data["('LOC', 'NuestraSeñoraDelRosario')"]

docs_list = []

#for tweet in result:
#    docs_list.append(nlp(tweet))

d = ["Mi madre", "Mi padre", "Mi hermano"]
t = []
for i in d:
    t.append(nlp(i))

results = list(itertools.combinations(t, 2))
for i in results:
    print("RESULT:")
    print(i, i[0].similarity(i[1]))




