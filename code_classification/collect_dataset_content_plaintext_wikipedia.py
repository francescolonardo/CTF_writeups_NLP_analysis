import wikipedia
import json
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

output_file = "dataset_content_plaintext_wikipedia.jsonl"

articles_list = []

pbar = tqdm(total=2500)

while len(articles_list) < 2500:
    try:
        random_title = wikipedia.random(pages=1)
        page = wikipedia.page(random_title)
        articles_list.append({'content': page.content})
        pbar.update(1)
    except wikipedia.exceptions.DisambiguationError as e:
        # this error is raised by wikipedia.page() for disambiguation pages
        pass
    except wikipedia.exceptions.PageError as e:
        # this error is raised if the page doesn't exist
        pass

pbar.close()

# Save the articles to a .jsonl file
with open(output_file, 'w') as f:
    for article in articles_list:
        f.write(json.dumps(article))
        f.write('\n')

print(f'Saved {len(articles_list)} articles to {output_file}')
