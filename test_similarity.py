#import spacy
#import json
#import itertools
from nltk import jaccard_distance, word_tokenize


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
sentences = [
("Aurah : “ Ves a Miriam bipolar ? ” Verdeliss : “ Las enfermedades mentales las tiene que diagnosticar un profesional , no yo , …", "Aurah : “ Ves a Miriam bipolar ? ” Verdeliss : “ Las enfermedades mentales las tiene que diagnosticar un profesional , no yo , así que no ” Aurah hija , te cubres de gloria"),
("Esta frase es exacta", "Esta frase es exacta"),
("Esta amiga es muy parecida", "Esta frase es exacta"),
("Toa la vida pensando que se iba pa'rriba", "Toda la vida pensando que subía"),
("Lleva menos de una temporada y ya habla mejor que Bale","Lleva menos de una temporada en España y ya habla mejor que Bale"),
("Esta es completmanete random", "la vida nos lleva a pensar"),
("To lo que pasa en graná esta torcio", "Todo lo que pasa en Granada está torcido")
]

for i in sentences:
    text1 = set(word_tokenize(i[0]))
    text2 = set(word_tokenize(i[1]))
    score = jaccard_distance(text1, text2)
    print(i[0])
    print(i[1])
    print(score)
    print(score < 0.5)
    print()


