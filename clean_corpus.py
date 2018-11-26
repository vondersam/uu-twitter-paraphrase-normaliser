from langdetect import detect
from os import listdir, path, makedirs
import json
import csv

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


def load_tracker(output_dir):
    ''' Load tracker with filenames processed '''
    # Create output_dir if not exist
    if not path.exists(output_dir):
        makedirs(output_dir)

    tracker = output_dir + "tracker.json"
    inv_tracker = output_dir + "inverted_tracker.json"
    try:
        with open(tracker, 'r') as f, open(inv_tracker, 'r') as inv_f:
            return json.loads(f.read()), json.loads(inv_f.read())
    except:
        with open(tracker, 'w') as f, open(inv_tracker, 'w') as inv_f:
            return {}, {}


def save_tracker(output_dir, tracker, inv_tracker):
    ''' Save tracker with filenames processed '''
    tracker_p = output_dir + "tracker.json"
    inv_tracker_p = output_dir + "inverted_tracker.json"
    with open(tracker_p, 'w') as f, open(inv_tracker_p, 'w') as inv_f:
        json.dump(tracker, f)
        json.dump(inv_tracker, inv_f)


def get_ouput_filenames(filename):
    ''' Create output filenames '''
    root = path.splitext(filename)[0]
    output = root + ".csv"
    output_foreign = root + "_foreign.csv"
    return output, output_foreign


def extract_id_text(tweet):
    ''' Extract text and id from tweets '''
    if "retweeted_status" in tweet and "extended_tweet" in tweet["retweeted_status"]:
        return tweet["id"], tweet["retweeted_status"]["extended_tweet"]["full_text"]
    else:
        return tweet["id"], tweet["text"]


def clean_corpus(input_dir, output_dir, language, foreign=False):
    ''' Separates corpora given a language '''
    #WE MIGH WANT TO CHANGE THE FORMAT OF OUTPUT TO JSON SINCE ITS FASTER TO EXTRACT TWEETS BY ID
    tracker, inv_tracker = load_tracker(output_dir)

    for filename in listdir(input_dir):
        print(f"Extracting tweets from {filename}")
        if filename not in tracker:
            tracker[filename] = []
            filepath = input_dir + filename

            # Input files
            with open(filepath, 'r') as input_file:
                output_filename, output_filename_foreign = get_ouput_filenames(filename)
                output_filename_path = output_dir + output_filename
                output_filename_foreign_path = output_dir + output_filename_foreign

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
                                if _id not in inv_tracker:
                                    output_writer.writerow([_id, text])
                                    tracker[filename].append(_id)
                                    inv_tracker[_id] = output_filename


                            else:
                                # Save foreign
                                if foreign:
                                    output_writer_foreign.writerow([_id, text])
                        except:
                            print(text)
                    if foreign:
                        output_file_foreign.close()

        save_tracker(output_dir, tracker, inv_tracker)
    print("Process finished")
    return inv_tracker



if __name__ == "__main__":
    main()
    #original_corpus = "/home/samuel/Documents/Classes/research_and_development/twitter-corpus/"
    #final_corpus = "/home/samuel/Documents/Classes/research_and_development/final_corpus/"
    #clean_corpus(original_corpus, final_corpus, "es")
    #print(f"The corpus has {corpus_size(final_corpus)} tweets")
