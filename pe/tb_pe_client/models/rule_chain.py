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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.rule_chain_id import RuleChainId
from tb_pe_client.models.rule_chain_type import RuleChainType
from tb_pe_client.models.rule_node_id import RuleNodeId
from tb_pe_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class RuleChain(BaseModel):
    """
    A JSON value representing the rule chain.
    """ # noqa: E501
    id: Optional[RuleChainId] = Field(default=None, description="JSON object with the Rule Chain Id. Specify this field to update the Rule Chain. Referencing non-existing Rule Chain Id will cause error. Omit this field to create new rule chain.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the rule chain creation, in milliseconds", alias="createdTime")
    tenant_id: TenantId = Field(description="JSON object with Tenant Id.", alias="tenantId")
    name: StrictStr = Field(description="Rule Chain name")
    type: Optional[RuleChainType] = Field(default=None, description="Rule Chain type. 'EDGE' rule chains are processing messages on the edge devices only.")
    first_rule_node_id: Optional[RuleNodeId] = Field(default=None, description="JSON object with Rule Chain Id. Pointer to the first rule node that should receive all messages pushed to this rule chain.", alias="firstRuleNodeId")
    root: Optional[StrictBool] = Field(default=None, description="Indicates root rule chain. The root rule chain process messages from all devices and entities by default. User may configure default rule chain per device profile.")
    debug_mode: Optional[StrictBool] = Field(default=None, description="Reserved for future usage.", alias="debugMode")
    version: Optional[StrictInt] = None
    configuration: Optional[Any] = None
    additional_info: Optional[Any] = Field(default=None, alias="additionalInfo")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "name", "type", "firstRuleNodeId", "root", "debugMode", "version", "configuration", "additionalInfo"]

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
        """Create an instance of RuleChain from a JSON string"""
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
            "tenant_id",
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
        # override the default output from pydantic by calling `to_dict()` of first_rule_node_id
        if self.first_rule_node_id:
            _dict['firstRuleNodeId'] = self.first_rule_node_id.to_dict()
        # set to None if configuration (nullable) is None
        # and model_fields_set contains the field
        if self.configuration is None and "configuration" in self.model_fields_set:
            _dict['configuration'] = None

        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RuleChain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": RuleChainId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "name": obj.get("name"),
            "type": obj.get("type"),
            "firstRuleNodeId": RuleNodeId.from_dict(obj["firstRuleNodeId"]) if obj.get("firstRuleNodeId") is not None else None,
            "root": obj.get("root"),
            "debugMode": obj.get("debugMode"),
            "version": obj.get("version"),
            "configuration": obj.get("configuration"),
            "additionalInfo": obj.get("additionalInfo")
        })
        return _obj


