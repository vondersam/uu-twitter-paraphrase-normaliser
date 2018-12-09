from itertools import combinations
from nltk import jaccard_distance, word_tokenize
import sys


def calculate_similarity(docs_list, similarity_type, threshold):
    ''' Calculate vector similarity of all possible pairs in list '''
    results = list()

    # Get all possible combinations of tweets that have same NER
    all_combinations = list(combinations(docs_list, 2))

    # Calculate vector similarity of every combination
    for combination in all_combinations:
        if combination[0] != combination[1]:
            text1 = set(word_tokenize(combination[0]))
            text2 = set(word_tokenize(combination[1]))

            if len(text1) > 3 and len(text2) > 3:
                # Only return those results above the threshold
                if jaccard_distance(text1, text2) < threshold:
                    if (combination[0], combination[1]) not in results:
                        results.append((combination[0], combination[1]))


    sys.stdout.write(f"\rAdding combinations...")
    sys.stdout.flush()
    return results
