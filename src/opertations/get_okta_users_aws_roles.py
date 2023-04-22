#!/usr/bin/env python3
import csv as csv_ops
import json

from queries.okta_users_query import okta_users_query
from common.ermetic_request import ermetic_request


def get_okta_users(csv: bool = True):
    """
    Get Okta users and save to CSV or JSON

    Keyword Arguments:

    token -- The Ermetic Token

    csv -- Save to file to csv (default false)
    """
    data = ermetic_request(query=okta_users_query)

    if csv:
        file_name = 'okta_users.csv'
        with open(file=file_name, mode='w', newline='') as csv_file:
            writer = csv_ops.DictWriter(
                csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    else:
        file_name = 'okta_users.json'
        with open(file=file_name, mode='w', newline='') as json_file:
            json_data = {"data": data}
            json_file.write(json.dumps(json_data))
            json_file.close()
    return data
