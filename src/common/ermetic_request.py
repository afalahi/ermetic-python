#!/usr/bin/env python3

import requests
from dotenv import dotenv_values
from typing import List, Dict, Callable


def ermetic_request(query: Callable, **kwargs):
    config = dotenv_values()
    # Needed for Pagination, but we can bypass by requesting 1000 items in the "first" query parameter
    CURRENT_CURSOR: str = "null"
    # Build the request and call the API
    URL = config['ERMETIC_URL']
    HEADERS = {
        'Authorization': f'Bearer {config["ERMETIC_TOKEN"]}',
        'Content-Type': 'application/json'
    }
    try:
        res = requests.post(url=URL, headers=HEADERS, json={
            'query': query(CURRENT_CURSOR, **kwargs)})
        res.raise_for_status()
        data: dict = res.json()
        res.close()
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
                'query': query(CURRENT_CURSOR, **kwargs)})
            res.raise_for_status()
            data = res.json()
            results += data['data'][resource]['nodes']
            has_next_page = data['data'][resource]['pageInfo']['hasNextPage']
            CURRENT_CURSOR = f"\"{data['data'][resource]['pageInfo']['endCursor']}\""
        res.close()
        return results
    except requests.exceptions.HTTPError as error:
        raise SystemExit(error)
    except requests.exceptions.RequestException as error:
        raise SystemExit(error)

    # Extract the resource name, whatever we're querying
    # resource = ''
    # for key in data['data']:
    #     resource = key
    # # prepare pagination variables
    # results: List[Dict] = data['data'][resource]['nodes']
    # has_next_page: bool = data['data'][resource]['pageInfo']['hasNextPage']
    # CURRENT_CURSOR = f"\"{data['data'][resource]['pageInfo']['endCursor']}\""
    # # loop if we have more than one page
    # while (has_next_page):
    #     res = requests.post(url=URL, headers=HEADERS, json={
    #         'query': query(CURRENT_CURSOR)})
    #     data = res.json()
    #     results += data['data'][resource]['nodes']
    #     has_next_page = data['data'][resource]['pageInfo']['hasNextPage']
    #     CURRENT_CURSOR = f"\"{data['data'][resource]['pageInfo']['endCursor']}\""
    # res.close()
    # return results
