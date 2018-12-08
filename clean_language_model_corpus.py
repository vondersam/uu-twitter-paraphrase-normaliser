import os
import re
from nltk.tokenize import TweetTokenizer



input_fol = "/Users/samuelrodriguezmedina/Downloads/raw.es/"
output_fol = "/Users/samuelrodriguezmedina/Documents/classes/research_and_development/language_model_corpus/"

def clean(input_folder, output_folder):
    list_files = os.listdir(input_folder)
    counter = len(list_files)
    total = counter
    for file in list_files:
        file_in = input_folder + file
        file_out = output_folder + file
        with open(file_in, encoding='windows-1252') as fi:
            print(f"Cleaning {counter} of {total}")
            with open(file_out, 'w') as fo:
                data = fi.readlines()
                for line in data:
                    if not line.startswith("<"):
                        if not re.match(r'^\s*$', line):
                            if not line.startswith("ENDOFARTICLE."):
                                try:
                                    tokens = TweetTokenizer().tokenize(line)
                                    fo.write(" ".join(tokens) + "\n")
                                except Exception as e:
                                    print(e)
        counter -= 1

clean(input_fol, output_fol)
