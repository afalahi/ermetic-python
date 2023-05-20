#!/usr/bin/env python3

from queries.okta_users_query import okta_users_query
from common.ermetic_request import ermetic_request
from common.save_to_disk import save_to_csv, save_to_json


def get_okta_users(csv_file: bool = False, json_file: bool = False):
    """
    Get Okta users and save to CSV or JSON

    Keyword Arguments:

    token -- The Ermetic Token

    csv -- Save to file to csv (default false)
    """
    data = ermetic_request(query=okta_users_query)

    if csv_file:
        file_name = 'okta_users.csv'
        save_to_csv(file_name=file_name, data=data)
    if json_file:
        file_name = 'okta_users.json'
        save_to_json(file_name=file_name, data=data)
    return data
