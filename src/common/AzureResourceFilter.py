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

class AzureResourceFilter:
    """
    Instantiates an Azure Resource Filter as string to be used in query filter. All kwargs are strings separated by commas.

    Parameters
    ----------
    **kwargs: dict
              AccountId: str
              Types: str
              ResourceGroupIds: str
              Ids: str

    Examples
    --------
    >>> azure_filter = AzureResourceFilter(Types='AzureResourcesResourceGroup')
    >>> azure_filter.filter
    {Types:[AzureResourcesResourceGroup], }
    >>> azure_filter = AzureResourceFilter(Types='AzureResourcesResourceGroup, AzureClassicNetworkVirtualNetwork')
    >>> azure_filter.filter
    {Types:[AzureResourcesResourceGroup, AzureClassicNetworkVirtualNetwork ], }

    Raises
    ------
    KeyErrorException
      If the keyword arguments provides doesn't match the required input. Note args are case sensitive
    """

    def __init__(self, **kwargs) -> None:
        # az_filter = {}
        string = ''
        for key in kwargs:
            if key not in ['AccountIds', 'Types', 'ResourceGroupIds', 'Ids']:
                raise KeyError(
                    f'AzureResourceFilter() kwarg{[key]}: Invalid key, accepted values are AccountIds, Types, ResourceGroupIds, Ids')
            if key == 'ResourceGroupIds':
                string += f'{key}:["{kwargs[key]}"], '
            else:
                string += f'{key}:[{kwargs[key]}], '
            # az_filter[key] = kwargs[key]
        self.filter = f'{{{string}}}'
