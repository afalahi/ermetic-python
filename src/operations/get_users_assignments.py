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
    users = get_users()
    aws_accounts = get_aws_accounts(False)
    folders = get_folders()
    # root_folders = [r for r in folders if r['Id']
    #                 == 'awsRoot' or r['Id'] == 'azureRoot' or r['Id'] == 'gcpRoot']
    # root_ous = [r for r in folders if r['Id']
    #             == 'awsRoot' or r['Id'] == 'azureRoot' or r['Id'] == 'gcpRoot']
    # folder_hierarchy: List
    # for idx, folder in enumerate(folders):
    #     if folder['Id'] == 'awsRoot' or 'azureRoot':
    #         pass
    #     for i, f in enumerate(folders, start=1):
    #         if folder['Id'] == f['ParentScopeId']:
    #             object = {"folderName": folder['Name']}
    access_report: List[Dict] = []

    for account in aws_accounts:
        obj = {}
        userRole = []
        userName = []
        access_type = []
        obj["account"] = account['Name']
        obj["accountId"] = account['Id']
        for user in users:
            if account['Id'] == user['ScopeId']:
                userName.append(user["UserId"])
                userRole.append(user['Role'])
                access_type.append('Direct')
                # userRole.append(
                #     f'[{user["UserId"]}, {user["Role"]}, Direct]')
                # userRole.append(
                #     {"userId": user['UserId'], "Role": user['Role'], "access": "Direct"})
                obj['Users'] = userRole
            if user['ScopeId'] is None:
                userName.append(user["UserId"])
                userRole.append(user['Role'])
                access_type.append('Organization')
                # userRole.append(
                #     f'[{user["UserId"]}, {user["Role"]}, Organization]')
                # userRole.append(
                #     {"userId": user['UserId'], "Role": user['Role'], "access": "Organization"})
                obj['Users'] = userRole
            for folder in folders:
                if folder['Id'] == user['ScopeId'] and folder['Id'] == account['ParentScopeId']:
                    userName.append(user["UserId"])
                    userRole.append(user['Role'])
                    access_type.append(folder["Name"])
                    # userRole.append(
                    #     f'[{user["UserId"]}, {user["Role"]}, {folder["Name"]}]')
                    # userRole.append(
                    #     {"userId": user['UserId'], "Role": user['Role'], "access": folder["Name"]})
        obj['Users'] = userName
        obj['Role'] = userRole
        obj['AccessType'] = access_type
        access_report.append(deepcopy(obj))
    if csv_file:
        with open('users.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(access_report[0].keys())
            for entry in access_report:
                account = entry['account']
                accountId = entry['accountId']
                users = entry['Users']
                role = entry['Role']
                accessType = entry['AccessType']
                for i in range(len(users)):
                    writer.writerow(
                        [account, accountId, users[i], role[i], accessType[i]])
    if json_file:
        with open(file='users.json', mode='w', newline='') as jsonFile:
            jsonFile.write(json.dumps(users))
            jsonFile.close()
    return access_report
