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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionUsage(BaseModel):
    """
    SubscriptionUsage
    """ # noqa: E501
    devices: Optional[StrictInt] = None
    assets: Optional[StrictInt] = None
    customers: Optional[StrictInt] = None
    users: Optional[StrictInt] = None
    dashboards: Optional[StrictInt] = None
    rule_chains: Optional[StrictInt] = Field(default=None, alias="ruleChains")
    integrations: Optional[StrictInt] = None
    converters: Optional[StrictInt] = None
    scheduler_events: Optional[StrictInt] = Field(default=None, alias="schedulerEvents")
    edges: Optional[StrictInt] = None
    transport_messages: Optional[StrictInt] = Field(default=None, alias="transportMessages")
    transport_data_points: Optional[StrictInt] = Field(default=None, alias="transportDataPoints")
    re_executions: Optional[StrictInt] = Field(default=None, alias="reExecutions")
    js_executions: Optional[StrictInt] = Field(default=None, alias="jsExecutions")
    dp_storage_days: Optional[StrictInt] = Field(default=None, alias="dpStorageDays")
    emails: Optional[StrictInt] = None
    sms: Optional[StrictInt] = None
    alarms: Optional[StrictInt] = None
    reports: Optional[StrictInt] = None
    ai_credits: Optional[StrictInt] = Field(default=None, alias="aiCredits")
    __properties: ClassVar[List[str]] = ["devices", "assets", "customers", "users", "dashboards", "ruleChains", "integrations", "converters", "schedulerEvents", "edges", "transportMessages", "transportDataPoints", "reExecutions", "jsExecutions", "dpStorageDays", "emails", "sms", "alarms", "reports", "aiCredits"]

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
        """Create an instance of SubscriptionUsage from a JSON string"""
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionUsage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "devices": obj.get("devices"),
            "assets": obj.get("assets"),
            "customers": obj.get("customers"),
            "users": obj.get("users"),
            "dashboards": obj.get("dashboards"),
            "ruleChains": obj.get("ruleChains"),
            "integrations": obj.get("integrations"),
            "converters": obj.get("converters"),
            "schedulerEvents": obj.get("schedulerEvents"),
            "edges": obj.get("edges"),
            "transportMessages": obj.get("transportMessages"),
            "transportDataPoints": obj.get("transportDataPoints"),
            "reExecutions": obj.get("reExecutions"),
            "jsExecutions": obj.get("jsExecutions"),
            "dpStorageDays": obj.get("dpStorageDays"),
            "emails": obj.get("emails"),
            "sms": obj.get("sms"),
            "alarms": obj.get("alarms"),
            "reports": obj.get("reports"),
            "aiCredits": obj.get("aiCredits")
        })
        return _obj


