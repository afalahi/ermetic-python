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

import logging
from datetime import datetime
from collections import defaultdict

from Filters.FindingFilter import FindingFilter
from enums.FindingTypes import FindingTypes
from operations.get_aws_accounts import get_aws_accounts
from operations.Folders import Folders
from common.ermetic_request import ermetic_request
from common.get_ermetic_folder_path import get_ermetic_folder_path
from queries.findings_query import findings_query

logging.basicConfig(level=logging.INFO)


def get_aws_excessive_permissions_count(days: int = None, group_by_ou: bool = False, compare: bool = False, depth: int = 0):
    if depth > 2:
        logging.info('Depth can not be larger than 2')
    logging.info('getting aws accounts')
    aws_accounts = get_aws_accounts(status="Valid")
    folders = Folders()
    folders.get_folders()
    logging.info("getting permissions count")

    # build the findings filter for excessive permissions
    finding_types = [FindingTypes.AwsInactiveRoleFinding,
                     FindingTypes.AwsExcessivePermissionGroupFinding,
                     FindingTypes.AwsExcessivePermissionRoleFinding,
                     FindingTypes.AwsExcessivePermissionUserFinding,
                     FindingTypes.AwsInactiveUserFinding,
                     FindingTypes.AwsUnusedPermissionSetFinding,
                     FindingTypes.AwsExcessivePermissionPermissionSetFinding]
    finding_filter = FindingFilter(types=finding_types, days=days)
    # Get the excessive permissions from GraphQL
    excessive_permissions = ermetic_request(
        findings_query, filters=finding_filter.to_filter_string())
    # Pre-filter permissions on accountId
    permissions_by_account = defaultdict(list)
    for permission in excessive_permissions:
        permissions_by_account[permission['AccountId']].append(permission)

    results = []
    # To get progress percentage
    count = 0
    # Set up mapping between the FindingType and a Common name for the report
    mapping = {
        "AwsInactiveUserFinding": "InactiveUsers",
        "AwsInactiveRoleFinding": "InactiveRoles",
        "AwsUnusedPermissionSetFinding": "InactivePermissionSet",
        "AwsExcessivePermissionGroupFinding": "OverPrivilegedGroups",
        "AwsExcessivePermissionRoleFinding": "OverPrivilegedRoles",
        "AwsExcessivePermissionUserFinding": "OverPrivilegedUsers",
        "AwsExcessivePermissionPermissionSetFinding": "OverPrivilegedPermissionSet"
    }

    # Function to update the Permissions object to reduce DRY
    def update_obj(obj, typename):
        nonlocal count
        count += 1
        logging.info(
            f"Currently calculating Excessive Permissions: {round(count / len(excessive_permissions) * 100)}% completion")
        # get the value mapping of the ermetic finding type
        key = mapping.get(typename)
        # if the key isn't none then increment the Excessive Permission
        if key:
            obj[key] += 1

    # This control flow will return a list of accounts with their Excessive Permission Counts, it's controlled by the parameter group_by_ou=False
    if not group_by_ou:
        for account in aws_accounts:
            obj = {
                "Account": f'{get_ermetic_folder_path(folders=folders.folders, folder_id=account["ParentScopeId"])}/{account["Name"]}',
                "InactiveUsers": 0,
                "InactiveRoles": 0,
                "InactivePermissionSet": 0,
                "OverPrivilegedGroups": 0,
                "OverPrivilegedRoles": 0,
                "OverPrivilegedUsers": 0,
                "OverPrivilegedPermissionSet": 0,
                "Date": datetime.now().strftime('%Y-%m-%d')
            }
            for permission in permissions_by_account.get(account['Id'], []):
                if account['Id'] == permission['AccountId']:
                    update_obj(obj=obj, typename=permission['__typename'])
            results.append(obj)
    # This flow aggregates the Excessive Permissions under their respective account OU/Folder in Ermetic
    else:
        folder_hierarchy = Folders(accounts=aws_accounts)
        folder_hierarchy.get_folders()
        parent_folders = folder_hierarchy.org_tree

        # Reduce DRY
        def update_result(parent, child, aws_accounts, permissions, results):
            folder_name = parent["Name"] if child is None else f"{parent['Name']}/{child['Name']}"
            obj = {
                "Folder": folder_name,
                "InactiveUsers": 0,
                "InactiveRoles": 0,
                "InactivePermissionSet": 0,
                "OverPrivilegedGroups": 0,
                "OverPrivilegedRoles": 0,
                "OverPrivilegedUsers": 0,
                "OverPrivilegedPermissionSet": 0,
                "Date": datetime.now().strftime('%Y-%m-%d')
            }
            for account in aws_accounts:
                folder_path = get_ermetic_folder_path(
                    folders=folders.folders, folder_id=account["ParentScopeId"])
                if folder_name in folder_path:
                    for permission in permissions.get(account['Id'], []):
                        update_obj(
                            obj=obj, typename=permission['__typename'])
            results.append(obj)
        # Loop through the root, parent and child folders only two levels deep. The first loop will always run, the rest are controlled by the depth parameter
        for parent in parent_folders:
            update_result(parent, None, aws_accounts,
                          permissions_by_account, results)
            if parent.get('Children') and depth == 1:
                for child in parent.get('Children'):
                    update_result(parent, child, aws_accounts,
                                  permissions_by_account, results)
                    if child.get('Children') and depth == 2:
                        print(f'Depth 2: {child}')
                        for subchild in child.get('Children'):
                            update_result(child, subchild, aws_accounts,
                                          permissions_by_account, results)

    return results
