#
# Copyright 2026 ThingsBoard, Inc.
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
#
# noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from importlib import import_module
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_ce_client.models.custom_interval import CustomInterval
    from tb_ce_client.models.day_interval import DayInterval
    from tb_ce_client.models.hour_interval import HourInterval
    from tb_ce_client.models.month_interval import MonthInterval
    from tb_ce_client.models.quarter_interval import QuarterInterval
    from tb_ce_client.models.week_interval import WeekInterval
    from tb_ce_client.models.week_sun_sat_interval import WeekSunSatInterval
    from tb_ce_client.models.year_interval import YearInterval

class AggInterval(BaseModel):
    """
    AggInterval
    """ # noqa: E501
    type: StrictStr
    __properties: ClassVar[List[str]] = ["type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'CUSTOM': 'CustomInterval','DAY': 'DayInterval','HOUR': 'HourInterval','MONTH': 'MonthInterval','QUARTER': 'QuarterInterval','WEEK': 'WeekInterval','WEEK_SUN_SAT': 'WeekSunSatInterval','YEAR': 'YearInterval'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[CustomInterval, DayInterval, HourInterval, MonthInterval, QuarterInterval, WeekInterval, WeekSunSatInterval, YearInterval]]:
        """Create an instance of AggInterval from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[CustomInterval, DayInterval, HourInterval, MonthInterval, QuarterInterval, WeekInterval, WeekSunSatInterval, YearInterval]]:
        """Create an instance of AggInterval from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'CustomInterval':
            return import_module("tb_ce_client.models.custom_interval").CustomInterval.from_dict(obj)
        if object_type ==  'DayInterval':
            return import_module("tb_ce_client.models.day_interval").DayInterval.from_dict(obj)
        if object_type ==  'HourInterval':
            return import_module("tb_ce_client.models.hour_interval").HourInterval.from_dict(obj)
        if object_type ==  'MonthInterval':
            return import_module("tb_ce_client.models.month_interval").MonthInterval.from_dict(obj)
        if object_type ==  'QuarterInterval':
            return import_module("tb_ce_client.models.quarter_interval").QuarterInterval.from_dict(obj)
        if object_type ==  'WeekInterval':
            return import_module("tb_ce_client.models.week_interval").WeekInterval.from_dict(obj)
        if object_type ==  'WeekSunSatInterval':
            return import_module("tb_ce_client.models.week_sun_sat_interval").WeekSunSatInterval.from_dict(obj)
        if object_type ==  'YearInterval':
            return import_module("tb_ce_client.models.year_interval").YearInterval.from_dict(obj)

        raise ValueError("AggInterval failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


