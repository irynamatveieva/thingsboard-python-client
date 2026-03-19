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

class TenantAddonData(BaseModel):
    """
    TenantAddonData
    """ # noqa: E501
    max_devices: Optional[StrictInt] = Field(default=None, alias="maxDevices")
    max_assets: Optional[StrictInt] = Field(default=None, alias="maxAssets")
    max_customers: Optional[StrictInt] = Field(default=None, alias="maxCustomers")
    max_users: Optional[StrictInt] = Field(default=None, alias="maxUsers")
    max_integrations: Optional[StrictInt] = Field(default=None, alias="maxIntegrations")
    max_converters: Optional[StrictInt] = Field(default=None, alias="maxConverters")
    max_calculated_fields_per_entity: Optional[StrictInt] = Field(default=None, alias="maxCalculatedFieldsPerEntity")
    max_transport_messages: Optional[StrictInt] = Field(default=None, alias="maxTransportMessages")
    max_transport_data_points: Optional[StrictInt] = Field(default=None, alias="maxTransportDataPoints")
    max_re_executions: Optional[StrictInt] = Field(default=None, alias="maxREExecutions")
    max_js_executions: Optional[StrictInt] = Field(default=None, alias="maxJSExecutions")
    max_dp_storage_days: Optional[StrictInt] = Field(default=None, alias="maxDPStorageDays")
    max_created_alarms: Optional[StrictInt] = Field(default=None, alias="maxCreatedAlarms")
    max_emails: Optional[StrictInt] = Field(default=None, alias="maxEmails")
    max_sms: Optional[StrictInt] = Field(default=None, alias="maxSms")
    max_ai_credits: Optional[StrictInt] = Field(default=None, alias="maxAiCredits")
    edge_enabled: Optional[StrictBool] = Field(default=None, alias="edgeEnabled")
    max_edges: Optional[StrictInt] = Field(default=None, alias="maxEdges")
    trendz_enabled: Optional[StrictBool] = Field(default=None, alias="trendzEnabled")
    white_labeling_enabled: Optional[StrictBool] = Field(default=None, alias="whiteLabelingEnabled")
    default: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["maxDevices", "maxAssets", "maxCustomers", "maxUsers", "maxIntegrations", "maxConverters", "maxCalculatedFieldsPerEntity", "maxTransportMessages", "maxTransportDataPoints", "maxREExecutions", "maxJSExecutions", "maxDPStorageDays", "maxCreatedAlarms", "maxEmails", "maxSms", "maxAiCredits", "edgeEnabled", "maxEdges", "trendzEnabled", "whiteLabelingEnabled", "default"]

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
        """Create an instance of TenantAddonData from a JSON string"""
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
        """Create an instance of TenantAddonData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maxDevices": obj.get("maxDevices"),
            "maxAssets": obj.get("maxAssets"),
            "maxCustomers": obj.get("maxCustomers"),
            "maxUsers": obj.get("maxUsers"),
            "maxIntegrations": obj.get("maxIntegrations"),
            "maxConverters": obj.get("maxConverters"),
            "maxCalculatedFieldsPerEntity": obj.get("maxCalculatedFieldsPerEntity"),
            "maxTransportMessages": obj.get("maxTransportMessages"),
            "maxTransportDataPoints": obj.get("maxTransportDataPoints"),
            "maxREExecutions": obj.get("maxREExecutions"),
            "maxJSExecutions": obj.get("maxJSExecutions"),
            "maxDPStorageDays": obj.get("maxDPStorageDays"),
            "maxCreatedAlarms": obj.get("maxCreatedAlarms"),
            "maxEmails": obj.get("maxEmails"),
            "maxSms": obj.get("maxSms"),
            "maxAiCredits": obj.get("maxAiCredits"),
            "edgeEnabled": obj.get("edgeEnabled"),
            "maxEdges": obj.get("maxEdges"),
            "trendzEnabled": obj.get("trendzEnabled"),
            "whiteLabelingEnabled": obj.get("whiteLabelingEnabled"),
            "default": obj.get("default")
        })
        return _obj


