import os
import shutil


def rename_files_in_directory(directory):
    # Walking through directory and subdirectories
    for foldername, subfolders, filenames in os.walk(directory):
        # Iterating over all files in current directory/subdirectory
        for filename in filenames:
            # Checking if the file name ends with '_abstracted.json'
            if filename.endswith("_abstracted.json"):
                old_file_path = os.path.join(foldername, filename)

                # Constructing the new file name and path
                new_file_name = filename.replace("_abstracted.json", "_steps.json")
                new_file_path = os.path.join(foldername, new_file_name)

                # Renaming the file
                shutil.move(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")


# Specify the directory you want to start the search from
directory = "../dataset_writeups"

rename_files_in_directory(directory)
