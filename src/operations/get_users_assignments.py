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
from pandas import DataFrame
import json
from copy import deepcopy
from operations.get_aws_accounts import get_aws_accounts
from operations.get_folders import get_folders
from operations.get_users import get_users


def get_users_assignments():
    users = get_users()
    aws_accounts = get_aws_accounts(False)
    folders = get_folders()
    # root_folders = [r for r in folders if r['Id']
    #                 == 'awsRoot' or r['Id'] == 'azureRoot' or r['Id'] == 'gcpRoot']
    # root_ous = [r for r in folders if r['Id']
    #             == 'awsRoot' or r['Id'] == 'azureRoot' or r['Id'] == 'gcpRoot']
    # folder_hierarchy: List
    access_report: List[Dict] = []
    # for idx, folder in enumerate(folders):
    #     if folder['Id'] == 'awsRoot' or 'azureRoot':
    #         pass
    #     for i, f in enumerate(folders, start=1):
    #         if folder['Id'] == f['ParentScopeId']:
    #             object = {"folderName": folder['Name']}
    # for user in users:
    #     if user['ScopeId'] is None:
    #         user["ScopeId"] = 'Organization'
    #     for folder in folders:
    #         if folder['Id'] == user['ScopeId']:
    #             user['ScopeName'] = folder['Name']
    #             user['AccessType'] = 'Folder'
    #     for account in aws_accounts:
    #         if account['Id'] == user['ScopeId']:
    #             user['ScopeName'] = account['Name']
    #             user['AccessType'] = 'Direct'
    #         else:
    #             user['AccessType'] = 'inherited'
    obj = {}
    userRole = []
    for account in aws_accounts:
        obj["account"] = account['Name']
        obj["accountId"] = account['Id']
        for user in users:
            if account['Id'] == user['ScopeId']:
                userRole.append(
                    f'[{user["UserId"]}, {user["Role"]}, Direct]')
                obj['Users'] = userRole
            if user['ScopeId'] is None:
                userRole.append(
                    f'[{user["UserId"]}, {user["Role"]}, Inherited: Organization]')
                obj['Users'] = userRole
            for folder in folders:
                if folder['Id'] == user['ScopeId']:
                    userRole.append(
                        f'[{user["UserId"]}, {user["Role"]}, Inherited: {folder["Name"]}]')
                    obj['Users'] = userRole
        access_report.append(deepcopy(obj))
    # user_assignments: List[Dict] = []
    return access_report


users = get_users_assignments()
with open(file='users.json', mode='w', newline='') as jsonFile:
    jsonFile.write(json.dumps(users))
    jsonFile.close()
