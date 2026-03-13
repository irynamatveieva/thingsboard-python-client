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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.authority import Authority
from tb_pe_client.models.custom_menu_id import CustomMenuId
from tb_pe_client.models.customer_id import CustomerId
from tb_pe_client.models.entity_id import EntityId
from tb_pe_client.models.tenant_id import TenantId
from tb_pe_client.models.user_id import UserId
from typing import Optional, Set
from typing_extensions import Self

class User(BaseModel):
    """
    A JSON value representing the User.
    """ # noqa: E501
    id: Optional[UserId] = Field(default=None, description="JSON object with the User Id. Specify this field to update the device. Referencing non-existing User Id will cause error. Omit this field to create new customer.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the user creation, in milliseconds", alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with the Tenant Id.", alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, description="JSON object with the Customer Id.", alias="customerId")
    email: StrictStr = Field(description="Email of the user")
    authority: Authority = Field(description="Authority")
    first_name: Optional[StrictStr] = Field(default=None, description="First name of the user", alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, description="Last name of the user", alias="lastName")
    phone: Optional[StrictStr] = Field(default=None, description="Phone number of the user")
    custom_menu_id: Optional[CustomMenuId] = Field(default=None, alias="customMenuId")
    version: Optional[StrictInt] = None
    name: Optional[StrictStr] = Field(default=None, description="Duplicates the email of the user, readonly")
    owner_id: Optional[EntityId] = Field(default=None, description="JSON object with Customer or Tenant Id", alias="ownerId")
    additional_info: Optional[Any] = Field(default=None, description="Additional parameters of the user. May include: 'defaultDashboardId' (string, UUID of the default dashboard), 'defaultDashboardFullscreen' (boolean), 'homeDashboardId' (string, UUID of the home dashboard), 'homeDashboardHideToolbar' (boolean), 'lang' (string, user locale, e.g. 'en_US'), 'authProviderName' (string, name of the authentication provider).", alias="additionalInfo")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "customerId", "email", "authority", "firstName", "lastName", "phone", "customMenuId", "version", "name", "ownerId", "additionalInfo"]

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
        """Create an instance of User from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "name",
            "owner_id",
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
        # override the default output from pydantic by calling `to_dict()` of custom_menu_id
        if self.custom_menu_id:
            _dict['customMenuId'] = self.custom_menu_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner_id
        if self.owner_id:
            _dict['ownerId'] = self.owner_id.to_dict()
        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": UserId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customerId": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "email": obj.get("email"),
            "authority": obj.get("authority"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "phone": obj.get("phone"),
            "customMenuId": CustomMenuId.from_dict(obj["customMenuId"]) if obj.get("customMenuId") is not None else None,
            "version": obj.get("version"),
            "name": obj.get("name"),
            "ownerId": EntityId.from_dict(obj["ownerId"]) if obj.get("ownerId") is not None else None,
            "additionalInfo": obj.get("additionalInfo")
        })
        return _obj


