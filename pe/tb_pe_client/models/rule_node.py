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
from tb_pe_client.models.debug_settings import DebugSettings
from tb_pe_client.models.rule_chain_id import RuleChainId
from tb_pe_client.models.rule_node_id import RuleNodeId
from typing import Optional, Set
from typing_extensions import Self

class RuleNode(BaseModel):
    """
    RuleNode
    """ # noqa: E501
    id: Optional[RuleNodeId] = Field(default=None, description="JSON object with the Rule Node Id. Specify this field to update the Rule Node. Referencing non-existing Rule Node Id will cause error. Omit this field to create new rule node.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the rule node creation, in milliseconds", serialization_alias="createdTime")
    additional_info: Optional[Any] = Field(default=None, description="Additional parameters of the rule node. May include: 'layoutX' (number, X coordinate for visualization), 'layoutY' (number, Y coordinate for visualization), 'description' (string).", serialization_alias="additionalInfo")
    rule_chain_id: Optional[RuleChainId] = Field(default=None, description="JSON object with the Rule Chain Id. ", serialization_alias="ruleChainId")
    type: Optional[StrictStr] = Field(default=None, description="Full Java Class Name of the rule node implementation. ")
    name: Optional[StrictStr] = Field(default=None, description="User defined name of the rule node. Used on UI and for logging. ")
    debug_settings: Optional[DebugSettings] = Field(default=None, description="Debug settings object.", serialization_alias="debugSettings")
    singleton_mode: Optional[StrictBool] = Field(default=None, description="Enable/disable singleton mode. ", serialization_alias="singletonMode")
    queue_name: Optional[StrictStr] = Field(default=None, description="Queue name. ", serialization_alias="queueName")
    configuration_version: Optional[StrictInt] = Field(default=None, description="Version of rule node configuration. ", serialization_alias="configurationVersion")
    configuration: Optional[Any] = Field(default=None, description="JSON with the rule node configuration. Structure depends on the rule node implementation.")
    external_id: Optional[RuleNodeId] = Field(default=None, serialization_alias="externalId")
    debug_mode: Optional[StrictBool] = Field(default=None, serialization_alias="debugMode")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "additionalInfo", "ruleChainId", "type", "name", "debugSettings", "singletonMode", "queueName", "configurationVersion", "configuration", "externalId", "debugMode"]

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
        """Create an instance of RuleNode from a JSON string"""
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
            "rule_chain_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rule_chain_id
        if self.rule_chain_id:
            _dict['ruleChainId'] = self.rule_chain_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of debug_settings
        if self.debug_settings:
            _dict['debugSettings'] = self.debug_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_id
        if self.external_id:
            _dict['externalId'] = self.external_id.to_dict()
        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        # set to None if configuration (nullable) is None
        # and model_fields_set contains the field
        if self.configuration is None and "configuration" in self.model_fields_set:
            _dict['configuration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RuleNode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": RuleNodeId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "additional_info": obj.get("additionalInfo"),
            "rule_chain_id": RuleChainId.from_dict(obj["ruleChainId"]) if obj.get("ruleChainId") is not None else None,
            "type": obj.get("type"),
            "name": obj.get("name"),
            "debug_settings": DebugSettings.from_dict(obj["debugSettings"]) if obj.get("debugSettings") is not None else None,
            "singleton_mode": obj.get("singletonMode"),
            "queue_name": obj.get("queueName"),
            "configuration_version": obj.get("configurationVersion"),
            "configuration": obj.get("configuration"),
            "external_id": RuleNodeId.from_dict(obj["externalId"]) if obj.get("externalId") is not None else None,
            "debug_mode": obj.get("debugMode")
        })
        return _obj


