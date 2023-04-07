import csv as csv_ops
from typing import List, Dict, Literal

from aws_accounts_query import aws_accounts_query
from ermetic_request import ermetic_request


def get_aws_accounts(token: str, csv: bool = True, status: str = "All"):
    aws_accounts = ermetic_request(token=token, query=aws_accounts_query)
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
    if csv:
        if isinstance(aws_accounts, list) != True:
            return aws_accounts
        file_name = f'AwsAccounts-{status}.csv'
        with open(file=file_name, mode='w', newline='') as csv_file:
            writer = csv_ops.DictWriter(
                csv_file, fieldnames=aws_accounts[0].keys())
            writer.writeheader()
            writer.writerows(aws_accounts)

    return aws_accounts
