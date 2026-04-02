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
    max_devices: Optional[StrictInt] = Field(default=None, serialization_alias="maxDevices")
    max_assets: Optional[StrictInt] = Field(default=None, serialization_alias="maxAssets")
    max_customers: Optional[StrictInt] = Field(default=None, serialization_alias="maxCustomers")
    max_users: Optional[StrictInt] = Field(default=None, serialization_alias="maxUsers")
    max_integrations: Optional[StrictInt] = Field(default=None, serialization_alias="maxIntegrations")
    max_converters: Optional[StrictInt] = Field(default=None, serialization_alias="maxConverters")
    max_calculated_fields_per_entity: Optional[StrictInt] = Field(default=None, serialization_alias="maxCalculatedFieldsPerEntity")
    max_transport_messages: Optional[StrictInt] = Field(default=None, serialization_alias="maxTransportMessages")
    max_transport_data_points: Optional[StrictInt] = Field(default=None, serialization_alias="maxTransportDataPoints")
    max_re_executions: Optional[StrictInt] = Field(default=None, serialization_alias="maxREExecutions")
    max_js_executions: Optional[StrictInt] = Field(default=None, serialization_alias="maxJSExecutions")
    max_dp_storage_days: Optional[StrictInt] = Field(default=None, serialization_alias="maxDPStorageDays")
    max_created_alarms: Optional[StrictInt] = Field(default=None, serialization_alias="maxCreatedAlarms")
    max_emails: Optional[StrictInt] = Field(default=None, serialization_alias="maxEmails")
    max_sms: Optional[StrictInt] = Field(default=None, serialization_alias="maxSms")
    max_ai_credits: Optional[StrictInt] = Field(default=None, serialization_alias="maxAiCredits")
    edge_enabled: Optional[StrictBool] = Field(default=None, serialization_alias="edgeEnabled")
    max_edges: Optional[StrictInt] = Field(default=None, serialization_alias="maxEdges")
    trendz_enabled: Optional[StrictBool] = Field(default=None, serialization_alias="trendzEnabled")
    white_labeling_enabled: Optional[StrictBool] = Field(default=None, serialization_alias="whiteLabelingEnabled")
    default: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["maxDevices", "maxAssets", "maxCustomers", "maxUsers", "maxIntegrations", "maxConverters", "maxCalculatedFieldsPerEntity", "maxTransportMessages", "maxTransportDataPoints", "maxREExecutions", "maxJSExecutions", "maxDPStorageDays", "maxCreatedAlarms", "maxEmails", "maxSms", "maxAiCredits", "edgeEnabled", "maxEdges", "trendzEnabled", "whiteLabelingEnabled", "default"]

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
            "max_devices": obj.get("maxDevices"),
            "max_assets": obj.get("maxAssets"),
            "max_customers": obj.get("maxCustomers"),
            "max_users": obj.get("maxUsers"),
            "max_integrations": obj.get("maxIntegrations"),
            "max_converters": obj.get("maxConverters"),
            "max_calculated_fields_per_entity": obj.get("maxCalculatedFieldsPerEntity"),
            "max_transport_messages": obj.get("maxTransportMessages"),
            "max_transport_data_points": obj.get("maxTransportDataPoints"),
            "max_re_executions": obj.get("maxREExecutions"),
            "max_js_executions": obj.get("maxJSExecutions"),
            "max_dp_storage_days": obj.get("maxDPStorageDays"),
            "max_created_alarms": obj.get("maxCreatedAlarms"),
            "max_emails": obj.get("maxEmails"),
            "max_sms": obj.get("maxSms"),
            "max_ai_credits": obj.get("maxAiCredits"),
            "edge_enabled": obj.get("edgeEnabled"),
            "max_edges": obj.get("maxEdges"),
            "trendz_enabled": obj.get("trendzEnabled"),
            "white_labeling_enabled": obj.get("whiteLabelingEnabled"),
            "default": obj.get("default")
        })
        return _obj


