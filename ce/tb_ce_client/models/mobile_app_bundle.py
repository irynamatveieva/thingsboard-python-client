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
from typing_extensions import Annotated
from tb_ce_client.models.mobile_app_bundle_id import MobileAppBundleId
from tb_ce_client.models.mobile_app_id import MobileAppId
from tb_ce_client.models.mobile_layout_config import MobileLayoutConfig
from tb_ce_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class MobileAppBundle(BaseModel):
    """
    A JSON value representing the Mobile Application Bundle.
    """ # noqa: E501
    id: Optional[MobileAppBundleId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id", alias="tenantId")
    title: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Application bundle title. Cannot be empty")
    description: Optional[StrictStr] = Field(default=None, description="Application bundle description.")
    android_app_id: Optional[MobileAppId] = Field(default=None, description="Android application id", alias="androidAppId")
    ios_app_id: Optional[MobileAppId] = Field(default=None, description="IOS application id", alias="iosAppId")
    layout_config: Optional[MobileLayoutConfig] = Field(default=None, description="Application layout configuration", alias="layoutConfig")
    oauth2_enabled: Optional[StrictBool] = Field(default=None, description="Whether OAuth2 settings are enabled or not", alias="oauth2Enabled")
    name: Optional[StrictStr] = Field(default=None, description="Mobile app bundle title")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "title", "description", "androidAppId", "iosAppId", "layoutConfig", "oauth2Enabled", "name"]

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
        """Create an instance of MobileAppBundle from a JSON string"""
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
            "name",
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
        # override the default output from pydantic by calling `to_dict()` of android_app_id
        if self.android_app_id:
            _dict['androidAppId'] = self.android_app_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ios_app_id
        if self.ios_app_id:
            _dict['iosAppId'] = self.ios_app_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of layout_config
        if self.layout_config:
            _dict['layoutConfig'] = self.layout_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MobileAppBundle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": MobileAppBundleId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "title": obj.get("title"),
            "description": obj.get("description"),
            "androidAppId": MobileAppId.from_dict(obj["androidAppId"]) if obj.get("androidAppId") is not None else None,
            "iosAppId": MobileAppId.from_dict(obj["iosAppId"]) if obj.get("iosAppId") is not None else None,
            "layoutConfig": MobileLayoutConfig.from_dict(obj["layoutConfig"]) if obj.get("layoutConfig") is not None else None,
            "oauth2Enabled": obj.get("oauth2Enabled"),
            "name": obj.get("name")
        })
        return _obj


