import requests
import csv as csv_ops

from aws_accounts_query import aws_accounts_query


def get_aws_accounts(token: str, csv: bool = False, status: str = "All"):
    """ Return Aws Accounts
    Return accounts as is or filtered and in CSV

    Parameters
    ----------
        status: str
            Filter Accounts by status: Valid, Invalid
        CSV: boolean
            Save results as CSV

    Returns
    --------
        aws_accounts: list
            a dict list of aws accounts
    """

    # Needed for Pagination, but we can bypass by requesting 1000 items in the "first" query parameter
    CURRENT_CURSOR: str = "null"

    # Build the request and call the API
    url = "https://us.app.ermetic.com/api/graph"
    query: str = aws_accounts_query(CURRENT_CURSOR)
    headers = {
        'Authorization': f"Bearer {token}",
        'Content-Type': 'application/json'
    }
    data = requests.request(
        "POST", url, headers=headers, json={'query': query}).json

    # prepare pagination variables
    aws_accounts: list = data['data']['AwsAccounts']['nodes']
    has_next_page: bool = data['data']['AwsAccounts']['pageInfo']['hasNextPage']
    CURRENT_CURSOR = f"\"{data['data']['AwsAccounts']['pageInfo']['endCursor']}\""
    # loop if we have more than one page
    while (has_next_page):
        query = aws_accounts_query(CURRENT_CURSOR)
        data = requests.request(
            "POST", url, headers=headers, json={'query': query}).json()
        aws_accounts += data['data']['AwsAccounts']['nodes']
        has_next_page = data['data']['AwsAccounts']['pageInfo']['hasNextPage']
        CURRENT_CURSOR = f"\"{data['data']['AwsAccounts']['pageInfo']['endCursor']}\""

    # Filter the accounts based on their status
    if status == 'Invalid' or status == "invalid":
        aws_accounts = list(
            filter(lambda account: account['Status'] != 'Valid', aws_accounts))
        aws_accounts = aws_accounts if len(
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
