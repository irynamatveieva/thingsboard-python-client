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
from tb_paas_client.models.entity_group_id import EntityGroupId
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.entity_type import EntityType
from tb_paas_client.models.group_permission_id import GroupPermissionId
from tb_paas_client.models.role import Role
from tb_paas_client.models.role_id import RoleId
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class GroupPermissionInfo(BaseModel):
    """
    GroupPermissionInfo
    """ # noqa: E501
    id: Optional[GroupPermissionId] = Field(default=None, description="JSON object with the Group Permission Id. Specify this field to update the Group Permission. Referencing non-existing Group Permission Id will cause error. Omit this field to create new Group Permission.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the group permission creation, in milliseconds", alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with the Tenant Id.", alias="tenantId")
    user_group_id: EntityGroupId = Field(description="JSON object with the User Group Id. Represents the user group that will have permissions to perform operations against the corresponding entity group.", alias="userGroupId")
    role_id: RoleId = Field(description="JSON object with the Role Id. Represents the set of permissions. The role type (GENERIC or GROUP) determines whether 'entityGroupId' is required.", alias="roleId")
    entity_group_id: Optional[EntityGroupId] = Field(default=None, description="JSON object with the Entity Group Id. Required when using a GROUP role — specifies the entity group to which the permissions apply. Must be null or omitted when using a GENERIC role.", alias="entityGroupId")
    entity_group_type: Optional[EntityType] = Field(default=None, description="Type of the entities in the group: DEVICE, ASSET, CUSTOMER, etc. Auto-populated from the referenced entity group. Null for generic permissions.", alias="entityGroupType")
    role: Optional[Role] = Field(default=None, description="Represent set of permissions.")
    entity_group_name: Optional[StrictStr] = Field(default=None, description="Entity Group Name.", alias="entityGroupName")
    entity_group_owner_id: Optional[EntityId] = Field(default=None, description="Entity Group Owner Id (Tenant or Customer).", alias="entityGroupOwnerId")
    entity_group_owner_name: Optional[StrictStr] = Field(default=None, description="Name of the entity group owner (Tenant or Customer title).", alias="entityGroupOwnerName")
    user_group_name: Optional[StrictStr] = Field(default=None, description="User Group Name.", alias="userGroupName")
    user_group_owner_id: Optional[EntityId] = Field(default=None, description="User Group Owner Id (Tenant or Customer).", alias="userGroupOwnerId")
    user_group_owner_name: Optional[StrictStr] = Field(default=None, description="Name of the user group owner (Tenant or Customer title).", alias="userGroupOwnerName")
    name: Optional[StrictStr] = Field(default=None, description="Name of the Group Permissions. Auto-generated")
    public: Optional[StrictBool] = None
    read_only: Optional[StrictBool] = Field(default=None, alias="readOnly")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "userGroupId", "roleId", "entityGroupId", "entityGroupType", "role", "entityGroupName", "entityGroupOwnerId", "entityGroupOwnerName", "userGroupName", "userGroupOwnerId", "userGroupOwnerName", "name", "public", "readOnly"]

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
        """Create an instance of GroupPermissionInfo from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "entity_group_type",
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
        # override the default output from pydantic by calling `to_dict()` of user_group_id
        if self.user_group_id:
            _dict['userGroupId'] = self.user_group_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of role_id
        if self.role_id:
            _dict['roleId'] = self.role_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entity_group_id
        if self.entity_group_id:
            _dict['entityGroupId'] = self.entity_group_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of role
        if self.role:
            _dict['role'] = self.role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entity_group_owner_id
        if self.entity_group_owner_id:
            _dict['entityGroupOwnerId'] = self.entity_group_owner_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_group_owner_id
        if self.user_group_owner_id:
            _dict['userGroupOwnerId'] = self.user_group_owner_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GroupPermissionInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": GroupPermissionId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "userGroupId": EntityGroupId.from_dict(obj["userGroupId"]) if obj.get("userGroupId") is not None else None,
            "roleId": RoleId.from_dict(obj["roleId"]) if obj.get("roleId") is not None else None,
            "entityGroupId": EntityGroupId.from_dict(obj["entityGroupId"]) if obj.get("entityGroupId") is not None else None,
            "entityGroupType": obj.get("entityGroupType"),
            "role": Role.from_dict(obj["role"]) if obj.get("role") is not None else None,
            "entityGroupName": obj.get("entityGroupName"),
            "entityGroupOwnerId": EntityId.from_dict(obj["entityGroupOwnerId"]) if obj.get("entityGroupOwnerId") is not None else None,
            "entityGroupOwnerName": obj.get("entityGroupOwnerName"),
            "userGroupName": obj.get("userGroupName"),
            "userGroupOwnerId": EntityId.from_dict(obj["userGroupOwnerId"]) if obj.get("userGroupOwnerId") is not None else None,
            "userGroupOwnerName": obj.get("userGroupOwnerName"),
            "name": obj.get("name"),
            "public": obj.get("public"),
            "readOnly": obj.get("readOnly")
        })
        return _obj


