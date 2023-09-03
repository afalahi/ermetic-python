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

# from operations.get_findings_by_azure_resource_group import get_findings_by_azure_resource_group
# from operations.get_users_assignments import get_users_assignments
from operations.get_aws_accounts import get_aws_accounts
# from operations.get_okta_users import get_okta_users
# from operations.get_aws_billable_resources import get_aws_billable_resources
# from operations.get_excessive_permissions_count import get_aws_excessive_permissions_count
from operations.Folders import Folders
# from common.ReportHandler import ReportHandler
# from Filters.FindingFilter import FindingFilter
# from operations.Folder_Refactor import folder_org_build
folders = Folders(accounts=get_aws_accounts())
folder_tree = folders.folders_tree
# parent_folders = {}
# folder_names = 'Accounts,SivansOU'
# for name in folder_names.split(','):
#     nodes = folder_tree.find_nodes_by_name(name=name)
#     if nodes:
#         parent_folders[name] = [node.to_dict() for node in nodes]
# print(parent_folders)
print(folder_tree.to_dict())
# Reduce DRY
# data = get_aws_excessive_permissions_count(group_by_ou=True, depth=2)
# report_handler = ReportHandler(base_file_name="permissions_report", data=data)
# report_handler.excel_report("ExcessivePermissions", True,)
# report_handler.csv_report()
# finding_filter = FindingFilter()
# finding_filter.end_date = '02/05/2023'
# finding_filter.start_date = '02/06/2023'
# folder_org_build()
# print(finding_filter.to_filter_string())
# print(finding_filter.to_filter_string())
# aws_accounts = get_aws_accounts()
# folders = GetFolders(aws_accounts)
# folders.get_folders()
# print(len(folders.org_tree))
# get_findings_by_azure_resource_group(
#     resource_group_id="8207b91f-642d-456e-961c-482524dbab6c/resourceGroups/yochayresourcegroup", csv_file=True)
