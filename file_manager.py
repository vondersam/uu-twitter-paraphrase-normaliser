from os import path, makedirs
import json

def load_tracker(output_dir, subdir, name):
    ''' Load tracker with filenames processed '''
    # Create output_dir if not exist
    directory = output_dir + f"/{subdir}/"
    if not path.exists(directory):
        makedirs(output_dir)

    filepath = directory + name
    try:
        with open(filepath, 'r') as f:
            return json.loads(f.read())
    except:
        with open(filepath, 'w') as f:
            return {}


def save_tracker(output_dir, subdir, name, tracker):
    ''' Save tracker with filenames processed '''
    filepath = output_dir + f"{name}"
    with open(filepath, 'w') as f
        json.dump(tracker, f)


def get_ouput_filenames(filename):
    ''' Create output filenames '''
    root = path.splitext(filename)[0]
    output = root + ".csv"
    output_foreign = root + "_foreign.csv"
    return output, output_foreign
