#from textblob import TextBlob
from langdetect import detect
from os import listdir, path
import json
import csv


""" Build a cleaned, monolingual corpus iteratively """


def corpus_size(ouput_directory):
    ''' Calculate corpus size '''
    counter = 0
    files_list = listdir(ouput_directory)
    files_counter = len(files_list)
    for filename in files_list:
        if filename != "tracker.json":
            path = ouput_directory + filename
            files_counter -= 1
            with open(path, 'r') as f:
                for tweet in csv.reader(f):
                    counter += 1
    return counter


def load_tracker(output_directory):
    ''' Load tracker with filenames processed '''
    path = output_directory + "tracker.json"
    try:
        with open(path, 'r') as f:
            return json.loads(f.read())
    except:
        with open(path, 'w') as f:
            return dict()


def save_tracker(output_directory, tracker):
    ''' Save tracker with filenames processed '''
    path = output_directory + "tracker.json"
    with open(path, 'w') as f:
        json.dump(tracker, f)


def get_ouput_filenames(filename):
    root = path.splitext(filename)[0]
    output = root + ".csv"
    output_foreign = root + "_foreign.csv"
    return output, output_foreign


def extract_id_text(tweet):
    if "retweeted_status" in tweet and "extended_tweet" in tweet["retweeted_status"]:
        return tweet["id"], tweet["retweeted_status"]["extended_tweet"]["full_text"]
    else:
        return tweet["id"], tweet["text"]



def create_corpus(input_directory, output_directory, language):
    tracker = load_tracker(output_directory)

    for filename in listdir(input_directory):
        print(f"Extracting tweets from {filename}")
        if filename not in tracker:
            tracker[filename] = None
            filepath = input_directory + filename

            # Input files
            with open(filepath, 'r') as input_file:
                output_filename, output_filename_foreign = get_ouput_filenames(filename)
                output_filename_path = output_directory + output_filename
                output_filename_foreign_path = output_directory + output_filename_foreign

                # Output files
                with open(output_filename_path, 'w') as output_file:
                    output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Output foreign
                    with open(output_filename_foreign_path, 'w') as output_file_foreign:
                        output_writer_foreign = csv.writer(output_file_foreign, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                        output_writer.writerow(['id', 'tweet'])
                        output_writer_foreign.writerow(['id', 'tweet'])

                        for line in input_file:
                            #data =json.loads(line)
                            #print(json.dumps(data))
                            _id, text = extract_id_text(json.loads(line))
                            #print(text)
                            try:
                                if detect(text) == language:

                                    output_writer.writerow([_id, text])
                                else:
                                    output_writer_foreign.writerow([_id, text])
                            except:
                                print(text)

        save_tracker(output_directory, tracker)
    print("Process finished")



if __name__ == "__main__":
    original_corpus = "/home/samuel/Documents/Classes/research_and_development/twitter-corpus/"
    final_corpus = "/home/samuel/Documents/Classes/research_and_development/final_corpus/"
    create_corpus(original_corpus, final_corpus, "es")
    print(f"The corpus has {corpus_size(final_corpus)} tweets")
