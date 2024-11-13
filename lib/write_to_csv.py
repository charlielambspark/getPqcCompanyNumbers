import csv

from lib.constants import SUBTYPE_TO_LABEL

def write_to_csv(data, output_path):
    headers = [SUBTYPE_TO_LABEL[key] for key in SUBTYPE_TO_LABEL.keys()]
    keys = list(data.keys())
    max_length = max(len(values) for values in data.values())

    for key, values in data.items():
        if len(values) < max_length:
            data[key] += [None] * (max_length - len(values))

    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for i in range(max_length):
            row = [data[key][i] for key in keys]
            writer.writerow(row)
        csvfile.close()
