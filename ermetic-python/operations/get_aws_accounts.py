#!/usr/bin/env python3

from typing import List, Dict, Literal
from queries.aws_accounts_query import aws_accounts_query
# from common.save_to_disk import save_to_csv
from common.ermetic_request import ermetic_request


def get_aws_accounts(csv_file: bool = False, status: str = "All"):
    aws_accounts = ermetic_request(query=aws_accounts_query)
    # Filter the accounts based on their status
    if status == 'Invalid' or status == "invalid":
        aws_accounts: List[Dict] = list(
            filter(lambda account: account['Status'] != 'Valid', aws_accounts))
        aws_accounts: List[Dict] | Literal = aws_accounts if len(
            aws_accounts) > 0 else "All accounts connected"

    elif status == 'Valid' or status == 'valid':
        aws_accounts = list(
            filter(lambda account: account['Status'] == 'Valid', aws_accounts))
        # Remove the issues property from valid accounts
        for i in aws_accounts:
            del i["Issues"]
    # Write results to CSV
    # if csv_file:
    #     if isinstance(aws_accounts, list) != True:
    #         return aws_accounts
    #     file_name = f'AwsAccounts-{status}'
    #     save_to_csv(file_name=file_name, data=aws_accounts)

    return aws_accounts
