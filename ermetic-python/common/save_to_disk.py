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
import xlsxwriter
import pandas as pd
from typing import List, Dict
from datetime import datetime

class ReportHandler:
    def __init__(self, base_file_name:str, data:List[Dict], days:int=30) -> None:
        self.base_file_name = f'{base_file_name}-{datetime.now().strftime("%Y-%m-%d")}'
        self.data = data
        self.days = days
    def csv_report(self):
        file_name = self.base_file_name + '.csv'
        try:
            with open(file=file_name, mode='w', newline='') as csv_file:
                writer = csv.DictWriter(
                    csv_file, fieldnames=self.data[0].keys())
                writer.writeheader()
                try:
                    writer.writerows(self.data)
                except (IOError, OSError) as e:
                    raise SystemExit(
                        f"Error writing to file {e.filename}: {e.args[1]}")
        except (FileNotFoundError, PermissionError, OSError) as e:
            raise SystemExit(
                f"The file '{e.filename}' is in use or we don't have access: {e.args[1]}")
    def json_report(self):
        file_name = self.base_file_name + '.json'
        try:
            with open(file=file_name, mode='w', newline='') as json_file:
                json_data = {"data": self.data}
                try:
                    json_file.write(json.dumps(json_data))
                    json_file.close()
                except (IOError, OSError) as e:
                    raise SystemExit(
                        f"Error writing to file {e.filename}: {e.args[1]}")
        except (FileNotFoundError, PermissionError, OSError) as e:
            raise SystemExit(
                f"The file '{e.filename}' is in use or we don't have access: {e.args[1]}")
    def excel_report(sheet_name:str='ermetic_data_overview', charts:bool=False, split_charts:bool=True):
        pass

def save_to_csv(file_name: str, data: List[Dict]):
    file_name += f'-{datetime.now().strftime("%Y-%m-%d")}.csv'
    try:
        with open(file=file_name, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(
                csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            try:
                writer.writerows(data)
            except (IOError, OSError) as e:
                raise SystemExit(
                    f"Error writing to file {e.filename}: {e.args[1]}")
    except (FileNotFoundError, PermissionError, OSError) as e:
        raise SystemExit(
            f"The file '{e.filename}' is in use or we don't have access: {e.args[1]}")


def save_to_json(file_name: str, data: List[Dict]):
    file_name += f'-{datetime.now().strftime("%Y-%m-%d")}.json'
    try:
        with open(file=file_name, mode='w', newline='') as json_file:
            json_data = {"data": data}
            try:
                json_file.write(json.dumps(json_data))
                json_file.close()
            except (IOError, OSError) as e:
                raise SystemExit(
                    f"Error writing to file {e.filename}: {e.args[1]}")
    except (FileNotFoundError, PermissionError, OSError) as e:
        raise SystemExit(
            f"The file '{e.filename}' is in use or we don't have access: {e.args[1]}")
def save_to_excel(file_name:str, data:List, sheet_name:str, split_charts:bool):
    # Create the workbook and sheet
    workbook_name = f"{file_name}_{datetime.now().strftime('%Y-%m-%d')}.xlsx"
    # sheet_name = 'excessive_permissions_overview'
    workbook = xlsxwriter.Workbook(workbook_name)
    worksheet =workbook.add_worksheet(name=sheet_name)
    #Get the headers
    headers = data[0].keys()
    # get number of rows from the permission report list. This ensures the sheet is dynamic
    num_rows = len(data)

    #Write sheet headers 
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)

    #Freeze the headers
    worksheet.freeze_panes(1, 0)

    #Write sheet values
    for row_num, row_data in enumerate(data, start=1):
        for col_num, (key, value) in enumerate(row_data.items()):
            worksheet.write(row_num, col_num, value)

    # Set cell size
    for col_num, header in enumerate(headers, start=1):
        max_length = len(str(header))  # Start with the length of the header
        for row_data in data:
            cell_content = row_data[header]
            max_length = max(max_length, len(str(cell_content)))  # Compare with the content of each row
        worksheet.set_column(col_num - 1, col_num - 1, max_length + 1)  # Set the column width
    
    # Add the chart
    chart = workbook.add_chart({'type': 'line'})
    chart.set_size({'width': 800, 'height': 350}) 
    chart_position = chr(65 + len(data[0])) + '2'
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
                'categories': f'={sheet_name}!$A$2:$A${num_rows+1}',
                'name': f'{sheet_name}!${chr(65+col_num)}$1',
            })


    if not split_charts:
        # Configure the chart title and x and y axes
        chart.set_title({'name': 'Excessive Permissions'})
        chart.set_x_axis({'name': 'Accounts'})
        chart.set_y_axis({'name': 'Categories'})
        worksheet.insert_chart(chart_position, chart)
    workbook.close()
