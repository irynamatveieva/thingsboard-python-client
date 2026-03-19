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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.alarm_condition import AlarmCondition
from tb_ce_client.models.alarm_schedule import AlarmSchedule
from tb_ce_client.models.dashboard_id import DashboardId
from typing import Optional, Set
from typing_extensions import Self

class AlarmRule(BaseModel):
    """
    AlarmRule
    """ # noqa: E501
    condition: Optional[AlarmCondition] = Field(default=None, description="JSON object representing the alarm rule condition")
    alarm_details: Optional[StrictStr] = Field(default=None, description="String value representing the additional details for an alarm rule", alias="alarmDetails")
    dashboard_id: Optional[DashboardId] = Field(default=None, description="JSON object with the dashboard Id representing the reference to alarm details dashboard used by mobile application", alias="dashboardId")
    schedule: Optional[AlarmSchedule] = Field(default=None, description="JSON object representing time interval during which the rule is active")
    __properties: ClassVar[List[str]] = ["condition", "alarmDetails", "dashboardId", "schedule"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AlarmRule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of condition
        if self.condition:
            _dict['condition'] = self.condition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dashboard_id
        if self.dashboard_id:
            _dict['dashboardId'] = self.dashboard_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlarmRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "condition": AlarmCondition.from_dict(obj["condition"]) if obj.get("condition") is not None else None,
            "alarmDetails": obj.get("alarmDetails"),
            "dashboardId": DashboardId.from_dict(obj["dashboardId"]) if obj.get("dashboardId") is not None else None,
            "schedule": AlarmSchedule.from_dict(obj["schedule"]) if obj.get("schedule") is not None else None
        })
        return _obj


