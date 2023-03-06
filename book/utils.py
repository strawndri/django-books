import requests
import json

def search_books(query):
    url = 'http://openlibrary.org/search.json'
    params = {'q': query}
    response = requests.get(url, params=params)
    results = json.loads(response.text)
    return results['docs']
