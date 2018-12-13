from nltk import ngrams, jaccard_distance, distance
import difflib

sents = [
("En esta frase hay un herror que quiero borrar para que no aparezca no si te apetece",
    "En aquella frase hay un error que puedes pensar que está mal no si te apetece eso eso")
]


def extract_jaccard_ngrams(a, b, threshold, ngram_num):
    """ Extracts similar all similar ngrams with jaccard distance below a threshold
        Threshold adapts to ngrams since jaccard penalises short shorter ngrams
        Extracts the longest ngrams first for more context
    """
    new_thres = threshold / (ngram_num * .1)
    result = {}
    for n in reversed(range(2, ngram_num + 1)):
        ngrams_a, ngrams_b = list(ngrams(a.split(), n)), list(ngrams(b.split(), n))

        for ngram_a in ngrams_a:
            temp_list = []
            joint_a = " ".join(ngram_a)
            set_a = set(joint_a)

            for ngram_b in ngrams_b:
                joint_b = " ".join(ngram_b)
                set_b = set(joint_b)

                distance = jaccard_distance(set_a, set_b)
                temp_list.append((distance, joint_a, joint_b))

            min_score = min(temp_list, key = lambda t : t[0])
            if min_score[0] < new_thres and min_score[0] != 0:
                # order best sentence in second
                ja, jb = min_score[1], min_score[2]
                result[ja] = jb
                a, b = a.replace(ja, "").strip(), b.replace(jb, "").strip()

    return result




print(extract_jaccard_ngrams(sentA, sentB, 0.08, 5))
# (0.2 * 8) 0.16, 0.14, 0.12
# (0.1 / 8) 0.25, 0.28, 0.28571428571428575

'''
    sent_ngram = ngrams(sentA.split(), n)
    sent_ngram = ngrams(sentB.split(), n)

        ngram_order
        if jaccard_distance(ngramA, ngramB)
        paraphrases.
'''


'''
print("word level")
error = set(('ha', 'urn', 'herror'))
correct = set(('hay', 'un', 'error'))
d = jaccard_distance(error, correct)
print(d)

print("character level")
error = set('ha urn herror')
correct = set('hay un error')
d = jaccard_distance(error, correct)
print(d)

a = "Dos erores aqu"
b = "Dos errores aquí"
f = "Dos errores aquí"
c = "erores aqu esta es una frase mucho más larga con dos "
d = "errores aquí esta es una frase mucho más larga con dos "

print("Jaccard")
print(jaccard_distance(set(a), set(b)))
print(jaccard_distance(set(c), set(d)))
print(jaccard_distance(set(b), set(f)))
print("Jaro")
print(1-distance.jaro_winkler_similarity(a, b))
print(1-distance.jaro_winkler_similarity(b, c))
print(1-distance.jaro_winkler_similarity(b, f))

'''
