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

  def get_ermetic_aws_folder_path(folders, aws_folder_id):
    '''
    Builds AWS Account Folder path to help locating accounts
    '''
    for item in folders:
      if item['Id'] == aws_folder_id:
        parent_id = item['ParentScopeId']
        if parent_id is None:
          return item['Name']
        else:
          parent_path = get_ermetic_aws_folder_path(folders, parent_id)
          return f"{parent_path}/{item['Name']}"
    return None

  access_report: List[Dict] = []
  for account in aws_accounts:
    obj = {
      "AccountName": account["Name"],
      "AccountId": account["Id"],
      "Users": []
    }
    for user in users:
      user_role = {
        "UserId": None,
        "Role": None,
        "AccessType": None,
        "FolderPath": None
      }
      if account["Id"] == user["ScopeId"]:
        user_role["UserId"] = user["UserId"]
        user_role["Role"] = user["Role"]
        user_role["AccessType"] = "Direct"
        user_role["FolderPath"] = get_ermetic_aws_folder_path(folders, account["ParentScopeId"])
        obj["Users"].append(user_role)
      if not user["ScopeId"]:
        user_role["UserId"] = user["UserId"]
        user_role["Role"] = user["Role"]
        user_role["AccessType"] = "Organization"
        user_role["FolderPath"] = get_ermetic_aws_folder_path(folders, account["ParentScopeId"])
        obj["Users"].append(user_role)
      for folder in folders:
        if folder["Id"] == user["ScopeId"]:
          user_role["UserId"] = user["UserId"]
          user_role["Role"] = user["Role"]
          user_role["AccessType"] = "Folder"
          user_role["FolderPath"] = get_ermetic_aws_folder_path(folders, account["ParentScopeId"])
          obj["Users"].append(user_role)
  access_report.append(obj)

  if csv_file:
    try:
      with open('users.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        try:
          header = list(access_report[0].keys())
          header.append(access_report[0]['Users'][0].keys())
          writer.writerow(header)
        except (IOError, OSError):
          raise SystemExit(
              f"Error writing to file {e.filename}: {e.args[1]}")
        for entry in access_report:
          account = entry['AccountName']
          accountId = entry['AccountId']
          users = entry['Users']
          try:
            for i in range(len(users)):
              writer.writerow(
                  [account, accountId, users[i]['UserId'], users[i]['Role'], users[i]['AccessType'], users[i]['FolderPath']])
          except (IOError, OSError) as e:
            raise SystemExit(
                f"Error writing to file {e.filename}: {e.args[1]}")
    except (FileNotFoundError, PermissionError, OSError) as e:
      raise SystemExit(
          f"The file '{e.filename}' is in use or we don't have access: {e.args[1]}")
  if json_file:
    with open(file='users.json', mode='w', newline='') as file:
      file.write(json.dumps(access_report))
      file.close()
  return access_report
