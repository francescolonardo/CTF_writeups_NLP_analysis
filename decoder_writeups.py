import json
import os
import re
import argparse

import openai

from settings import MODEL_ID, MODEL_RANDOMNESS_DECODER
from settings import DATASET_DIRPATH, HUMANS_TAGGED_DIRNAME, DATASET_MD_SUFFIXES


def get_response(messages: list):
	response = openai.ChatCompletion.create(  # https://platform.openai.com/docs/api-reference/chat/create
		model=MODEL_ID,
		messages=messages,
		temperature=MODEL_RANDOMNESS_DECODER,
		stream=False,
	)
	return response.choices[0].message


if __name__ == "__main__":
	# create an argument for the string parameter 
	parser = argparse.ArgumentParser()
	parser.add_argument('-dir', dest='directory', default=DATASET_DIRPATH,
						help='the directory to scan for tagging')
	# create an argument for the integer parameter
	parser.add_argument("-n", dest="number", type=int, default=10000,
						help="the number of writeups to tag")
	args = parser.parse_args()
	# get the directory to scan
	starting_directory = args.directory
	# get the number of writeups to scan
	num_writeups = args.number
	
	with open("./api_keys.json", "r", encoding="utf-8") as f:
		api_key = json.load(f)["api_key"]
	openai.api_key = api_key
	with open("./guidelines.json", "r", encoding="utf-8") as f:
		requirements = json.load(f)
		basic_requirements = requirements["basic_requirements"]
		decoder_requirements = requirements["decoder_requirements"]
	guidelines = basic_requirements + decoder_requirements
	print("Sending the context...")
	get_response(messages=guidelines)
	
	# set the regex pattern to match code snippets
	code_snippet_regex = re.compile(r'```[\w\W]*?```')
	try:
		print("Decoding writeups...")
		# loop through all directories and subdirectories
		for dirpath, dirnames, filenames in os.walk(starting_directory):
			# loop through all files in the directory
			# skip the human tagged writeups
			if HUMANS_TAGGED_DIRNAME in dirnames:
				dirnames.remove(HUMANS_TAGGED_DIRNAME)
			for filename in filenames:
				# check if the file is a text file
				if filename.endswith(".txt"):
					if not filename.endswith(DATASET_MD_SUFFIXES[2]):
						# check that the file is not yet tagged
						prefix_filename = filename.split(".")[0]
						if not os.path.exists(os.path.join(dirpath, prefix_filename+DATASET_MD_SUFFIXES[2])):
							num_writeups = num_writeups - 1
							# original file
							in_filepath = os.path.join(
								dirpath, filename)
							#print(f"Writeup file (original): {in_filepath}")
							with open(in_filepath, 'r') as input_f:
								file_content = input_f.read()
								code_snippets = code_snippet_regex.findall(file_content)
								for code_snippet in code_snippets:
									print("Found code snippet in file:", in_filepath)
									print(code_snippet)
		print("Done.")
	except KeyboardInterrupt:
		print("Stop.")
	