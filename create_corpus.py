#from textblob import TextBlob
from langdetect import detect
from os import listdir, path
import json
import csv


""" Designed to build a cleaned, monolingual corpus iteratively """


def corpus_size(old_size, new_size):
    ''' Calculate corpus size '''
    pass


def load_previous_info(output_directory):
    ''' Load last size of corpus and files processed '''
    size = {"Corpus files": 0,
            "Corpus size": 0,
            "Number of tweets": 0,
             }
    info = []

    for filename in ["size.json", "tracker.json"]:
        path = output_directory + filename
        try:
            with open(path, 'r') as f:
                info.append(json.loads(f.read()))
        except:
            with open(path, 'w') as f:
                if filename == "size.json":
                    info.append(size)
                else:
                    info.append(dict())
    return info



def get_ouput_filenames(filename):
    root = path.splitext(filename)[0]
    output = root + ".csv"
    output_foreign = root + "_foreign.csv"
    return output, output_foreign


def save_previous_info(output_directory, size, tracker):
    ''' Save last size of corpus and files processed '''
    for filename in ["size.json", "tracker.json"]:
        path = output_directory + filename
        with open(path, 'w') as f:
            if filename == "size.json":
                json.dump(size, f)
            else:
                json.dump(tracker, f)


def create_corpus(input_directory, output_directory, language):
    size, tracker = load_previous_info(output_directory)

    for filename in listdir(input_directory):
        print(f"Extracting tweets from {filename}")
        if filename not in tracker:
            tracker[filename] = None
            filepath = input_directory + filename

            # Input
            with open(filepath, 'r') as input_file:
                output_filename, output_filename_foreign = get_ouput_filenames(filename)
                output_filename_path = output_directory + output_filename
                output_filename_foreign_path = output_directory + output_filename_foreign

                # Output
                with open(output_filename_path, 'w') as output_file:
                    output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Output foreign
                    with open(output_filename_foreign_path, 'w') as output_file_foreign:
                        output_writer_foreign = csv.writer(output_file_foreign, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                        output_writer.writerow(['id', 'tweet'])
                        output_writer_foreign.writerow(['id', 'tweet'])

                        for line in input_file:
                            data = json.loads(line)
                            if detect(data["text"]) == language:
                                output_writer.writerow([data["id"], data["text"]])
                                size["Number of tweets"] += 1
                            else:
                                output_writer_foreign.writerow([data["id"], data["text"]])
    save_previous_info(output_directory, size, tracker)
    print("Process finished")



if __name__ == "__main__":
    original_corpus = "/home/samuel/Documents/Classes/research_and_development/twitter-corpus-test/"
    final_corpus = "/home/samuel/Documents/Classes/research_and_development/final_corpus/"
    create_corpus(original_corpus, final_corpus, "es")
