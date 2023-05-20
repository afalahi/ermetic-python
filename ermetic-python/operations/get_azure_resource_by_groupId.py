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
from common.ermetic_request import ermetic_request
from common.AzureResourceFilter import AzureResourceFilter
from queries.azure_resources_query import azure_resources_query


def azure_resources_by_groupId(group_ids: str):
    '''
    Parameters
    ----------
    group_ids: str
              comma separated Azure Resource Group Id(s)

    Examples
    --------
    >>> azure_resources_by_groupId('7590f34r-834a-095g-106t-482524dbab6c/resourceGroups/exampleresourcegroup')
    >>> azure_resources_by_groupId('7590f34r-834a-095g-106t-482524dbab6c/resourceGroups/exampleresourcegroup, 7590f34r-834a-095g-106t-482524dbab6c/resourceGroups/exampleresourcegroup')
    '''
    az_filter = None
    try:
        az_filter = AzureResourceFilter(ResourceGroupIds=group_ids)
    except KeyError as error:
        raise SystemExit(f'Error: {error}')
    azure_resources = ermetic_request(
        azure_resources_query, filters=az_filter.filter)
    return azure_resources
