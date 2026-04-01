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
from tb_ce_client.models.tenant_profile_data import TenantProfileData
from tb_ce_client.models.tenant_profile_id import TenantProfileId
from typing import Optional, Set
from typing_extensions import Self

class TenantProfile(BaseModel):
    """
    A JSON value representing the tenant profile.
    """ # noqa: E501
    id: Optional[TenantProfileId] = Field(default=None, description="JSON object with the tenant profile Id. Specify this field to update the tenant profile. Referencing non-existing tenant profile Id will cause error. Omit this field to create new tenant profile.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the tenant profile creation, in milliseconds", serialization_alias="createdTime")
    name: Optional[StrictStr] = Field(default=None, description="Name of the tenant profile")
    description: Optional[StrictStr] = Field(default=None, description="Description of the tenant profile")
    default: Optional[StrictBool] = Field(default=None, description="Default Tenant profile to be used.")
    isolated_tb_rule_engine: Optional[StrictBool] = Field(default=None, description="If enabled, will push all messages related to this tenant and processed by the rule engine into separate queue. Useful for complex microservices deployments, to isolate processing of the data for specific tenants", serialization_alias="isolatedTbRuleEngine")
    profile_data: Optional[TenantProfileData] = Field(default=None, serialization_alias="profileData")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "name", "description", "default", "isolatedTbRuleEngine", "profileData"]

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
        """Create an instance of TenantProfile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of profile_data
        if self.profile_data:
            _dict['profileData'] = self.profile_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": TenantProfileId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "default": obj.get("default"),
            "isolated_tb_rule_engine": obj.get("isolatedTbRuleEngine"),
            "profile_data": TenantProfileData.from_dict(obj["profileData"]) if obj.get("profileData") is not None else None
        })
        return _obj


