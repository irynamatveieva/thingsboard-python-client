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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tb_paas_client.models.mobile_app_id import MobileAppId
from tb_paas_client.models.mobile_app_status import MobileAppStatus
from tb_paas_client.models.mobile_app_version_info import MobileAppVersionInfo
from tb_paas_client.models.platform_type import PlatformType
from tb_paas_client.models.store_info import StoreInfo
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class MobileApp(BaseModel):
    """
    A JSON value representing the Mobile Application.
    """ # noqa: E501
    id: Optional[MobileAppId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", serialization_alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id", serialization_alias="tenantId")
    pkg_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Application package name. Cannot be empty", serialization_alias="pkgName")
    title: Optional[StrictStr] = Field(default=None, description="Application title")
    app_secret: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Application secret. The length must be at least 16 characters", serialization_alias="appSecret")
    platform_type: PlatformType = Field(description="Application platform type: ANDROID or IOS", serialization_alias="platformType")
    status: MobileAppStatus = Field(description="Application status: PUBLISHED, DEPRECATED, SUSPENDED, DRAFT")
    version_info: Optional[MobileAppVersionInfo] = Field(default=None, description="Application version info", serialization_alias="versionInfo")
    store_info: Optional[StoreInfo] = Field(default=None, description="Application store information", serialization_alias="storeInfo")
    name: Optional[StrictStr] = Field(default=None, description="Mobile app package name")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "pkgName", "title", "appSecret", "platformType", "status", "versionInfo", "storeInfo", "name"]

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
        """Create an instance of MobileApp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of version_info
        if self.version_info:
            _dict['versionInfo'] = self.version_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of store_info
        if self.store_info:
            _dict['storeInfo'] = self.store_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MobileApp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": MobileAppId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "pkg_name": obj.get("pkgName"),
            "title": obj.get("title"),
            "app_secret": obj.get("appSecret"),
            "platform_type": obj.get("platformType"),
            "status": obj.get("status"),
            "version_info": MobileAppVersionInfo.from_dict(obj["versionInfo"]) if obj.get("versionInfo") is not None else None,
            "store_info": StoreInfo.from_dict(obj["storeInfo"]) if obj.get("storeInfo") is not None else None,
            "name": obj.get("name")
        })
        return _obj


