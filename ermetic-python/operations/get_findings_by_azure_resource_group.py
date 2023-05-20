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
import json

from common import ermetic_request, FindingsFilter, save_to_csv, save_to_json
from operations import azure_resources_by_groupId
from queries.findings_by_resource_group_query import findings_by_resource_group_query


def get_findings_by_azure_resource_group(resource_group_id: str, status: str = 'Open', csv_file=False, json_file=False):
    """
    Retrieves findings by Azure resource group Id.

    Parameters
    ----------
    resource_group_id (str)
                        The ID of the Azure resource group.
    status (str, optional): 
                        The status of the findings. Defaults to 'Open'.
    csv_file (bool, optional): 
                        Flag indicating whether to save findings as a CSV file. Defaults to False.
    json_file (bool, optional): 
                        Flag indicating whether to save findings as a JSON file. Defaults to False.

    Returns
    -------
        List[dict]: 
                        A list of findings matching the specified criteria.
    """
    azure_resources = azure_resources_by_groupId(resource_group_id)
    resource_ids = [i['Id'] for i in azure_resources]
    findings_filter = FindingsFilter(
        ResourceIds=json.dumps(resource_ids), Statuses=status)
    findings = ermetic_request(
        findings_by_resource_group_query, filters=findings_filter.filter)
    for finding in findings:
        steps = finding['Remediation']['Console']['Steps'] = str(
            finding['Remediation']['Console']['Steps']).split('\n')
        finding['Remediation'] = '\n'.join(steps)
    if csv_file:
        file_name = f'findings-{resource_group_id.split("/")[-1]}'
        save_to_csv(file_name=file_name, data=findings)
    if json_file:
        file_name = f'findings-{resource_group_id.split("/")[-1]}'
        save_to_json(file_name=file_name, data=findings)
    return findings
