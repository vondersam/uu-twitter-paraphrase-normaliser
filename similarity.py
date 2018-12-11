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
    for tweet_pair in all_combinations:
        tweet_pair[0].filter("*")
        tweet_pair[1].filter("*")

        # Filter out pairs with exact sentences
        if tweet_pair[0].clean_text != tweet_pair[1].clean_text:

            # Filter out sentences shorter than 4 words
            if tweet_pair[0].tweet_len() > 3 and tweet_pair[1].tweet_len() > 3:

                # Filter out those combinations with excesive word number differences
                if abs(tweet_pair[0].tweet_len() - tweet_pair[1].tweet_len()) < 4:

                    # Only return those results above the threshold
                    settext1 = tweet_pair[0].word_set()
                    settext2 = tweet_pair[1].word_set()
                    if jaccard_distance(settext1, settext2) < threshold:

                        # Put in source sentences with more oov words and extra filter target
                        if tweet_pair[0].oov_words() > tweet_pair[1].oov_words():
                            bi_combination = tweet_pair[0].source_filter(), tweet_pair[1].target_filter()
                        else:
                            bi_combination = tweet_pair[1].source_filter(), tweet_pair[0].target_filter()

                        if bi_combination not in results:
                            results.append(bi_combination)

    sys.stdout.write(f"\rAdding combinations...")
    sys.stdout.flush()
    return results
