from langdetect import detect
import json
import csv
from file_manager import load_tracker, save_tracker, get_ouput_filenames
from os import listdir, path, makedirs

""" Build a cleaned, monolingual corpus iteratively """

def corpus_size(ouput_dir):
    ''' Calculate number of tweets in a directory '''
    print("Calculating the size of the corpus...")
    counter = 0
    files_list = listdir(ouput_dir)
    files_counter = len(files_list)
    for filename in files_list:
        if filename != "tracker.json":
            path = ouput_dir + filename
            files_counter -= 1
            with open(path, 'r') as f:
                for tweet in csv.reader(f):
                    counter += 1
    return counter


def extract_id_text(tweet):
    ''' Extract text and id from tweets '''
    if "retweeted_status" in tweet and "extended_tweet" in tweet["retweeted_status"]:
        return tweet["id"], tweet["retweeted_status"]["extended_tweet"]["full_text"]
    elif "extended_tweet" in tweet:
        return tweet["id"], tweet["extended_tweet"]["full_text"]
    else:
        return tweet["id"], tweet["text"]


def clean_corpus(input_dir, output_dir, language, foreign=False):
    ''' Separates corpora given a language '''
    tracker = load_tracker(output_dir, "cleaning", "tracker.json")
    inv_tracker = load_tracker(output_dir, "cleaning", "inv_tracker.json")

    for filename in listdir(input_dir):
        if filename not in tracker and filename.endswith(".json"):
            print(f"Extracting tweets from {filename}")
            unique_tweets = {}
            filepath = input_dir + filename

            # Input files
            with open(filepath, 'r') as input_file:
                output_filename, output_filename_foreign = get_ouput_filenames(filename)

                # Output directory
                corpus_directory = output_dir + "/corpus/"
                if not path.exists(corpus_directory):
                    makedirs(corpus_directory)
                output_filename_path = corpus_directory + output_filename
                output_filename_foreign_path = corpus_directory + output_filename_foreign

                # Output files
                with open(output_filename_path, 'w') as output_file:
                    output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    output_writer.writerow(['id', 'tweet'])

                    # Output foreign
                    if foreign:
                        output_file_foreign = open(output_filename_foreign_path, 'w')
                        output_writer_foreign = csv.writer(output_file_foreign, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        output_writer_foreign.writerow(['id', 'tweet'])

                    for line in input_file:
                        _id, text = extract_id_text(json.loads(line))
                        try:
                            if detect(text) == language:
                                # Filter duplicates and save language output
                                if text not in unique_tweets:
                                    unique_tweets[text] = None
                                    output_writer.writerow([_id, text])
                                    tracker[filename] = None
                                    inv_tracker[_id] = output_filename

                            else:
                                # Write foreign text to another file
                                if foreign:
                                    output_writer_foreign.writerow([_id, text])
                        except:
                            print(text)
                    if foreign:
                        output_file_foreign.close()

        tracker[filename] = None
        save_tracker(output_dir, "cleaning", "tracker.json", tracker)
        save_tracker(output_dir, "cleaning", "inv_tracker.json", inv_tracker)
    print("All tweets extracted")
    return inv_tracker



if __name__ == "__main__":
    main()
