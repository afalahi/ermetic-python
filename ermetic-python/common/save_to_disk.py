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
from typing import List, Dict
from datetime import datetime


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
    file_name += f'-{datetime.now().strftime("%Y-%m-%d")}.csv'
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
