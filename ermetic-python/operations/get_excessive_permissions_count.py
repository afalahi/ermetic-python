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

def get_aws_excessive_permissions_count(save_csv:bool=False, save_excel:bool=False, split_charts:bool=False, days:int=30):
    if not save_excel and not save_csv:
        print('Cannot save report, you must provide one of these arguments: save_csv=True or save_excel=True')
        return
    print('getting aws accounts')
    aws_accounts = get_aws_accounts(status='valid')
    folders = get_folders()
    print("getting permissions count")
    now = datetime.now()
    month_ago = now - timedelta(days=days)
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
            "Account":f'{get_ermetic_folder_path(folders=folders, folder_id=account["ParentScopeId"])}/{account["Name"]}',
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
    if save_csv:
        save_to_csv(data=permission_report, file_name="excessive_permissions")
    if save_excel:
        # Create the workbook and sheet
        workbook_name = f"excessive_permissions_{now.strftime('%Y-%m-%d')}.xlsx"
        sheet_name = 'excessive_permissions_overview'
        workbook = xlsxwriter.Workbook(workbook_name)
        worksheet =workbook.add_worksheet(name=sheet_name)
        #Get the headers
        headers = permission_report[0].keys()
        # get number of rows from the permission report list. This ensures the sheet is dynamic
        num_rows = len(permission_report)

        #Write sheet headers 
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header)

        #Freeze the headers
        worksheet.freeze_panes(1, 0)

        #Write sheet values
        for row_num, row_data in enumerate(permission_report, start=1):
            for col_num, (key, value) in enumerate(row_data.items()):
                worksheet.write(row_num, col_num, value)
        # Set Column width to max with of header
        for col_num, header in enumerate(headers, start=1):
            max_length = len(str(header))  # Start with the length of the header
            for row_data in permission_report:
                cell_content = row_data[header]
                max_length = max(max_length, len(str(cell_content)))  # Compare with the content of each row
            worksheet.set_column(col_num - 1, col_num - 1, max_length + 1)  # Set the column width
        # add the chart
        chart = workbook.add_chart({'type': 'line'})
        chart.set_size({'width': 800, 'height': 350}) 
        chart_position = chr(65 + len(permission_report[0])) + '2'
        chart_width = 13
        charts_per_row = 2
        last_data_column = len(headers) 
        for col_num in range(1, len(headers)):
            # Create a new chart object for each series
            if split_charts:
                chart = workbook.add_chart({'type': 'line'})
                chart.set_size({'width': 800, 'height': 350}) 
                # Add a series to the chart
                chart.add_series({
                    'values': f'={sheet_name}!${chr(65+col_num)}$2:${chr(65+col_num)}${num_rows+1}',
                    'trendline':{
                        'type': 'polynomial',
                        'order': 3,
                    },
                    'categories': f'={sheet_name}!$A$2:$A${num_rows+1}',
                    'name': f'{sheet_name}!${chr(65+col_num)}$1',
                })
                # Calculate the chart row and column position
                chart_row = 2
                chart_col = last_data_column + (col_num - 1) % charts_per_row * chart_width
                chart_col_letter = chr(65 + chart_col)
                chart_position = f'{chart_col_letter}{chart_row + (col_num - 1) // charts_per_row * 20}'
                worksheet.insert_chart(chart_position, chart)
            else:
                chart.add_series({
                    'values': f'={sheet_name}!${chr(65+col_num)}$2:${chr(65+col_num)}${num_rows+1}',
                    'trendline':{
                        'type': 'polynomial',
                        'order': 3,
                    },
                    'categories': f'={sheet_name}!$A$2:$A${num_rows+1}',
                    'name': f'{sheet_name}!${chr(65+col_num)}$1',
                })
        # worksheet.insert_chart('' + str(15 * (col_num-1) + 2), chart)
        # chart_position = chr(65 + len(permission_report[0])) + '2'
        if not split_charts:
            # Configure the chart title and x and y axes
            chart.set_title({'name': 'Excessive Permissions'})
            chart.set_x_axis({'name': 'Accounts'})
            chart.set_y_axis({'name': 'Categories'})
            # Insert single sheet
            worksheet.insert_chart(chart_position, chart)
        workbook.close()