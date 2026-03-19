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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from tb_ce_client.models.rule_chain_id import RuleChainId
from tb_ce_client.models.rule_node_id import RuleNodeId
from typing import Optional, Set
from typing_extensions import Self

class RuleChainOutputLabelsUsage(BaseModel):
    """
    RuleChainOutputLabelsUsage
    """ # noqa: E501
    rule_chain_id: RuleChainId = Field(description="Rule Chain Id", alias="ruleChainId")
    rule_node_id: RuleNodeId = Field(description="Rule Node Id", alias="ruleNodeId")
    rule_chain_name: StrictStr = Field(description="Rule Chain Name", alias="ruleChainName")
    rule_node_name: StrictStr = Field(description="Rule Node Name", alias="ruleNodeName")
    labels: List[StrictStr] = Field(description="Output labels")
    __properties: ClassVar[List[str]] = ["ruleChainId", "ruleNodeId", "ruleChainName", "ruleNodeName", "labels"]

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
        """Create an instance of RuleChainOutputLabelsUsage from a JSON string"""
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
            "rule_chain_id",
            "rule_node_id",
            "rule_chain_name",
            "rule_node_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of rule_chain_id
        if self.rule_chain_id:
            _dict['ruleChainId'] = self.rule_chain_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rule_node_id
        if self.rule_node_id:
            _dict['ruleNodeId'] = self.rule_node_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RuleChainOutputLabelsUsage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ruleChainId": RuleChainId.from_dict(obj["ruleChainId"]) if obj.get("ruleChainId") is not None else None,
            "ruleNodeId": RuleNodeId.from_dict(obj["ruleNodeId"]) if obj.get("ruleNodeId") is not None else None,
            "ruleChainName": obj.get("ruleChainName"),
            "ruleNodeName": obj.get("ruleNodeName"),
            "labels": obj.get("labels")
        })
        return _obj


