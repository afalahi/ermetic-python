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
from datetime import datetime, timedelta
from typing import List
from enums.FindingTypes import FindingTypes
from enums.FindingCategory import FindingCategory
from enums.FindingStatus import FindingStatus

class FindingFilter:
  def __init__(
    self, 
    days:int=None, 
    types:List[FindingTypes]|FindingTypes=None, 
    categories:FindingCategory=None,
    status:FindingStatus=None
  ):
    self.days = days

    if types:
        if not isinstance(types, list):
            types = [types]
        self.types = [t if isinstance(t, FindingTypes) else FindingTypes[t] for t in types]
    else:
        self.types = None
    
    if status:
        if not isinstance(status, list):
            status = [status]
        self.status = [s if isinstance(s, FindingStatus) else FindingStatus[s] for s in status]
    else:
        self.status = None

    if categories:
        if not isinstance(categories, list):
            categories = [categories]
        self.categories = [c if isinstance(c, FindingCategory) else FindingCategory[c] for c in categories]
    else:
        self.categories = None
  
  @property
  def types(self):
     return self._types
  
  @types.setter
  def types(self, value):
    if value is not None:
      if not isinstance(value, list):
        value = [value]
      for item in value:
        if isinstance(item, str):
          if item not in FindingTypes.__members__:
            raise ValueError(f"{item} is not a valid FindingTypes")
        elif not isinstance(item, FindingTypes):
          raise TypeError(f"All items in types must be instances of FindingTypes or their string representation, got {type(item)}")
    self._types = value
  
  def _date_filter(self):
    """_summary_

    Returns:
        _type_: _description_
    """
    end = datetime.now()
    start = end - timedelta(days=self.days)
    return f'CreationTimeStart:"{start.strftime("%Y-%m-%dT%H:%M:%S")}",\nCreationTimeEnd:"{end.strftime("%Y-%m-%dT%H:%M:%S")}"\n'
  
  def _types_filter(self):
    if self.types:
        types_str = ', '.join(t.name if isinstance(t, FindingTypes) else t for t in self.types)
    else:
        types_str = ""
    return f"Types:[{types_str}],\n"
  
  def _categories_filter(self):
    categories_str = ', '.join(c.name for c in self.categories) if self.categories else ""
    return f"Categories:[{categories_str}],\n"
      
  def to_filter_string(self):
    filter_string = "filter:{\n"
    if self.types:
        filter_string += self._types_filter()
    if self.categories:
        filter_string += self._categories_filter()
    if self.days:
        filter_string += self._date_filter()
    filter_string += "}"
    return filter_string