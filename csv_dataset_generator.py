import csv
import os
import unicodedata
import chardet

from settings import DATASET_DIRPATH, DATASET_TXT_SUFFIXES
from settings import CSV_FILENAME, CSV_HEADER
from settings import DATASET_CATEGORY


def normalize_file(in_filepath):
    # open the file in binary mode and read its content
    with open(in_filepath, "rb") as input_f:
        content = input_f.read()
    # detect the file's encoding
    encoding = chardet.detect(content)["encoding"]
    # decode the contents of the file using the detected encoding
    decoded_content = content.decode(encoding)
    # normalize the text by replacing non-ASCII characters with their closest ASCII equivalent
    normalized_content = unicodedata.normalize(
        'NFKD', decoded_content).encode("ascii", "ignore").decode("utf-8")
    # write the normalized contents back to the file
    with open(in_filepath, "wb") as output_f:
        output_f.write(normalized_content.encode("utf-8"))

def read_file(in_filepath):
    with open(in_filepath, "r", encoding="utf-8") as input_f:
        file_content = input_f.read()
    return file_content

def csv_row_write(filename, text, category=DATASET_CATEGORY):
    data_row = [filename, category, text]
    # write the data to the CSV file
    writer.writerow(data_row)


if __name__ == "__main__":
    csv_filepath = os.path.join(DATASET_DIRPATH, CSV_FILENAME)
    # open the CSV file in write mode
    with open(csv_filepath, "w", encoding="utf-8", newline="") as csvfile:
        # create a CSV writer object
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # write the header
        writer.writerow(CSV_HEADER)
        # loop through all directories and subdirectories
        for dirpath, dirnames, filenames in os.walk(DATASET_DIRPATH):
            # loop through all files in the directory
            for filename in filenames:
                # check if the file is a text (tagged) file
                if filename.endswith(DATASET_TXT_SUFFIXES[2]):
                    in_filepath = os.path.join(dirpath, filename)
                    normalize_file(in_filepath)
                    file_content = read_file(in_filepath)
                    csv_row_write(filename=filename, text=file_content)
        print(f"CSV file: {csv_filepath}")
