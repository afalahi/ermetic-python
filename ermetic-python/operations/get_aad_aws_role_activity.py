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

import csv
import json
from datetime import datetime
from queries.azure_ad_aws_last_activity_query import azure_ad_aws_last_activity_query
from common.ermetic_request import ermetic_request

def get_aad_aws_role_activity(days:int=90, csv_file:bool=False, json_file:bool=True):
  """
    Retrieves AAD Users' AWS Roles with activity less than 90 days.

    Parameters
    ----------
    days (int)
                        Number of days since last activity Default is 90.

    Returns
    -------
        List[dict]: 
                        A list of AAD users and their AWS roles.
  """
  if days <= 0:
    raise SystemExit("Days cannot be zero or lower")
  aad_users = ermetic_request(azure_ad_aws_last_activity_query)
  aad_users = [users for users in aad_users if len(users['AwsAssumableRoles']) > 0]
  for user in aad_users:
    for role in list(user['AwsAssumableRoles']):
      now = datetime.utcnow()
      lastActivityTime = role['Role']['LastActivityTime']
      if lastActivityTime is not None:
        lastActivityTime = datetime.fromisoformat(role['Role']['LastActivityTime'][:-1])
        delta = now - lastActivityTime
        if delta.days > days:
          role['Role']['LastActivityTime'] = f'{delta.days} days'
        else:
          user['AwsAssumableRoles'].remove(role)
      else:
        role['Role']['LastActivityTime'] = 'Never'
  if csv_file:
    try:
      with open('aad_users_aws_roles.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        try:
          header = list(aad_users[0].keys())[:-1] + list(aad_users[0]['AwsAssumableRoles'][0]['Role'].keys())
          print(header)
          writer.writerow(header)
        except (IOError, OSError):
          raise SystemExit(
              f"Error writing to file {e.filename}: {e.args[1]}")
        for entry in aad_users:
            roles = entry['AwsAssumableRoles']
            try:
              for i in range(len(roles)):
                role = roles[i]['Role']
                writer.writerow(
                    [entry['UserPrincipalName'], entry['Name'] ,entry['AccountId'], role['Id'], role['Name'], role['LastActivityTime']])
            except (IOError, OSError) as e:
              raise SystemExit(
                  f"Error writing to file {e.filename}: {e.args[1]}")
    except (FileNotFoundError, PermissionError, OSError) as e:
      raise SystemExit(
        f"The file '{e.filename}' is in use or we don't have access: {e.args[1]}")
  if json_file:
    with open(file='aad_users_aws_roles.json', mode='w', newline='') as file:
      file.write(json.dumps(aad_users, indent=2))
      file.close()
  return aad_users