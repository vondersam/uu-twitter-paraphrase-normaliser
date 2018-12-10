from os import path, makedirs
import json

def load_tracker(output_dir, subdir, name):
    ''' Load tracker with filenames processed '''
    # Create output_dir if not exist
    directory = output_dir + f"{subdir}_trackers/"
    if not path.exists(directory):
        makedirs(directory)

    filepath = directory + name
    try:
        with open(filepath, 'r') as f:
            return json.loads(f.read())
    except:
        with open(filepath, 'w') as f:
            return {}


def save_tracker(output_dir, subdir, name, tracker):
    ''' Save tracker with filenames processed '''
    filepath = output_dir + f"{subdir}_trackers/" + name
    with open(filepath, 'w') as f:
        json.dump(tracker, f)


def get_ouput_filenames(filename):
    ''' Create output filenames '''
    root = path.splitext(filename)[0]
    output = root + ".csv"
    output_foreign = root + "_foreign.csv"
    return output, output_foreign

def write_final_files(output_dir, paraphrases_results, name):
    ''' Write the final files in two different files '''
    directory = output_dir + "final_files/"
    if not path.exists(directory):
        makedirs(directory)
    filepath_src = directory + f"{name}_paraphrases.source"
    filepath_tgt = directory + f"{name}_paraphrases.target"

    with open(filepath_src, 'w') as s, open(filepath_tgt, 'w') as t:
        for result in paraphrases_results:
            for paraphrase_pair in result.get():
                s.write(paraphrase_pair[0] + "\n")
                t.write(paraphrase_pair[1] + "\n")
