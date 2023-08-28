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

from typing import List, Tuple


class FindingsFilter:
    def __init__(self, **kwargs) -> None:
        string = ''
        for key in kwargs:
            if key not in ['Statuses', 'Types', 'ResourceIds', 'Ids', 'Severities', 'CreationTimeStart', 'CreationTimeEnd']:
                raise KeyError(
                    f'FindingFilter kwarg{[key]}: Invalid key, accepted values are Statuses, ResourceIds, Severities, Ids')
            if key == 'ResourceIds':
                string += f'{key}:{kwargs[key]}, '
            else:
                string += f'{key}:[{kwargs[key]}], '
            # string += f'{key}:[{kwargs[key]}], '
            # az_filter[key] = kwargs[key]
        self.filter = f'{{{string}}}'
