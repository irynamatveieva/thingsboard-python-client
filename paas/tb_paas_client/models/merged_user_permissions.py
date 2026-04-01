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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.merged_group_permission_info import MergedGroupPermissionInfo
from tb_paas_client.models.merged_group_type_permission_info import MergedGroupTypePermissionInfo
from tb_paas_client.models.operation import Operation
from typing import Optional, Set
from typing_extensions import Self

class MergedUserPermissions(BaseModel):
    """
    MergedUserPermissions
    """ # noqa: E501
    generic_permissions: Optional[Dict[str, List[Operation]]] = Field(default=None, description="Map of permissions defined using generic roles ('Customer Administrator', etc)", serialization_alias="genericPermissions")
    group_permissions: Optional[Dict[str, MergedGroupPermissionInfo]] = Field(default=None, description="Map of permissions defined using group roles ('Read' or 'Write' access to specific entity group, etc)", serialization_alias="groupPermissions")
    read_group_permissions: Optional[Dict[str, MergedGroupTypePermissionInfo]] = Field(default=None, description="Map of read permissions per entity type. Used on the UI to enable/disable certain components.", serialization_alias="readGroupPermissions")
    read_entity_permissions: Optional[Dict[str, MergedGroupTypePermissionInfo]] = Field(default=None, description="Map of read permissions per resource. Used on the UI to enable/disable certain components.", serialization_alias="readEntityPermissions")
    read_attr_permissions: Optional[Dict[str, MergedGroupTypePermissionInfo]] = Field(default=None, description="Map of read entity attributes permissions per resource. Used on the UI to enable/disable certain tabs.", serialization_alias="readAttrPermissions")
    read_ts_permissions: Optional[Dict[str, MergedGroupTypePermissionInfo]] = Field(default=None, description="Map of read entity time-series permissions per resource. Used on the UI to enable/disable certain tabs.", serialization_alias="readTsPermissions")
    __properties: ClassVar[List[str]] = ["genericPermissions", "groupPermissions", "readGroupPermissions", "readEntityPermissions", "readAttrPermissions", "readTsPermissions"]

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
        """Create an instance of MergedUserPermissions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in generic_permissions (dict of array)
        _field_dict_of_array = {}
        if self.generic_permissions:
            for _key_generic_permissions in self.generic_permissions:
                if self.generic_permissions[_key_generic_permissions] is not None:
                    _field_dict_of_array[_key_generic_permissions] = [
                        _item.to_dict() for _item in self.generic_permissions[_key_generic_permissions]
                    ]
            _dict['genericPermissions'] = _field_dict_of_array
        # override the default output from pydantic by calling `to_dict()` of each value in group_permissions (dict)
        _field_dict = {}
        if self.group_permissions:
            for _key_group_permissions in self.group_permissions:
                if self.group_permissions[_key_group_permissions]:
                    _field_dict[_key_group_permissions] = self.group_permissions[_key_group_permissions].to_dict()
            _dict['groupPermissions'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in read_group_permissions (dict)
        _field_dict = {}
        if self.read_group_permissions:
            for _key_read_group_permissions in self.read_group_permissions:
                if self.read_group_permissions[_key_read_group_permissions]:
                    _field_dict[_key_read_group_permissions] = self.read_group_permissions[_key_read_group_permissions].to_dict()
            _dict['readGroupPermissions'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in read_entity_permissions (dict)
        _field_dict = {}
        if self.read_entity_permissions:
            for _key_read_entity_permissions in self.read_entity_permissions:
                if self.read_entity_permissions[_key_read_entity_permissions]:
                    _field_dict[_key_read_entity_permissions] = self.read_entity_permissions[_key_read_entity_permissions].to_dict()
            _dict['readEntityPermissions'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in read_attr_permissions (dict)
        _field_dict = {}
        if self.read_attr_permissions:
            for _key_read_attr_permissions in self.read_attr_permissions:
                if self.read_attr_permissions[_key_read_attr_permissions]:
                    _field_dict[_key_read_attr_permissions] = self.read_attr_permissions[_key_read_attr_permissions].to_dict()
            _dict['readAttrPermissions'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in read_ts_permissions (dict)
        _field_dict = {}
        if self.read_ts_permissions:
            for _key_read_ts_permissions in self.read_ts_permissions:
                if self.read_ts_permissions[_key_read_ts_permissions]:
                    _field_dict[_key_read_ts_permissions] = self.read_ts_permissions[_key_read_ts_permissions].to_dict()
            _dict['readTsPermissions'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MergedUserPermissions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "generic_permissions": dict(
                (_k,
                        [Operation.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("genericPermissions", {}).items()
            ),
            "groupPermissions": dict(
                (_k, MergedGroupPermissionInfo.from_dict(_v))
                for _k, _v in obj["groupPermissions"].items()
            )
            if obj.get("groupPermissions") is not None
            else None,
            "readGroupPermissions": dict(
                (_k, MergedGroupTypePermissionInfo.from_dict(_v))
                for _k, _v in obj["readGroupPermissions"].items()
            )
            if obj.get("readGroupPermissions") is not None
            else None,
            "readEntityPermissions": dict(
                (_k, MergedGroupTypePermissionInfo.from_dict(_v))
                for _k, _v in obj["readEntityPermissions"].items()
            )
            if obj.get("readEntityPermissions") is not None
            else None,
            "readAttrPermissions": dict(
                (_k, MergedGroupTypePermissionInfo.from_dict(_v))
                for _k, _v in obj["readAttrPermissions"].items()
            )
            if obj.get("readAttrPermissions") is not None
            else None,
            "readTsPermissions": dict(
                (_k, MergedGroupTypePermissionInfo.from_dict(_v))
                for _k, _v in obj["readTsPermissions"].items()
            )
            if obj.get("readTsPermissions") is not None
            else None
        })
        return _obj


