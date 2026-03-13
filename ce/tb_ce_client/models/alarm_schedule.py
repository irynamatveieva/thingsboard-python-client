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
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_ce_client.models.alarm_schedule_type import AlarmScheduleType
from tb_ce_client.models.dynamic_value_string import DynamicValueString
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_ce_client.models.any_time_schedule import AnyTimeSchedule
    from tb_ce_client.models.custom_time_schedule import CustomTimeSchedule
    from tb_ce_client.models.specific_time_schedule import SpecificTimeSchedule

class AlarmSchedule(BaseModel):
    """
    Configuration for alarm schedule
    """ # noqa: E501
    type: Optional[AlarmScheduleType] = None
    dynamic_value: Optional[DynamicValueString] = Field(default=None, alias="dynamicValue")
    __properties: ClassVar[List[str]] = ["type", "dynamicValue"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ANY_TIME': 'AnyTimeSchedule','CUSTOM': 'CustomTimeSchedule','SPECIFIC_TIME': 'SpecificTimeSchedule'
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
    def from_json(cls, json_str: str) -> Optional[Union[AnyTimeSchedule, CustomTimeSchedule, SpecificTimeSchedule]]:
        """Create an instance of AlarmSchedule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dynamic_value
        if self.dynamic_value:
            _dict['dynamicValue'] = self.dynamic_value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[AnyTimeSchedule, CustomTimeSchedule, SpecificTimeSchedule]]:
        """Create an instance of AlarmSchedule from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'AnyTimeSchedule':
            return import_module("tb_ce_client.models.any_time_schedule").AnyTimeSchedule.from_dict(obj)
        if object_type ==  'CustomTimeSchedule':
            return import_module("tb_ce_client.models.custom_time_schedule").CustomTimeSchedule.from_dict(obj)
        if object_type ==  'SpecificTimeSchedule':
            return import_module("tb_ce_client.models.specific_time_schedule").SpecificTimeSchedule.from_dict(obj)

        raise ValueError("AlarmSchedule failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


