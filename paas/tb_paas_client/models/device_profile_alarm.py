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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.alarm_rule import AlarmRule
from typing import Optional, Set
from typing_extensions import Self

class DeviceProfileAlarm(BaseModel):
    """
    DeviceProfileAlarm
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="String value representing the alarm rule id")
    alarm_type: Optional[StrictStr] = Field(default=None, description="String value representing type of the alarm", alias="alarmType")
    create_rules: Optional[Dict[str, AlarmRule]] = Field(default=None, description="Complex JSON object representing create alarm rules. The unique create alarm rule can be created for each alarm severity type. There can be 5 create alarm rules configured per a single alarm type. See method implementation notes and AlarmRule model for more details", alias="createRules")
    clear_rule: Optional[AlarmRule] = Field(default=None, description="JSON object representing clear alarm rule", alias="clearRule")
    propagate: Optional[StrictBool] = Field(default=None, description="Propagation flag to specify if alarm should be propagated to parent entities of alarm originator")
    propagate_to_owner: Optional[StrictBool] = Field(default=None, description="Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) of alarm originator", alias="propagateToOwner")
    propagate_to_owner_hierarchy: Optional[StrictBool] = Field(default=None, description="Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) and all parent owners in the customer hierarchy", alias="propagateToOwnerHierarchy")
    propagate_to_tenant: Optional[StrictBool] = Field(default=None, description="Propagation flag to specify if alarm should be propagated to the tenant entity", alias="propagateToTenant")
    propagate_relation_types: Optional[List[StrictStr]] = Field(default=None, description="JSON array of relation types that should be used for propagation. By default, 'propagateRelationTypes' array is empty which means that the alarm will be propagated based on any relation type to parent entities. This parameter should be used only in case when 'propagate' parameter is set to true, otherwise, 'propagateRelationTypes' array will be ignored.", alias="propagateRelationTypes")
    __properties: ClassVar[List[str]] = ["id", "alarmType", "createRules", "clearRule", "propagate", "propagateToOwner", "propagateToOwnerHierarchy", "propagateToTenant", "propagateRelationTypes"]

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
        """Create an instance of DeviceProfileAlarm from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in create_rules (dict)
        _field_dict = {}
        if self.create_rules:
            for _key_create_rules in self.create_rules:
                if self.create_rules[_key_create_rules]:
                    _field_dict[_key_create_rules] = self.create_rules[_key_create_rules].to_dict()
            _dict['createRules'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of clear_rule
        if self.clear_rule:
            _dict['clearRule'] = self.clear_rule.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceProfileAlarm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "alarmType": obj.get("alarmType"),
            "createRules": dict(
                (_k, AlarmRule.from_dict(_v))
                for _k, _v in obj["createRules"].items()
            )
            if obj.get("createRules") is not None
            else None,
            "clearRule": AlarmRule.from_dict(obj["clearRule"]) if obj.get("clearRule") is not None else None,
            "propagate": obj.get("propagate"),
            "propagateToOwner": obj.get("propagateToOwner"),
            "propagateToOwnerHierarchy": obj.get("propagateToOwnerHierarchy"),
            "propagateToTenant": obj.get("propagateToTenant"),
            "propagateRelationTypes": obj.get("propagateRelationTypes")
        })
        return _obj


