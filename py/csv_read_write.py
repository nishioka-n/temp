import csv
import json
import os
from datetime import datetime
from pprint import pprint

input_filename = "csv_read.csv"
encoding = "utf-8" # "utf-8" | "ms932"


def get_time_string() -> str:
    return datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')


def get_dicts_from_csv(input_filename):
    csv_file = open(input_filename, "r", encoding=encoding, errors="", newline="")

    # f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    dr = csv.DictReader(csv_file)
    header = dr.fieldnames
    rows = []
    for row in dr:  # row : dictionary
        rows.append(row)
        #  print(json.dumps(row, ensure_ascii=False, indent=2))

    return header, rows


def write_dics_to_csv(output_filename, header, rows):

    with open(output_filename, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def make_output_filename(input_filename):
    basename, ext = os.path.splitext(input_filename)
    ts = get_time_string()
    return f'{basename}_{ts}{ext}'


def update_rows(rows):
    for row in rows:
        # row[""] = ""
        pass


def main():
    header, rows = get_dicts_from_csv(input_filename)
    update_rows(rows)
    output_filename = make_output_filename(input_filename)
    write_dics_to_csv(output_filename, header, rows)

if __name__ == '__main__':
    main()