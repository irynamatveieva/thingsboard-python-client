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
from tb_ce_client.models.dashboard_id import DashboardId
from tb_ce_client.models.device_profile_type import DeviceProfileType
from tb_ce_client.models.device_transport_type import DeviceTransportType
from tb_ce_client.models.entity_id import EntityId
from tb_ce_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class DeviceProfileInfo(BaseModel):
    """
    DeviceProfileInfo
    """ # noqa: E501
    id: Optional[EntityId] = Field(default=None, description="JSON object with the entity Id. ")
    name: Optional[StrictStr] = Field(default=None, description="Entity Name")
    image: Optional[StrictStr] = Field(default=None, description="Either URL or Base64 data of the icon. Used in the mobile application to visualize set of device profiles in the grid view. ")
    default_dashboard_id: Optional[DashboardId] = Field(default=None, description="Reference to the dashboard. Used in the mobile application to open the default dashboard when user navigates to device details.", alias="defaultDashboardId")
    type: Optional[DeviceProfileType] = Field(default=None, description="Type of the profile. Always 'DEFAULT' for now. Reserved for future use.")
    transport_type: Optional[DeviceTransportType] = Field(default=None, description="Type of the transport used to connect the device. Default transport supports HTTP, CoAP and MQTT.", alias="transportType")
    tenant_id: Optional[TenantId] = Field(default=None, description="Tenant id.", alias="tenantId")
    __properties: ClassVar[List[str]] = ["id", "name", "image", "defaultDashboardId", "type", "transportType", "tenantId"]

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
        """Create an instance of DeviceProfileInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_dashboard_id
        if self.default_dashboard_id:
            _dict['defaultDashboardId'] = self.default_dashboard_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenantId'] = self.tenant_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceProfileInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": EntityId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "name": obj.get("name"),
            "image": obj.get("image"),
            "defaultDashboardId": DashboardId.from_dict(obj["defaultDashboardId"]) if obj.get("defaultDashboardId") is not None else None,
            "type": obj.get("type"),
            "transportType": obj.get("transportType"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None
        })
        return _obj


