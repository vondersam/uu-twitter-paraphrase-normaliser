from itertools import combinations
from nltk import jaccard_distance
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


def calculate_similarity_ngram(docs_list, similarity_type, threshold):
    ''' Calculate vector similarity of all possible pairs in list '''
    results = {}

    # Get all possible combinations of tweets that have same NER
    all_combinations = list(combinations(docs_list, 2))

    # Calculate vector similarity of every combination
    for tweet_pair in all_combinations:
        tweet1 = tweet_pair[0]
        tweet2 = tweet_pair[1]
        tweet1.filter("*")
        tweet2.filter("*")

        # Filter out pairs with exact sentences
        if tweet1.clean_text != tweet2.clean_text:

            # Filter out sentences shorter than 4 words
            if tweet1.tweet_len() > 3 and tweet2.tweet_len() > 3:
                ngram_results = extract_jaccard_ngrams(tweet1, tweet2, 0.03, 5)

                # Merge dictionaries
                results = {**results, **ngram_results}

    sys.stdout.write(f"\rAdding combinations...")
    sys.stdout.flush()
    return list(results.items())


def extract_jaccard_ngrams(tweet1, tweet2, threshold, ngram_num):
    """ Extracts all similar ngrams with jaccard distance below a threshold
        Threshold adapts to ngrams since jaccard penalises short shorter ngrams
        Extracts the longest ngrams first for more context
    """
    new_thres = threshold / (ngram_num * .1)
    result = {}
    for n in reversed(range(2, ngram_num + 1)):
        ngrams_a, ngrams_b = tweet1.ngrams(n), tweet2.ngrams(n)

        for ngram_a in ngrams_a:
            temp_list = []
            joint_a = " ".join(ngram_a)
            set_a = set(joint_a)

            for ngram_b in ngrams_b:
                joint_b = " ".join(ngram_b)
                set_b = set(joint_b)

                distance = jaccard_distance(set_a, set_b)
                temp_list.append((distance, joint_a, joint_b))

            min_score = min(temp_list, key = lambda t:t[0], default=1)

            if min_score != 1:
                if min_score[0] < new_thres and min_score[0] != 0:

                    # order best sentence in second
                    joint_a = Tweet(min_score[1])
                    joint_b = Tweet(min_score[2])
                    joint_a.filter("*")
                    joint_b.filter("*")

                    if joint_a.oov_words() > joint_b.oov_words():
                        result[joint_a.source_filter()] = joint_b.target_filter()
                    else:
                        result[joint_b.source_filter()] = joint_a.target_filter()

                    tweet1.strip_out(joint_a.clean_text)
                    tweet2.strip_out(joint_b.clean_text)

    return result

