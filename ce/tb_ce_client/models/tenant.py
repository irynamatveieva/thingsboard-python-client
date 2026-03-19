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
from tb_ce_client.models.tenant_id import TenantId
from tb_ce_client.models.tenant_profile_id import TenantProfileId
from typing import Optional, Set
from typing_extensions import Self

class Tenant(BaseModel):
    """
    A JSON value representing the tenant.
    """ # noqa: E501
    id: Optional[TenantId] = Field(default=None, description="JSON object with the tenant Id. Specify this field to update the tenant. Referencing non-existing tenant Id will cause error. Omit this field to create new tenant.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the tenant creation, in milliseconds", alias="createdTime")
    country: Optional[StrictStr] = Field(default=None, description="Country")
    state: Optional[StrictStr] = Field(default=None, description="State")
    city: Optional[StrictStr] = Field(default=None, description="City")
    address: Optional[StrictStr] = Field(default=None, description="Address Line 1")
    address2: Optional[StrictStr] = Field(default=None, description="Address Line 2")
    zip: Optional[StrictStr] = Field(default=None, description="Zip code")
    phone: Optional[StrictStr] = Field(default=None, description="Phone number")
    email: Optional[StrictStr] = Field(default=None, description="Email")
    title: StrictStr = Field(description="Title of the tenant")
    region: Optional[StrictStr] = Field(default=None, description="Geo region of the tenant")
    tenant_profile_id: Optional[TenantProfileId] = Field(default=None, description="JSON object with Tenant Profile Id", alias="tenantProfileId")
    version: Optional[StrictInt] = None
    additional_info: Optional[Any] = Field(default=None, description="Additional parameters of the tenant. May include: 'description' (string), 'homeDashboardId' (string, UUID of the home dashboard), 'homeDashboardHideToolbar' (boolean, whether to hide the dashboard toolbar).", alias="additionalInfo")
    name: Optional[StrictStr] = Field(default=None, description="Name of the tenant. Read-only, duplicated from title for backward compatibility")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "country", "state", "city", "address", "address2", "zip", "phone", "email", "title", "region", "tenantProfileId", "version", "additionalInfo", "name"]

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
        """Create an instance of Tenant from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tenant_profile_id
        if self.tenant_profile_id:
            _dict['tenantProfileId'] = self.tenant_profile_id.to_dict()
        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Tenant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": TenantId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "country": obj.get("country"),
            "state": obj.get("state"),
            "city": obj.get("city"),
            "address": obj.get("address"),
            "address2": obj.get("address2"),
            "zip": obj.get("zip"),
            "phone": obj.get("phone"),
            "email": obj.get("email"),
            "title": obj.get("title"),
            "region": obj.get("region"),
            "tenantProfileId": TenantProfileId.from_dict(obj["tenantProfileId"]) if obj.get("tenantProfileId") is not None else None,
            "version": obj.get("version"),
            "additionalInfo": obj.get("additionalInfo"),
            "name": obj.get("name")
        })
        return _obj


