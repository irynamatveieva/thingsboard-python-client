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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.customer_id import CustomerId
from tb_ce_client.models.device_data import DeviceData
from tb_ce_client.models.device_id import DeviceId
from tb_ce_client.models.device_profile_id import DeviceProfileId
from tb_ce_client.models.ota_package_id import OtaPackageId
from tb_ce_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class DeviceInfo(BaseModel):
    """
    DeviceInfo
    """ # noqa: E501
    id: Optional[DeviceId] = Field(default=None, description="JSON object with the Device Id. Specify this field to update the Device. Referencing non-existing Device Id will cause error. Omit this field to create new Device.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the device creation, in milliseconds", alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id. Use 'assignDeviceToTenant' to change the Tenant Id.", alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, description="JSON object with Customer Id. Use 'assignDeviceToCustomer' to change the Customer Id.", alias="customerId")
    name: StrictStr = Field(description="Unique Device Name in scope of Tenant")
    type: Optional[StrictStr] = Field(default=None, description="Device Profile Name")
    label: Optional[StrictStr] = Field(default=None, description="Label that may be used in widgets")
    device_profile_id: DeviceProfileId = Field(description="JSON object with Device Profile Id.", alias="deviceProfileId")
    firmware_id: Optional[OtaPackageId] = Field(default=None, description="JSON object with Ota Package Id.", alias="firmwareId")
    software_id: Optional[OtaPackageId] = Field(default=None, description="JSON object with Ota Package Id.", alias="softwareId")
    version: Optional[StrictInt] = None
    customer_title: Optional[StrictStr] = Field(default=None, description="Title of the Customer that owns the device.", alias="customerTitle")
    customer_is_public: Optional[StrictBool] = Field(default=None, description="Indicates special 'Public' Customer that is auto-generated to use the devices on public dashboards.", alias="customerIsPublic")
    device_profile_name: Optional[StrictStr] = Field(default=None, description="Name of the corresponding Device Profile.", alias="deviceProfileName")
    active: Optional[StrictBool] = Field(default=None, description="Device active flag.")
    additional_info: Optional[Any] = Field(default=None, description="Additional parameters of the device. May include: 'gateway' (boolean, whether the device is a gateway), 'description' (string), 'lastConnectedGateway' (string, UUID of the last gateway that connected this device).", alias="additionalInfo")
    device_data: Optional[DeviceData] = Field(default=None, description="JSON object with content specific to type of transport in the device profile.", alias="deviceData")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "customerId", "name", "type", "label", "deviceProfileId", "firmwareId", "softwareId", "version", "customerTitle", "customerIsPublic", "deviceProfileName", "active", "additionalInfo", "deviceData"]

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
        """Create an instance of DeviceInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "customer_id",
            "customer_title",
            "customer_is_public",
            "device_profile_name",
            "active",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenantId'] = self.tenant_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_id
        if self.customer_id:
            _dict['customerId'] = self.customer_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device_profile_id
        if self.device_profile_id:
            _dict['deviceProfileId'] = self.device_profile_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of firmware_id
        if self.firmware_id:
            _dict['firmwareId'] = self.firmware_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of software_id
        if self.software_id:
            _dict['softwareId'] = self.software_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device_data
        if self.device_data:
            _dict['deviceData'] = self.device_data.to_dict()
        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": DeviceId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customerId": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "name": obj.get("name"),
            "type": obj.get("type"),
            "label": obj.get("label"),
            "deviceProfileId": DeviceProfileId.from_dict(obj["deviceProfileId"]) if obj.get("deviceProfileId") is not None else None,
            "firmwareId": OtaPackageId.from_dict(obj["firmwareId"]) if obj.get("firmwareId") is not None else None,
            "softwareId": OtaPackageId.from_dict(obj["softwareId"]) if obj.get("softwareId") is not None else None,
            "version": obj.get("version"),
            "customerTitle": obj.get("customerTitle"),
            "customerIsPublic": obj.get("customerIsPublic"),
            "deviceProfileName": obj.get("deviceProfileName"),
            "active": obj.get("active"),
            "additionalInfo": obj.get("additionalInfo"),
            "deviceData": DeviceData.from_dict(obj["deviceData"]) if obj.get("deviceData") is not None else None
        })
        return _obj


