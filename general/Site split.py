import requests
from bs4 import BeautifulSoup

# Define your search query
query = "__.surya.__052 on instagram"

# Construct the search URL for DuckDuckGo
search_url = f"https://html.duckduckgo.com/html?q={query.replace(' ', '+')}"

# Create a headers dictionary to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send an HTTP request to the search URL with headers
response = requests.get(search_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all search result links
    for link in soup.find_all('h2'):
        print(link.get_text())
        
else:
    print(f"Failed to retrieve the search results. Status code: {response.status_code}")
