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
import requests
from dotenv import dotenv_values
from queries.users_assignments_query import users_assignments_query
from typing import List, Dict


def get_users():
    config = dotenv_values()
    URL = config['ERMETIC_URL']
    config["ERMETIC_TOKEN"]
    HEADERS = {
        'Authorization': f'Bearer {config["ERMETIC_TOKEN"]}',
        'Content-Type': 'application/json'
    }
    try:
        res = requests.post(url=URL, headers=HEADERS, json={
            'query': users_assignments_query()})
        res.raise_for_status()
        users: List[Dict] = res.json()['data']['UserRoleAssignments']
        res.close()
        return users
    except requests.exceptions.HTTPError as error:
        raise SystemExit(f'UsersQueryError: {error}')
    except requests.exceptions.RequestException as error:
        SystemExit(f'UserRequestError: {error}')
