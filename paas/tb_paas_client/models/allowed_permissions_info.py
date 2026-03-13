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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.merged_user_permissions import MergedUserPermissions
from tb_paas_client.models.operation import Operation
from tb_paas_client.models.resource import Resource
from typing import Optional, Set
from typing_extensions import Self

class AllowedPermissionsInfo(BaseModel):
    """
    AllowedPermissionsInfo
    """ # noqa: E501
    operations_by_resource: Optional[Dict[str, List[Operation]]] = Field(default=None, description="Static map (vocabulary) of allowed operations by resource type", alias="operationsByResource")
    allowed_for_group_role_operations: Optional[List[Operation]] = Field(default=None, description="Static set (vocabulary) of allowed operations for group roles", alias="allowedForGroupRoleOperations")
    allowed_for_group_owner_only_operations: Optional[List[Operation]] = Field(default=None, description="Static set (vocabulary) of allowed operations for group owner", alias="allowedForGroupOwnerOnlyOperations")
    allowed_for_group_owner_only_group_operations: Optional[List[Operation]] = Field(default=None, description="Static set (vocabulary) of allowed group operations for group owner", alias="allowedForGroupOwnerOnlyGroupOperations")
    allowed_resources: Optional[List[Resource]] = Field(default=None, description="Static set (vocabulary) of all possibly allowed resources. Static and depends only on the authority of the user", alias="allowedResources")
    user_permissions: Optional[MergedUserPermissions] = Field(default=None, description="JSON object with merged permission for all generic and group roles assigned to all user groups the user belongs to", alias="userPermissions")
    user_owner_id: Optional[EntityId] = Field(default=None, description="Owner Id of the user (Tenant or Customer)", alias="userOwnerId")
    __properties: ClassVar[List[str]] = ["operationsByResource", "allowedForGroupRoleOperations", "allowedForGroupOwnerOnlyOperations", "allowedForGroupOwnerOnlyGroupOperations", "allowedResources", "userPermissions", "userOwnerId"]

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
        """Create an instance of AllowedPermissionsInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in operations_by_resource (dict of array)
        _field_dict_of_array = {}
        if self.operations_by_resource:
            for _key_operations_by_resource in self.operations_by_resource:
                if self.operations_by_resource[_key_operations_by_resource] is not None:
                    _field_dict_of_array[_key_operations_by_resource] = [
                        _item.to_dict() for _item in self.operations_by_resource[_key_operations_by_resource]
                    ]
            _dict['operationsByResource'] = _field_dict_of_array
        # override the default output from pydantic by calling `to_dict()` of user_permissions
        if self.user_permissions:
            _dict['userPermissions'] = self.user_permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_owner_id
        if self.user_owner_id:
            _dict['userOwnerId'] = self.user_owner_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AllowedPermissionsInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operationsByResource": dict(
                (_k,
                        [Operation.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("operationsByResource", {}).items()
            ),
            "allowedForGroupRoleOperations": obj.get("allowedForGroupRoleOperations"),
            "allowedForGroupOwnerOnlyOperations": obj.get("allowedForGroupOwnerOnlyOperations"),
            "allowedForGroupOwnerOnlyGroupOperations": obj.get("allowedForGroupOwnerOnlyGroupOperations"),
            "allowedResources": obj.get("allowedResources"),
            "userPermissions": MergedUserPermissions.from_dict(obj["userPermissions"]) if obj.get("userPermissions") is not None else None,
            "userOwnerId": EntityId.from_dict(obj["userOwnerId"]) if obj.get("userOwnerId") is not None else None
        })
        return _obj


