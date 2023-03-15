import requests
from typing import List, Dict, Callable


def ermetic_request(token: str, query: Callable):
    # Needed for Pagination, but we can bypass by requesting 1000 items in the "first" query parameter
    CURRENT_CURSOR: str = "null"
    # Build the request and call the API
    URL = "https://us.app.ermetic.com/api/graph"
    HEADERS = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    res = requests.post(url=URL, headers=HEADERS, json={
        'query': query(CURRENT_CURSOR)})
    data: dict = res.json()
    res.close()

    # Extract the resource name, whatever we're querying
    resource = ''
    for key in data['data']:
        resource = key
    # prepare pagination variables
    results: List[Dict] = data['data'][resource]['nodes']
    has_next_page: bool = data['data'][resource]['pageInfo']['hasNextPage']
    CURRENT_CURSOR = f"\"{data['data'][resource]['pageInfo']['endCursor']}\""
    # loop if we have more than one page
    while (has_next_page):
        res = requests.post(url=URL, headers=HEADERS, json={
            'query': query(CURRENT_CURSOR)})
        data = res.json()
        results += data['data'][resource]['nodes']
        has_next_page = data['data'][resource]['pageInfo']['hasNextPage']
        CURRENT_CURSOR = f"\"{data['data'][resource]['pageInfo']['endCursor']}\""
    res.close()
    return results