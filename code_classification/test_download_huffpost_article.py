from newspaper import Article

# URL of the article you want to download
url = 'https://www.huffpost.com/entry/american-airlines-passenger-banned-flight-attendant-punch-justice-department_n_632e25d3e4b0e247890329fe'

# Create an Article object
article = Article(url)

# Download and parse the article
article.download()
article.parse()

# Now you can access the article text
print(article.text)
