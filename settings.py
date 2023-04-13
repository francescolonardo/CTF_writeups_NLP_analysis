OLD_LABELS = ["#overview", "# overview", "#analysis", "# analysis",
              "#attack execution", "# attack execution", "#attack_execution", "# attack_execution"]
NEW_LABELS = ["#context", "#discovery",
              "#exploitation", "#countermeasures", "#code"]

MODEL_ID = "gpt-3.5-turbo"
# more contextually relevant and less creative responses (from 0.0 to 2.0)
MODEL_RANDOMNESS_TAGGER = 0.0
MODEL_RANDOMNESS_GATHERER = 1.25
MODEL_RANDOMNESS_DECODER = 0.75
DATASET_DIRPATH = "./dataset_writeups/"
HUMANS_TAGGED_DIRNAME = "humans"
DATASET_TXT_SUFFIXES = ["_original.txt", "_cleaned.txt", "_tagged.txt"]
DATASET_MD_SUFFIXES = ["_original.md", "_cleaned.md", "_tagged.md"]

NEW_WRITEUP_CMD = "CMD: new_writeup"
NONCE_LENGTH = 21

CSV_FILENAME = "dataset_writeups.csv"
CSV_HEADER_OBSOLETE = ["filename", "category", "topic", "text"]
CSV_HEADER = ["filename", "category", "text"]
DATASET_CATEGORY = "Web Exploitation"  # TODO: change this
