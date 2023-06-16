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


from operations.get_aws_accounts import get_aws_accounts
from operations.get_azure_resource_by_groupId import azure_resources_by_groupId
from operations.get_findings_by_azure_resource_group import get_findings_by_azure_resource_group
from operations.get_users_assignments import get_users_assignments
from operations.get_okta_users import get_okta_users
from operations.get_aad_aws_role_activity import get_aad_aws_role_activity