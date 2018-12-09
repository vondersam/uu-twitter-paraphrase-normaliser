from itertools import combinations
from nltk import jaccard_distance, word_tokenize
import sys


def calculate_similarity(docs_list, similarity_type, threshold):
    ''' Calculate vector similarity of all possible pairs in list '''
    results = list()

    # Get all possible combinations of tweets that have same NER
    all_combinations = list(combinations(docs_list, 2))
    len_combinations = len(all_combinations)
    counter = len_combinations

    # Calculate vector similarity of every combination
    for combination in all_combinations:
        if similarity_type == "vector":
            score = combination[0].similarity(combination[1])
        elif similarity_type == "jaccard":
            text1 = set(word_tokenize(combination[0]))
            text2 = set(word_tokenize(combination[1]))
            score = jaccard_distance(text1, text2)

        # Only return those results above the threshold
        if score > threshold and combination[0] != combination[1]:
            if (combination[0], combination[1]) not in results:
                results.append((combination[0], combination[1]))
        counter -= 1
        sys.stdout.write(f"Processed {counter} of {len_combinations}")
        sys.stdout.flush()
    return results
