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

from enums.FindingSeverity import FindingSeverity
from enums.FindingTypes import FindingTypes
from enums.FindingCategory import FindingCategory
from enums.FindingStatus import FindingStatus
from enums.CloudProviders import CloudProviders


class FindingFilter:
    """
    Provides filtering capabilities for findings using various criteria such as
    days, types, categories, statuses, severities, and providers.

    Attributes:
    ----------
        days (int) :
            Number of days for the filter. It determines the time range for creation dates.
        types (List[FindingTypes] | FindingTypes):
            Finding types for the filter.
        categories (FindingCategory):
            Categories of findings for the filter.
        statuses (FindingStatus):
            Statuses for the filter, default is 'Open'.
        severities (List[FindingSeverity] | FindingSeverity):
            Severity levels for the filter.
        providers (List[CloudProviders] | CloudProviders):
            Cloud providers for the filter.
        findings_ids (List[str] | str):
            List of specific finding ids or a single Id. Can be set and get
    """

    def __init__(
        self,
        days: int = None,
        resource_ids: List[str] | str = None,
        findings_ids: List[str] | str = None,
        types: List[FindingTypes] | FindingTypes = None,
        categories: FindingCategory = None,
        statuses: FindingStatus = None,
        severities: List[FindingSeverity] | FindingSeverity = None,
        providers: List[CloudProviders] | CloudProviders = None
    ):
        """Constructs all the necessary attributes for the class

        Parameters
        ----------
        days : int, optional
            Converts to date range for findings. 30 days means get findings from the past month, by default None
        types : List[FindingTypes] | FindingTypes, optional
            Finding types, by default None
        categories : FindingCategory, optional
            Finding Categories. Case sensitive, by default None
        statuses : FindingStatus, optional
            Finding status. Case sensitive, by default 'Open'
        severities : List[FindingSeverity] | FindingSeverity, optional
            Finding Severities, by default [ 'Critical', 'High']
        providers : List[CloudProviders] | CloudProviders, optional
            Cloud Providers, only AWS, Azure, and GCP, by default None
        resource_ids : List[str] | str, optional
            Resource Ids, these are cloud resource ids. Cloud be Arns or GUID etc. The parameter will accept a list of Ids, or a single Id
        findings_ids : List[str] | str, optional
            Findings Ids, these are Finding ids. The parameter will accept a list of Ids, or a single Id
        """
        self._days = days
        self.resource_ids = resource_ids
        self.findings_ids = findings_ids

        if resource_ids:
            if not isinstance(resource_ids, list):
                if isinstance(resource_ids, str) and ',' in resource_ids:
                    raise ValueError(
                        'If you need to provide a list of resource ids they must be in a List')
                resource_ids = [resource_ids]
            self.resource_ids = resource_ids

        if findings_ids:
            if not isinstance(findings_ids, list):
                if isinstance(findings_ids, str) and ',' in findings_ids:
                    raise ValueError(
                        'If you need to provide a list of findings ids they must be in a List')
                findings_ids = [findings_ids]
            self.findings_ids = findings_ids

        if types:
            self._types = []
            self.__initialize_attributes(self._types, types, FindingTypes)
        else:
            self._types = None

        if statuses:
            self._statuses = []
            self.__initialize_attributes(
                self._statuses, statuses, FindingStatus)
        else:
            self._statuses = None

        if categories:
            self._categories = []
            self.__initialize_attributes(
                self._categories, categories, FindingCategory)
        else:
            self._categories = None

        if severities:
            self._severities = []
            self.__initialize_attributes(
                self._severities, severities, FindingSeverity)
        else:
            self._severities = None

        if providers:
            self._providers = []
            self.__initialize_attributes(
                self._providers, providers, CloudProviders)
        else:
            self._providers = None

    @property
    def days(self):
        return self._days

    def __date_range(self):
        if self.days:
            end = datetime.now()
            start = end - timedelta(days=self.days)
            return f'CreationTimeStart:"{start.strftime("%Y-%m-%dT%H:%M:%S")}",\nCreationTimeEnd:"{end.strftime("%Y-%m-%dT%H:%M:%S")}"\n'
        return ""

    @days.setter
    def days(self, value: int):
        if value < 0:
            raise ValueError("Days can't be negative")
        self._days = value

    @property
    def types(self):
        return self._types

    @types.setter
    def types(self, value):
        value = self.__setter_helper(value=value, enum_type=FindingTypes)
        self._types = value

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        value = self.__setter_helper(value, FindingCategory)
        self._categories = value

    @property
    def statuses(self):
        return self._statuses

    @statuses.setter
    def statuses(self, value):
        value = self.__setter_helper(value, FindingStatus)
        self._statuses = value

    @property
    def severities(self):
        return self._severities

    @severities.setter
    def severities(self, value):
        value = self.__setter_helper(value, FindingSeverity)
        self._severities = value

    @property
    def providers(self):
        return self._providers

    @providers.setter
    def providers(self, value):
        value = self.__setter_helper(value, CloudProviders)
        self._providers = value

    def __setter_helper(self, value, enum_type: FindingCategory | FindingSeverity | FindingStatus | FindingTypes | CloudProviders):
        """Helper method for property setters to reduce DRY

        Parameters
        ----------
        value : List | FindingCategory | FindingSeverity | FindingStatus | FindingTypes | CloudProviders | str
        enum_type : FindingCategory | FindingSeverity | FindingStatus | FindingTypes | CloudProviders

        Returns
        -------
        List
            List of FindingCategory | FindingSeverity | FindingStatus | FindingTypes | CloudProviders

        Raises
        ------
        ValueError
            Raises Enum member error of the item isn't a valid member of the Enum
        TypeError
            Raises Enum Type error if items isn't an instance of the enum type provided or it's string representation
        """
        if value is not None:
            if not isinstance(value, list):
                value = [value]
            for item in value:
                if isinstance(item, str):
                    if item not in enum_type.__members__:
                        raise ValueError(f"{item} is not a valid {enum_type}")
                elif not isinstance(item, enum_type):
                    raise TypeError(
                        f"All items in types must be instances of {enum_type} or their string representation, got {type(item)}")
        return value

    def __initialize_attributes(self, prop, param, enum_type):
        """Helper function to reduce DRY. It takes the property, the parameter if entered, and the corresponding Enum Type and then sets the value"""
        if not isinstance(param, list):
            # if it's not a list then cast to list
            param = [param]
        for i in param:
            try:
                prop.append(i if isinstance(
                    i, enum_type) else enum_type[i])
            except KeyError:
                print(f'Invalid Type {i}')
                prop = None

    def __filter_string_helper(self, value, enum_type):
        """Helper method to join and stringify the Enum list 

        Returns
        -------
        str
            stringified filter element
        """
        if value:
            filter_str = ', '.join(v.name if isinstance(
                v, enum_type) else v for v in value)
        else:
            filter_str = ""
        return filter_str

    def to_filter_string(self):
        """This method concatenates the different filter elements into a single filter for GraphQL API

        Returns
        -------
        str
            GraphQL filter string
        """
        filter_string = "filter:{\n"
        if self.types:
            types_str = self.__filter_string_helper(self.types, FindingTypes)
            filter_string += f"Types:[{types_str}],\n"
        if self.categories:
            categories_str = self.__filter_string_helper(
                self.categories, FindingCategory)
            filter_string += f"Categories:[{categories_str}],\n"
        if self.statuses:
            value = self.__filter_string_helper(self.statuses, FindingStatus)
            filter_string += f"Statuses:[{value}],\n"
        if self.severities:
            value = self.__filter_string_helper(
                self.severities, FindingSeverity)
            filter_string += f"Severities:[{value}],\n"
        if self.providers:
            value = self.__filter_string_helper(self.providers, CloudProviders)
            filter_string += f"CloudProviders:[{value}],\n"
        if self.days:
            filter_string += self.__date_range()
        if self.resource_ids:
            if self.resource_ids:
                if not isinstance(self.resource_ids, list):
                    self.resource_ids = [self.resource_ids]
                filter_str = ', '.join(
                    f'"{resource_id}"' for resource_id in self.resource_ids)
            else:
                filter_str = ""
            filter_string += f"ResourceIds:[{filter_str}],\n"
        if self.findings_ids:
            if self.findings_ids:
                if not isinstance(self.findings_ids, list):
                    self.findings_ids = [self.findings_ids]
                filter_str = ', '.join(
                    f'"{finding_id}"' for finding_id in self.findings_ids)
            else:
                filter_str = ""
            filter_string += f"Ids:[{filter_str}]\n"
        filter_string += "}"
        return filter_string
