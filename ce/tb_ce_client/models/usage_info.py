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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UsageInfo(BaseModel):
    """
    UsageInfo
    """ # noqa: E501
    devices: Optional[StrictInt] = None
    max_devices: Optional[StrictInt] = Field(default=None, alias="maxDevices")
    assets: Optional[StrictInt] = None
    max_assets: Optional[StrictInt] = Field(default=None, alias="maxAssets")
    customers: Optional[StrictInt] = None
    max_customers: Optional[StrictInt] = Field(default=None, alias="maxCustomers")
    users: Optional[StrictInt] = None
    max_users: Optional[StrictInt] = Field(default=None, alias="maxUsers")
    dashboards: Optional[StrictInt] = None
    max_dashboards: Optional[StrictInt] = Field(default=None, alias="maxDashboards")
    edges: Optional[StrictInt] = None
    max_edges: Optional[StrictInt] = Field(default=None, alias="maxEdges")
    transport_messages: Optional[StrictInt] = Field(default=None, alias="transportMessages")
    max_transport_messages: Optional[StrictInt] = Field(default=None, alias="maxTransportMessages")
    js_executions: Optional[StrictInt] = Field(default=None, alias="jsExecutions")
    tbel_executions: Optional[StrictInt] = Field(default=None, alias="tbelExecutions")
    max_js_executions: Optional[StrictInt] = Field(default=None, alias="maxJsExecutions")
    max_tbel_executions: Optional[StrictInt] = Field(default=None, alias="maxTbelExecutions")
    emails: Optional[StrictInt] = None
    max_emails: Optional[StrictInt] = Field(default=None, alias="maxEmails")
    sms: Optional[StrictInt] = None
    max_sms: Optional[StrictInt] = Field(default=None, alias="maxSms")
    sms_enabled: Optional[StrictBool] = Field(default=None, alias="smsEnabled")
    alarms: Optional[StrictInt] = None
    max_alarms: Optional[StrictInt] = Field(default=None, alias="maxAlarms")
    __properties: ClassVar[List[str]] = ["devices", "maxDevices", "assets", "maxAssets", "customers", "maxCustomers", "users", "maxUsers", "dashboards", "maxDashboards", "edges", "maxEdges", "transportMessages", "maxTransportMessages", "jsExecutions", "tbelExecutions", "maxJsExecutions", "maxTbelExecutions", "emails", "maxEmails", "sms", "maxSms", "smsEnabled", "alarms", "maxAlarms"]

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
        """Create an instance of UsageInfo from a JSON string"""
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
        """Create an instance of UsageInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "devices": obj.get("devices"),
            "maxDevices": obj.get("maxDevices"),
            "assets": obj.get("assets"),
            "maxAssets": obj.get("maxAssets"),
            "customers": obj.get("customers"),
            "maxCustomers": obj.get("maxCustomers"),
            "users": obj.get("users"),
            "maxUsers": obj.get("maxUsers"),
            "dashboards": obj.get("dashboards"),
            "maxDashboards": obj.get("maxDashboards"),
            "edges": obj.get("edges"),
            "maxEdges": obj.get("maxEdges"),
            "transportMessages": obj.get("transportMessages"),
            "maxTransportMessages": obj.get("maxTransportMessages"),
            "jsExecutions": obj.get("jsExecutions"),
            "tbelExecutions": obj.get("tbelExecutions"),
            "maxJsExecutions": obj.get("maxJsExecutions"),
            "maxTbelExecutions": obj.get("maxTbelExecutions"),
            "emails": obj.get("emails"),
            "maxEmails": obj.get("maxEmails"),
            "sms": obj.get("sms"),
            "maxSms": obj.get("maxSms"),
            "smsEnabled": obj.get("smsEnabled"),
            "alarms": obj.get("alarms"),
            "maxAlarms": obj.get("maxAlarms")
        })
        return _obj


