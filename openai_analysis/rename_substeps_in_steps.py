import os


def rename_files_in_dir(dirpath):
    # Rename *_substeps_*.json files in a given directory
    for filename in os.listdir(dirpath):
        if "_substeps_" in filename and filename.endswith(".json"):
            old_path = os.path.join(dirpath, filename)
            new_name = filename.replace("_substeps_", "_step_")  # TODO:Change this
            new_path = os.path.join(dirpath, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed file: {old_path} -> {new_path}")


def rename_files_and_dirs(root_dir):
    # Walk through directory
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Check directories ending with "_substeps"
        for dirname in dirnames:
            if dirname.endswith("_substeps"):
                dir_full_path = os.path.join(dirpath, dirname)

                # Rename files inside the directory
                rename_files_in_dir(dir_full_path)

                # Rename the directory itself
                new_name = dirname.replace("_substeps", "_steps")
                new_path = os.path.join(dirpath, new_name)
                os.rename(dir_full_path, new_path)
                print(f"Renamed directory: {dir_full_path} -> {new_path}")


if __name__ == "__main__":
    directory_to_scan = "../dataset_writeups"
    rename_files_and_dirs(directory_to_scan)
