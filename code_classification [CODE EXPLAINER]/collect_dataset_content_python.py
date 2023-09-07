import os
import json
import requests
from time import sleep
from urllib.parse import urljoin
import argparse
from secrets import code_scraping_github_token

headers = {
    'Authorization': f'token {code_scraping_github_token}',
    'Accept': 'application/vnd.github+json',
}

def search_repositories(query, page=1):
    search_url = f'https://api.github.com/search/repositories?q={query}&page={page}'
    response = requests.get(search_url, headers=headers)
    return response.json().get('items', [])

def get_code_files(repo_owner, repo_name):
    contents_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents'
    response = requests.get(contents_url, headers=headers)

    if response.status_code != 200:
        return []

    contents = response.json()
    return [content for content in contents if content['type'] == 'file' and content['name'].endswith('.py')]

def download_file(file_url):
    response = requests.get(file_url, headers=headers)
    return response.text if response.status_code == 200 else ''

def main(programming_language):
    code_files = []
    query = f'language:{programming_language}'
    page = 1

    with open(f"dataset_code_language_{programming_language}.jsonl", 'w') as output_file:
        while len(code_files) < 250:
            print(f'Searching repositories. Page: {page}')
            repositories = search_repositories(query, page)
            if not repositories:
                break

            for repo in repositories:
                print(f'Processing repository: {repo["name"]}')
                code_files_in_repo = get_code_files(repo['owner']['login'], repo['name'])
                for code_file in code_files_in_repo:
                    file_content = download_file(code_file['download_url'])

                    if file_content:
                        code_files.append({"content": file_content})
                        output_file.write(json.dumps({"content": file_content}) + '\n')

                        print(f'Collected {programming_language} files: {len(code_files)}')

                        if len(code_files) >= 250:
                            print(f"Reached target number of {programming_language} files.")
                            break

                if len(code_files) >= 250:
                    break

            page += 1
            sleep(10)  # To avoid hitting the rate limits

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('programming_language', help='The programming language to scrape for')
    args = parser.parse_args()
    main(args.programming_language)
