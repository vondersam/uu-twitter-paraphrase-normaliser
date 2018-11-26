from itertools import combinations

def calculate_similarity(docs_list, threshold):
    ''' Calculate similarity of all possible pairs in list '''
    results = list()

    # Get all possible combinations of tweets that have same NER
    all_combinations = list(combinations(docs_list, 2))

    # Calculate vector similarity of every combination
    for combination in all_combinations:
        score = combination[0].similarity(combination[1])

        # Only return those results above the threshold
        if score > threshold and combination[0].text != combination[1].text:
            if (combination[0].text, combination[1].text) not in results:
                results.append((combination[0].text, combination[1].text))
    return results


