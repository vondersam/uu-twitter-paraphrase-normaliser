import json

def filter_separate(input_dir):
    file_path = input_dir + "paraphrases.json"
    output_file_a = input_dir + "source.txt"
    output_file_b = input_dir + "target.txt"
    with open(file_path) as f:
        data = json.load(f)
        with open(output_file_a, 'w') as a, open(output_file_b, 'w') as b:
            for source, target in data.items():
                a.write(source + "\n")
                b.write(target + "\n")



