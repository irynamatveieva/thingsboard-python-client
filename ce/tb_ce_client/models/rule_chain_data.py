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
from typing import Any, ClassVar, Dict, List
from tb_ce_client.models.rule_chain import RuleChain
from tb_ce_client.models.rule_chain_meta_data import RuleChainMetaData
from typing import Optional, Set
from typing_extensions import Self

class RuleChainData(BaseModel):
    """
    A JSON value representing the rule chains.
    """ # noqa: E501
    rule_chains: List[RuleChain] = Field(description="List of the Rule Chain objects.", alias="ruleChains")
    metadata: List[RuleChainMetaData] = Field(description="List of the Rule Chain metadata objects.")
    __properties: ClassVar[List[str]] = ["ruleChains", "metadata"]

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
        """Create an instance of RuleChainData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rule_chains (list)
        _items = []
        if self.rule_chains:
            for _item_rule_chains in self.rule_chains:
                if _item_rule_chains:
                    _items.append(_item_rule_chains.to_dict())
            _dict['ruleChains'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item_metadata in self.metadata:
                if _item_metadata:
                    _items.append(_item_metadata.to_dict())
            _dict['metadata'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RuleChainData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ruleChains": [RuleChain.from_dict(_item) for _item in obj["ruleChains"]] if obj.get("ruleChains") is not None else None,
            "metadata": [RuleChainMetaData.from_dict(_item) for _item in obj["metadata"]] if obj.get("metadata") is not None else None
        })
        return _obj


