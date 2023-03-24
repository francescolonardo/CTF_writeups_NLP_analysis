import os
import glob


WRITEUPS_DIRNAME = "./dataset_writeups/"
TXT_SUFFIXES = ["_original.txt", "_cleaned.txt", "_tagged.txt"]


# get a list of all "*_original.txt" files in the writeups directory
original_filenames = glob.glob(
    os.path.join(WRITEUPS_DIRNAME, "*_original.txt")
)

# iterate through the list of files
for original_filename in original_filenames:
    prefix_filename = original_filename.split(TXT_SUFFIXES[0])[0]
    # delete "*_cleaned.txt" and "*_tagged.txt" files
    cleaned_filename = prefix_filename + TXT_SUFFIXES[1]
    tagged_filename = prefix_filename + TXT_SUFFIXES[2]
    if os.path.exists(cleaned_filename):
        os.remove(cleaned_filename)
    if os.path.exists(tagged_filename):
        os.remove(tagged_filename)
    # revert the filename
    reverted_filename = original_filename.replace(TXT_SUFFIXES[0], ".txt")
    os.rename(original_filename, reverted_filename)
    print(f"Reverted {original_filename} to {reverted_filename}")
