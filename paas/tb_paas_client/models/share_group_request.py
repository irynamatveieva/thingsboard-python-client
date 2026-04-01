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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.entity_group_id import EntityGroupId
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.role_id import RoleId
from typing import Optional, Set
from typing_extensions import Self

class ShareGroupRequest(BaseModel):
    """
    The Share Group Request JSON
    """ # noqa: E501
    owner_id: Optional[EntityId] = Field(default=None, description="In case 'allUserGroup' is set to true, this property specifies the owner of the user group 'All'. Either Tenant or Customer Id.", serialization_alias="ownerId")
    all_user_group: StrictBool = Field(description="Indicate that the group should be shared with user group 'All' that belongs to Tenant or Customer (see 'ownerId' property description).", serialization_alias="allUserGroup")
    user_group_id: Optional[EntityGroupId] = Field(default=None, description="In case 'allUserGroup' is set to false, this property specifies the specific user group that the entity group should be shared with.", serialization_alias="userGroupId")
    read_else_write: Optional[StrictBool] = Field(default=None, description="Used if 'roleIds' property is not present. if the value is 'true', creates role with read-only permissions. If the value is 'false', creates role with write permissions.", serialization_alias="readElseWrite")
    role_ids: Optional[List[RoleId]] = Field(default=None, description="List of group role Ids that should be used to share the entity group with the user group. If not set, the platform will create new role (see 'readElseWrite' property description)", serialization_alias="roleIds")
    __properties: ClassVar[List[str]] = ["ownerId", "allUserGroup", "userGroupId", "readElseWrite", "roleIds"]

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
        """Create an instance of ShareGroupRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of owner_id
        if self.owner_id:
            _dict['ownerId'] = self.owner_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_group_id
        if self.user_group_id:
            _dict['userGroupId'] = self.user_group_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in role_ids (list)
        _items = []
        if self.role_ids:
            for _item_role_ids in self.role_ids:
                if _item_role_ids:
                    _items.append(_item_role_ids.to_dict())
            _dict['roleIds'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShareGroupRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "owner_id": EntityId.from_dict(obj["ownerId"]) if obj.get("ownerId") is not None else None,
            "all_user_group": obj.get("allUserGroup"),
            "user_group_id": EntityGroupId.from_dict(obj["userGroupId"]) if obj.get("userGroupId") is not None else None,
            "read_else_write": obj.get("readElseWrite"),
            "role_ids": [RoleId.from_dict(_item) for _item in obj["roleIds"]] if obj.get("roleIds") is not None else None
        })
        return _obj


