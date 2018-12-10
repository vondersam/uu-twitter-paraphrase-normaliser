from itertools import combinations
from nltk import jaccard_distance, word_tokenize
import sys
from tweet import Tweet


def calculate_similarity(docs_list, similarity_type, threshold):
    ''' Calculate vector similarity of all possible pairs in list '''
    results = list()

    # Get all possible combinations of tweets that have same NER
    all_combinations = list(combinations(docs_list, 2))

    # Calculate vector similarity of every combination
    for combination in all_combinations:
        text1 = combination[0].strip()
        text2 = combination[1].strip()

        # Filter out pairs with exact sentences
        if text1 != text2:

            # Filter out sentences shorter than 4 words
            if len(combination[0].split()) > 3 and len(text2) > 3:

                # Filter out those combinations with excesive word number differences
                if abs(len(text1) - len(text2)) < 4:

                    # Only return those results above the threshold
                    settext1 = set(word_tokenize(text1))
                    settext2 = set(word_tokenize(text2))
                    if jaccard_distance(settext1, settext2) < threshold:

                        # Put in source sentences with more oov words
                        if Tweet(combination[0]).oov_words() > Tweet(combination[1]).oov_words():
                            bi_combination = combination[0], combination[1]
                        else:
                            bi_combination = combination[1], combination[0]

                        if bi_combination not in results:
                            results.append(bi_combination)

    sys.stdout.write(f"\rAdding combinations...")
    sys.stdout.flush()
    return results
