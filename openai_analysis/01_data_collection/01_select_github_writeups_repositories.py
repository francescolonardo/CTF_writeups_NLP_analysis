import requests
from secrets import github_token


def select_github_repositories(query, max_repos=25):
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Form the search query URL
    search_url = (
        f"https://api.github.com/search/repositories?q={query}+in:readme+in:description"
    )

    # Make the request to GitHub API
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        results = response.json()
        repos = results["items"][:max_repos]

        for repo in repos:
            print(f"Repository Name: {repo['name']}")
            print(f"Description: {repo['description']}")
            print(f"URL: {repo['html_url']}\n")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)


# Searching for web application CTF writeups
select_github_repositories("web+application+CTF+writeup")
