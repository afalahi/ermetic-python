# Copyright 2023 ali.falahi@ermetic.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List, Dict
import json
import csv
from copy import deepcopy

from operations.get_aws_accounts import get_aws_accounts
from operations.get_folders import get_folders
from operations.get_users import get_users


def get_users_assignments(csv_file=False, json_file=False):
    """
    Get Tenant users and save to CSV or JSON

    Keyword Arguments:

    csv_file -- Save to file to csv (default false)

    json_file -- Save to file to json (default false)
    """
    users = get_users()
    aws_accounts = get_aws_accounts(False)
    folders = get_folders()

    def aws_folder_path(folders, aws_folder_id):
        '''
        Builds AWS Account Folder path to help locating accounts
        '''
        for item in folders:
            if item['Id'] == aws_folder_id:
                parent_id = item['ParentScopeId']
                if parent_id is None:
                    return item['Name']
                else:
                    parent_path = aws_folder_path(folders, parent_id)
                    return f"{parent_path}/{item['Name']}"
        return None

    access_report: List[Dict] = []
    for account in aws_accounts:
        obj = {}
        userRole = []
        userName = []
        access_type = []
        path = []
        obj["account"] = account['Name']
        obj["accountId"] = account['Id']
        for user in users:
            if account['Id'] == user['ScopeId']:
                userName.append(user["UserId"])
                userRole.append(user['Role'])
                access_type.append('Direct')
                path.append(aws_folder_path(folders, account['ParentScopeId']))
            if user['ScopeId'] is None:
                userName.append(user["UserId"])
                userRole.append(user['Role'])
                access_type.append('Organization')
                path.append(aws_folder_path(folders, account['ParentScopeId']))
            for folder in folders:
                if folder['Id'] == user['ScopeId'] and folder['Id'] == account['ParentScopeId']:
                    userName.append(user["UserId"])
                    userRole.append(user['Role'])
                    access_type.append(folder["Name"])
                    path.append(aws_folder_path(
                        folders, account['ParentScopeId']))

        obj['Users'] = userName
        obj['Role'] = userRole
        obj['AccessType'] = access_type
        obj['AccountPath'] = path
        access_report.append(deepcopy(obj))
    if csv_file:
        try:
            with open('users.csv', 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                try:
                    writer.writerow(access_report[0].keys())
                except (IOError, OSError):
                    raise SystemExit(
                        f"Error writing to file {e.filename}: {e.args[1]}")
                for entry in access_report:
                    account = entry['account']
                    accountId = entry['accountId']
                    users = entry['Users']
                    role = entry['Role']
                    accessType = entry['AccessType']
                    accountPath = entry['AccountPath']
                    try:
                        for i in range(len(users)):
                            writer.writerow(
                                [account, accountId, users[i], role[i], accessType[i], accountPath[i]])
                    except (IOError, OSError) as e:
                        raise SystemExit(
                            f"Error writing to file {e.filename}: {e.args[1]}")
        except (FileNotFoundError, PermissionError, OSError) as e:
            raise SystemExit(
                f"The file '{e.filename}' is in use or we don't have access: {e.args[1]}")
    if json_file:
        with open(file='users.json', mode='w', newline='') as jsonFile:
            jsonFile.write(json.dumps(users))
            jsonFile.close()
    return access_report
