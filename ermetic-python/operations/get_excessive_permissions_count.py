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
import xlsxwriter
from datetime import datetime, timedelta
from operations.get_aws_accounts import get_aws_accounts
from operations.get_folders import get_folders
from common import ermetic_request, save_to_csv, get_ermetic_folder_path
from queries import aws_excessive_permissions

def get_aws_excessive_permissions_count():
    workbook = xlsxwriter.Workbook('charts.xlsx')
    worksheet =workbook.add_worksheet()

    print('getting aws accounts')
    aws_accounts = get_aws_accounts(status='valid')
    folders = get_folders()
    print("getting permissions count")
    now = datetime.now()
    month_ago = now - timedelta(days=30)
    print(month_ago.strftime('%Y-%m-%dT%H:%M:%S'))
    filters = f'''Types:[
        AwsInactiveUserFinding, 
        AwsInactiveRoleFinding,
        AwsExcessivePermissionGroupFinding, 
        AwsExcessivePermissionRoleFinding, 
        AwsExcessivePermissionUserFinding,
        AwsExcessivePermissionPermissionSetFinding,
        AwsUnusedPermissionSetFinding],
        CreationTimeStart:"{month_ago.strftime('%Y-%m-%dT%H:%M:%S')}"
        CreationTimeEnd:"{now.strftime('%Y-%m-%dT%H:%M:%S')}"
        '''
    excessive_permissions = ermetic_request(aws_excessive_permissions,filters=filters)
    permission_report = []
    count = 0
    for account in aws_accounts:
        obj = {
            "Account":account["Name"],
            "InactiveUsers":0,
            "InactiveRoles":0,
            "InactivePermissionSet":0,
            "OverPrivilegedGroups":0,
            "OverPrivilegedRoles":0,
            "OverPrivilegedUsers":0,
            "OverPrivilegedPermissionSet":0,
        }
        for permission in excessive_permissions:
            if account['Id'] == permission['AccountId']:
                count+= 1
                print(f"Currently calculating Excessive Permissions on Account {account['Id']}: {round(count / len(excessive_permissions) * 100)}% completion")
                if permission["__typename"] == "AwsInactiveUserFinding":
                    obj["InactiveUsers"]+= 1
                if permission["__typename"] == "AwsInactiveRoleFinding":
                    obj["InactiveRoles"]+= 1
                if permission["__typename"] == "AwsUnusedPermissionSetFinding":
                    obj["InactivePermissionSet"]+= 1
                if permission["__typename"] == "AwsExcessivePermissionGroupFinding":
                    obj["OverPrivilegedGroups"]+= 1
                if permission["__typename"] == "AwsExcessivePermissionRoleFinding":
                    obj["OverPrivilegedRoles"]+= 1
                if permission["__typename"] == "AwsExcessivePermissionUserFinding":
                    obj["OverPrivilegedUsers"]+= 1
                if permission["__typename"] == "AwsExcessivePermissionPermissionSetFinding":
                    obj["OverPrivilegedPermissionSet"]+= 1
        permission_report.append(obj)
    # save_to_csv(data=permission_report, file_name="excessive_permissions")
    headers = permission_report[0].keys()
    num_rows = len(permission_report)
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)
    for row_num, row_data in enumerate(permission_report, start=1):
        for col_num, (key, value) in enumerate(row_data.items()):
            worksheet.write(row_num, col_num, value)
    worksheet.freeze_panes(1, 0)
    chart = workbook.add_chart({'type': 'line'})
    for col_num in range(1, len(headers)):
        # Create a new chart object for each series
        # chart = workbook.add_chart({'type': 'line'})
        
         # Add a series to the chart
        chart.add_series({
            'values': f'=Sheet1!${chr(65+col_num)}$2:${chr(65+col_num)}${num_rows+1}',
            'categories': f'=Sheet1!$A$2:$A${num_rows+1}',
            'name': f'Sheet1!${chr(65+col_num)}$1',
        })
    worksheet.insert_chart('D' + str(15 * (col_num-1) + 2), chart)
    workbook.close()