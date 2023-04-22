#!/usr/bin/env python3
import csv

from common.ermetic_request import ermetic_request
from get_folders import get_folders


def update_account_folder(token: str, file_name: str):
    excluded_child_orgs = ['edl', 'pks', 'sec',
                           'micro', 'dev', 'qa', 'uat', 'prod']
    child_orgs = ['bp', 'corp', 'cpg', 'cto', 'eda', 'edp', ' ', 'mfg', 'pkg']
    os.
    with open(file=file_name, mode='r') as csv_file:
        reader = csv.DictReader(csvfile=csv_file, delimiter=',')
        for row in reader:
            print(row['accountId'])


update_account_folder(token='test', file_name='folders.csv')
