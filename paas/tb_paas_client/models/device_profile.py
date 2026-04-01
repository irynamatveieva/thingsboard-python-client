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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.dashboard_id import DashboardId
from tb_paas_client.models.device_profile_data import DeviceProfileData
from tb_paas_client.models.device_profile_id import DeviceProfileId
from tb_paas_client.models.device_profile_provision_type import DeviceProfileProvisionType
from tb_paas_client.models.device_profile_type import DeviceProfileType
from tb_paas_client.models.device_transport_type import DeviceTransportType
from tb_paas_client.models.ota_package_id import OtaPackageId
from tb_paas_client.models.rule_chain_id import RuleChainId
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class DeviceProfile(BaseModel):
    """
    A JSON value representing the device profile.
    """ # noqa: E501
    id: Optional[DeviceProfileId] = Field(default=None, description="JSON object with the device profile Id. Specify this field to update the device profile. Referencing non-existing device profile Id will cause error. Omit this field to create new device profile.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the profile creation, in milliseconds", serialization_alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id that owns the profile.", serialization_alias="tenantId")
    name: Optional[StrictStr] = Field(default=None, description="Unique Device Profile Name in scope of Tenant.")
    description: Optional[StrictStr] = Field(default=None, description="Device Profile description. ")
    image: Optional[StrictStr] = Field(default=None, description="Either URL or Base64 data of the icon. Used in the mobile application to visualize set of device profiles in the grid view. ")
    type: Optional[DeviceProfileType] = Field(default=None, description="Type of the profile. Always 'DEFAULT' for now. Reserved for future use.")
    transport_type: Optional[DeviceTransportType] = Field(default=None, description="Type of the transport used to connect the device. Default transport supports HTTP, CoAP and MQTT.", serialization_alias="transportType")
    provision_type: Optional[DeviceProfileProvisionType] = Field(default=None, description="Provisioning strategy.", serialization_alias="provisionType")
    default_rule_chain_id: Optional[RuleChainId] = Field(default=None, description="Reference to the rule chain. If present, the specified rule chain will be used to process all messages related to device, including telemetry, attribute updates, etc. Otherwise, the root rule chain will be used to process those messages.", serialization_alias="defaultRuleChainId")
    default_dashboard_id: Optional[DashboardId] = Field(default=None, description="Reference to the dashboard. Used in the mobile application to open the default dashboard when user navigates to device details.", serialization_alias="defaultDashboardId")
    default_queue_name: Optional[StrictStr] = Field(default=None, description="Rule engine queue name. If present, the specified queue will be used to store all unprocessed messages related to device, including telemetry, attribute updates, etc. Otherwise, the 'Main' queue will be used to store those messages.", serialization_alias="defaultQueueName")
    profile_data: Optional[DeviceProfileData] = Field(default=None, description="Complex JSON object that includes addition device profile configuration (transport, alarm rules, etc).", serialization_alias="profileData")
    provision_device_key: Optional[StrictStr] = Field(default=None, description="Unique provisioning key used by 'Device Provisioning' feature.", serialization_alias="provisionDeviceKey")
    firmware_id: Optional[OtaPackageId] = Field(default=None, description="Reference to the firmware OTA package. If present, the specified package will be used as default device firmware. ", serialization_alias="firmwareId")
    software_id: Optional[OtaPackageId] = Field(default=None, description="Reference to the software OTA package. If present, the specified package will be used as default device software. ", serialization_alias="softwareId")
    default_edge_rule_chain_id: Optional[RuleChainId] = Field(default=None, description="Reference to the edge rule chain. If present, the specified edge rule chain will be used on the edge to process all messages related to device, including telemetry, attribute updates, etc. Otherwise, the edge root rule chain will be used to process those messages.", serialization_alias="defaultEdgeRuleChainId")
    version: Optional[StrictInt] = None
    default: Optional[StrictBool] = Field(default=None, description="Used to mark the default profile. Default profile is used when the device profile is not specified during device creation.")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "name", "description", "image", "type", "transportType", "provisionType", "defaultRuleChainId", "defaultDashboardId", "defaultQueueName", "profileData", "provisionDeviceKey", "firmwareId", "softwareId", "defaultEdgeRuleChainId", "version", "default"]

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
        """Create an instance of DeviceProfile from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
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
        # override the default output from pydantic by calling `to_dict()` of default_rule_chain_id
        if self.default_rule_chain_id:
            _dict['defaultRuleChainId'] = self.default_rule_chain_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_dashboard_id
        if self.default_dashboard_id:
            _dict['defaultDashboardId'] = self.default_dashboard_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of profile_data
        if self.profile_data:
            _dict['profileData'] = self.profile_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of firmware_id
        if self.firmware_id:
            _dict['firmwareId'] = self.firmware_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of software_id
        if self.software_id:
            _dict['softwareId'] = self.software_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_edge_rule_chain_id
        if self.default_edge_rule_chain_id:
            _dict['defaultEdgeRuleChainId'] = self.default_edge_rule_chain_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": DeviceProfileId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "name": obj.get("name"),
            "description": obj.get("description"),
            "image": obj.get("image"),
            "type": obj.get("type"),
            "transport_type": obj.get("transportType"),
            "provision_type": obj.get("provisionType"),
            "default_rule_chain_id": RuleChainId.from_dict(obj["defaultRuleChainId"]) if obj.get("defaultRuleChainId") is not None else None,
            "default_dashboard_id": DashboardId.from_dict(obj["defaultDashboardId"]) if obj.get("defaultDashboardId") is not None else None,
            "default_queue_name": obj.get("defaultQueueName"),
            "profile_data": DeviceProfileData.from_dict(obj["profileData"]) if obj.get("profileData") is not None else None,
            "provision_device_key": obj.get("provisionDeviceKey"),
            "firmware_id": OtaPackageId.from_dict(obj["firmwareId"]) if obj.get("firmwareId") is not None else None,
            "software_id": OtaPackageId.from_dict(obj["softwareId"]) if obj.get("softwareId") is not None else None,
            "default_edge_rule_chain_id": RuleChainId.from_dict(obj["defaultEdgeRuleChainId"]) if obj.get("defaultEdgeRuleChainId") is not None else None,
            "version": obj.get("version"),
            "default": obj.get("default")
        })
        return _obj


