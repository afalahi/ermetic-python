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
from queries import azure_ad_aws_last_activity_query
from common import ermetic_request
from datetime import datetime

def get_aad_aws_role_activity(days:int=90):
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
  try:
    with open('add_users_aws_roles.csv', 'w', newline='') as csv_file:
      writer = csv.writer(csv_file)
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