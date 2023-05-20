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

from queries.aws_accounts_query import aws_accounts_query
from queries.azure_resources_query import azure_resources_query
from queries.users_assignments_query import users_assignments_query
from queries.get_folders_query import get_folders_query
from queries.okta_users_query import okta_users_query
from queries.findings_by_resource_group_query import findings_by_resource_group_query