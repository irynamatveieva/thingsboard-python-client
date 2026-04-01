#
# Copyright © 2026-2026 ThingsBoard, Inc.
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

from pydantic import ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.alarm_schedule import AlarmSchedule
from tb_ce_client.models.alarm_schedule_type import AlarmScheduleType
from tb_ce_client.models.dynamic_value_string import DynamicValueString
from typing import Optional, Set
from typing_extensions import Self

class SpecificTimeSchedule(AlarmSchedule):
    """
    SpecificTimeSchedule
    """ # noqa: E501
    days_of_week: Optional[List[StrictInt]] = Field(default=None, serialization_alias="daysOfWeek")
    ends_on: Optional[StrictInt] = Field(default=None, serialization_alias="endsOn")
    starts_on: Optional[StrictInt] = Field(default=None, serialization_alias="startsOn")
    timezone: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["dynamicValue", "type", "daysOfWeek", "endsOn", "startsOn", "timezone"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.model_dump(by_alias=False, mode='json'))

    def __str__(self) -> str:
        return self.to_str()

    def __repr__(self) -> str:
        return self.to_str()

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SpecificTimeSchedule from a JSON string"""
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpecificTimeSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dynamic_value": DynamicValueString.from_dict(obj["dynamicValue"]) if obj.get("dynamicValue") is not None else None,
            "type": obj.get("type"),
            "days_of_week": obj.get("daysOfWeek"),
            "ends_on": obj.get("endsOn"),
            "starts_on": obj.get("startsOn"),
            "timezone": obj.get("timezone")
        })
        return _obj


