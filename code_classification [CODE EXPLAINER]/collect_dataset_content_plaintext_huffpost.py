import json
from newspaper import Article
from tqdm import tqdm

links_file = "huffpost_links_dataset.jsonl"
output_file = "dataset_content_plaintext_huffpost.jsonl"

with open(links_file, 'r') as infile:
    links = list(infile)

# Initializing the progress bar with a total of 2500
pbar = tqdm(total=2500, ncols=75)

with open(output_file, 'w') as outfile:
    i = 0
    for line in links:
        if i >= 2500:
            break
        data = json.loads(line)
        url = data['link']

        # Create an Article object
        article = Article(url)

        # Try to download and parse the article
        try:
            article.download()
            article.parse()
        except Exception as e:
            print(f"Failed to download article at {url}. Error: {e}")
            continue

        # Add the article text to the output file
        json.dump({'content': article.text}, outfile)
        outfile.write('\n')
        i += 1
        
        # Update the progress bar
        pbar.update(1)

# Close the progress bar
pbar.close()

print(f'Saved articles to {output_file}')
