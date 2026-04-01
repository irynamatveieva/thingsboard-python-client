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

class SubscriptionItems(BaseModel):
    """
    SubscriptionItems
    """ # noqa: E501
    extra_device_pack_count: Optional[StrictInt] = Field(default=None, serialization_alias="extraDevicePackCount")
    extra_customer_pack_count: Optional[StrictInt] = Field(default=None, serialization_alias="extraCustomerPackCount")
    extra_integration_pack_count: Optional[StrictInt] = Field(default=None, serialization_alias="extraIntegrationPackCount")
    extra_calculated_field_count: Optional[StrictInt] = Field(default=None, serialization_alias="extraCalculatedFieldCount")
    traffic_pack_count: Optional[StrictInt] = Field(default=None, serialization_alias="trafficPackCount")
    compute_pack_count: Optional[StrictInt] = Field(default=None, serialization_alias="computePackCount")
    storage_pack_count: Optional[StrictInt] = Field(default=None, serialization_alias="storagePackCount")
    alarm_pack_count: Optional[StrictInt] = Field(default=None, serialization_alias="alarmPackCount")
    email_pack_count: Optional[StrictInt] = Field(default=None, serialization_alias="emailPackCount")
    sms_pack_count: Optional[StrictInt] = Field(default=None, serialization_alias="smsPackCount")
    ai_credits_pack_count: Optional[StrictInt] = Field(default=None, serialization_alias="aiCreditsPackCount")
    edge_enabled: Optional[StrictBool] = Field(default=None, serialization_alias="edgeEnabled")
    extra_edge_count: Optional[StrictInt] = Field(default=None, serialization_alias="extraEdgeCount")
    trendz_enabled: Optional[StrictBool] = Field(default=None, serialization_alias="trendzEnabled")
    white_labeling_addon_enabled: Optional[StrictBool] = Field(default=None, serialization_alias="whiteLabelingAddonEnabled")
    __properties: ClassVar[List[str]] = ["extraDevicePackCount", "extraCustomerPackCount", "extraIntegrationPackCount", "extraCalculatedFieldCount", "trafficPackCount", "computePackCount", "storagePackCount", "alarmPackCount", "emailPackCount", "smsPackCount", "aiCreditsPackCount", "edgeEnabled", "extraEdgeCount", "trendzEnabled", "whiteLabelingAddonEnabled"]

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
        """Create an instance of SubscriptionItems from a JSON string"""
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
        """Create an instance of SubscriptionItems from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "extra_device_pack_count": obj.get("extraDevicePackCount"),
            "extra_customer_pack_count": obj.get("extraCustomerPackCount"),
            "extra_integration_pack_count": obj.get("extraIntegrationPackCount"),
            "extra_calculated_field_count": obj.get("extraCalculatedFieldCount"),
            "traffic_pack_count": obj.get("trafficPackCount"),
            "compute_pack_count": obj.get("computePackCount"),
            "storage_pack_count": obj.get("storagePackCount"),
            "alarm_pack_count": obj.get("alarmPackCount"),
            "email_pack_count": obj.get("emailPackCount"),
            "sms_pack_count": obj.get("smsPackCount"),
            "ai_credits_pack_count": obj.get("aiCreditsPackCount"),
            "edge_enabled": obj.get("edgeEnabled"),
            "extra_edge_count": obj.get("extraEdgeCount"),
            "trendz_enabled": obj.get("trendzEnabled"),
            "white_labeling_addon_enabled": obj.get("whiteLabelingAddonEnabled")
        })
        return _obj


