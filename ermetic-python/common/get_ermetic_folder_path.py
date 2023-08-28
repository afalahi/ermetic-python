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

def get_ermetic_folder_path(folders, folder_id):
  '''
  Builds Account Folder path to help locating accounts
  '''
  for item in folders:
    if item['Id'] == folder_id:
      parent_id = item['ParentScopeId']
      if parent_id is None:
        return item['Name']
      else:
        parent_path = get_ermetic_folder_path(folders, parent_id)
        return f"{parent_path}/{item['Name']}"
  return None