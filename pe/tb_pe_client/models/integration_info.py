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
from tb_pe_client.models.debug_settings import DebugSettings
from tb_pe_client.models.integration_id import IntegrationId
from tb_pe_client.models.integration_type import IntegrationType
from tb_pe_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class IntegrationInfo(BaseModel):
    """
    IntegrationInfo
    """ # noqa: E501
    id: Optional[IntegrationId] = Field(default=None, description="JSON object with the Integration Id. Specify this field to update the Integration. Referencing non-existing Integration Id will cause error. Omit this field to create new Integration.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the integration creation, in milliseconds", serialization_alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id", serialization_alias="tenantId")
    name: StrictStr = Field(description="Integration Name")
    type: IntegrationType = Field(description="The type of the integration")
    debug_mode: Optional[StrictBool] = Field(default=None, description="Enable/disable debug. ", serialization_alias="debugMode")
    debug_settings: Optional[DebugSettings] = Field(default=None, description="Debug settings object.", serialization_alias="debugSettings")
    enabled: Optional[StrictBool] = Field(default=None, description="Boolean flag to enable/disable the integration")
    remote: Optional[StrictBool] = Field(default=None, description="Boolean flag to enable/disable the integration to be executed remotely. Remote integration is launched in a separate microservice. Local integration is executed by the platform core")
    allow_create_devices_or_assets: Optional[StrictBool] = Field(default=None, description="Boolean flag to allow/disallow the integration to create devices or assets that send message and do not exist in the system yet", serialization_alias="allowCreateDevicesOrAssets")
    edge_template: Optional[StrictBool] = Field(default=None, description="Boolean flag that specifies that is regular or edge template integration", serialization_alias="edgeTemplate")
    version: Optional[StrictInt] = None
    status: Optional[Dict[str, Any]] = None
    stats: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "name", "type", "debugMode", "debugSettings", "enabled", "remote", "allowCreateDevicesOrAssets", "edgeTemplate", "version", "status", "stats"]

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
        """Create an instance of IntegrationInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of debug_settings
        if self.debug_settings:
            _dict['debugSettings'] = self.debug_settings.to_dict()
        # set to None if stats (nullable) is None
        # and model_fields_set contains the field
        if self.stats is None and "stats" in self.model_fields_set:
            _dict['stats'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IntegrationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": IntegrationId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "name": obj.get("name"),
            "type": obj.get("type"),
            "debug_mode": obj.get("debugMode"),
            "debug_settings": DebugSettings.from_dict(obj["debugSettings"]) if obj.get("debugSettings") is not None else None,
            "enabled": obj.get("enabled"),
            "remote": obj.get("remote"),
            "allow_create_devices_or_assets": obj.get("allowCreateDevicesOrAssets"),
            "edge_template": obj.get("edgeTemplate"),
            "version": obj.get("version"),
            "status": obj.get("status"),
            "stats": obj.get("stats")
        })
        return _obj


