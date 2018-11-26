from os import path, makedirs
import json

def load_tracker(output_dir, subdir):
    ''' Load tracker with filenames processed '''
    # Create output_dir if not exist
    if not path.exists(output_dir):
        makedirs(output_dir)

    tracker_path = output_dir + subdir + "/tracker.json"
    inv_tracker_path = output_dir + subdir + "inverted_tracker.json"
    try:
        with open(tracker_path, 'r') as f, open(inv_tracker_path, 'r') as inv_f:
            return json.loads(f.read()), json.loads(inv_f.read())
    except:
        with open(tracker_path, 'w') as f, open(inv_tracker_path, 'w') as inv_f:
            return {}, {}


def save_tracker(output_dir, tracker, inv_tracker, subdir):
    ''' Save tracker with filenames processed '''
    tracker_path = output_dir + subdir + "/tracker.json"
    inv_tracker_path = output_dir + subdir + "inverted_tracker.json"
    with open(tracker_path, 'w') as f, open(inv_tracker_path, 'w') as inv_f:
        json.dump(tracker, f)
        json.dump(inv_tracker, inv_f)


def get_ouput_filenames(filename):
    ''' Create output filenames '''
    root = path.splitext(filename)[0]
    output = root + ".csv"
    output_foreign = root + "_foreign.csv"
    return output, output_foreign
