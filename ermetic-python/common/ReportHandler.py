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
import pandas as pd
import logging
from typing import List, Dict
from datetime import datetime

logging.basicConfig(level=logging.INFO)


class ReportHandler:
    def __init__(self, base_file_name: str, data: List[Dict]) -> None:
        self.base_file_name = f'{base_file_name}-{datetime.now().strftime("%Y-%m-%d")}'
        self.data = data

    def csv_report(self):
        if not self.data:
            logging.warning("Received empty data, cannot generate report")
            return
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
        if not self.data:
            logging.warning("Received empty data, cannot generate report")
            return
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

    def excel_report(self, sheet_name: str = 'ermetic_data_overview', charts: bool = False, split_charts: bool = False, chart_trends: bool = False):
        if not self.data:
            logging.warning("Received empty data, cannot generate report")
            return
        # Create the workbook and sheet using Pandas DF
        df = pd.DataFrame(self.data)
        workbook_name = self.base_file_name + ".xlsx"
        writer = pd.ExcelWriter(workbook_name, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]
        # Freeze the headers
        worksheet.freeze_panes(1, 0)
        # Set Column width to max with of header
        for col_num, value in enumerate(df.columns):
            max_length = max(df[value].astype(
                str).apply(len).max(), len(str(value)))
            worksheet.set_column(col_num, col_num, max_length + 1)
        if charts:
            # add the chart
            chart = workbook.add_chart({'type': 'column'})
            chart.set_size({'width': 800, 'height': 350})
            chart_position = chr(65 + len(df.columns)) + '2'
            chart_width = 13
            charts_per_row = 2
            last_data_column = len(df.columns)
            for col_num in range(1, len(df.columns) - 2):
                # Create a new chart object for each series
                if split_charts:
                    chart = workbook.add_chart({'type': 'column'})
                    chart.set_size({'width': 800, 'height': 350})
                    # Add a series to the chart
                    chart.add_series({
                        'values': f'={sheet_name}!${chr(65 + col_num)}$2:${chr(65 + col_num)}${len(df) + 1}',
                        'categories': f'={sheet_name}!$A$2:$A${len(df) + 1}',
                        'name': f'{sheet_name}!${chr(65 + col_num)}$1',
                    })
                    if chart_trends:
                        chart.add_series({
                            'trendline': {'type': 'polynomial', 'order': 3},
                        })
                    # Calculate the chart row and column position
                    chart_row = 2
                    chart_col = last_data_column + \
                        (col_num - 1) % charts_per_row * chart_width
                    chart_col_letter = chr(65 + chart_col)
                    chart_position = f'{chart_col_letter}{chart_row + (col_num - 1) // charts_per_row * 20}'
                    worksheet.insert_chart(chart_position, chart)
                else:
                    chart.add_series({
                        'values': f'={sheet_name}!${chr(65 + col_num)}$2:${chr(65 + col_num)}${len(df) + 1}',
                        'categories': f'={sheet_name}!$A$2:$A${len(df) + 1}',
                        'name': f'{sheet_name}!${chr(65 + col_num)}$1',
                    })
                    if chart_trends:
                        chart.add_series({
                            'trendline': {'type': 'polynomial', 'order': 3},
                        })
                    chart.set_title({'name': 'Excessive Permissions'})
                    chart.set_x_axis({'name': 'Accounts'})
                    chart.set_y_axis({'name': 'Permissions'})
                    chart.set_style(10)
                    # Insert single sheet
                    worksheet.insert_chart(chart_position, chart)
            # if not split_charts:
            #     # Configure the chart title and x and y axes
            #     chart.set_title({'name': 'Excessive Permissions'})
            #     chart.set_x_axis({'name': 'Accounts'})
            #     chart.set_y_axis({'name': 'Permissions'})
            #     # Insert single sheet
            #     worksheet.insert_chart(chart_position, chart)
        writer.close()
