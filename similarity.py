def calculate_similarity(docs_list, threshold):
    ''' Calculate similarity of all possible pairs in list '''
    results = list()
    all_combinations = list(itertools.combinations(docs_list, 2))
    for combination in all_combinations:
        score = combination[0].similarity(combination[1])
        if score > threshold:
            results.append((combination[0].text, combination[1].text))
    return results


def group_similarity(dictionary, threshold):
    ''' Group tweets by similarity '''
    print("Calculating similarities in tweets...")
    results = {}
    for key, docs_list in dictionary.items():
        score, paraphrases = calculate_similarity(docs_list)
        if score > threshold:
            results[key] += paraphrases
    return results
