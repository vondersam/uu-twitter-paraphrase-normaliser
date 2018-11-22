import json

input_path = "/Users/samuelrodriguezmedina/Google Drive/Language Technology/Research and Development/project/corpora/grouped_ner/grouped_entities.json"
with open(output_path) as f:
    data = json.loads(f.read())
