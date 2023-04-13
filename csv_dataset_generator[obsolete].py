import csv
import os

from settings import NEW_LABELS
from settings import DATASET_DIRPATH, DATASET_TXT_SUFFIXES
from settings import CSV_FILENAME, CSV_HEADER_OBSOLETE
from settings import DATASET_CATEGORY


def read_clean_file(in_filepath):
    with open(in_filepath, "r", encoding="utf-8") as input_f:
        file_lines = []
        for line in input_f:
            # skip lines containing just whitespace characters
            if line.isspace():
                continue
            # skip newline characters
            if line == "\n":
                continue
            # skip empty lines
            if not line.strip():
                continue
            # skip code lines
            if line.strip() == "```":
                continue
            else:
                # strip() to remove any leading or trailing whitespace characters
                file_lines.append(line.strip())
        return file_lines


def csv_row_write(filename, topic, text, category=DATASET_CATEGORY):
    data_row = [filename, category, topic, text]
    writer.writerow(data_row)  # write the data to the CSV file


if __name__ == "__main__":
    csv_filepath = os.path.join(DATASET_DIRPATH, CSV_FILENAME)
    # open the CSV file in write mode
    with open(csv_filepath, "w", encoding="utf-8", newline="") as csvfile:
        # create a CSV writer object
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # write the header
        writer.writerow(CSV_HEADER_OBSOLETE)
        # loop through all directories and subdirectories
        for dirpath, dirnames, filenames in os.walk(DATASET_DIRPATH):
            # loop through all files in the directory
            for filename in filenames:
                # check if the file is a text file
                if filename.endswith(DATASET_TXT_SUFFIXES[2]):
                    in_filepath = os.path.join(dirpath, filename)
                    file_lines = read_clean_file(in_filepath)
                    section_text = ""
                    section_start = False
                    good_file = False
                    topic_states = {"current": -1, "next": -1}
                    for line_number, line in enumerate(file_lines, start=1):
                        # last line
                        if line_number == len(file_lines):
                            if good_file:  # skip all wrong files
                                if section_start:
                                    section_text += line
                                else:
                                    section_text += " " + line
                                csv_row_write(filename=filename,
                                              topic=topic_states["current"], text=section_text)
                        # section's first line
                        elif line in NEW_LABELS:
                            good_file = True
                            section_start = True
                            if not section_text:  # if section_text is empty
                                topic_states["current"] = line.split(
                                    "#")[1]  # TOPICS.index(line)
                            else:
                                topic_states["next"] = line.split(
                                    "#")[1]  # TOPICS.index(line)
                                csv_row_write(filename=filename,
                                              topic=topic_states["current"], text=section_text)
                                topic_states["current"] = topic_states["next"]
                                section_text = ""
                        # section's in-between line or untagged line
                        else:
                            # skip all first untagged lines
                            if topic_states["current"] != -1:
                                if section_start:
                                    section_text += line
                                else:
                                    section_text += " " + line
                                section_start = False
        print(f"CSV file: {csv_filepath}")
