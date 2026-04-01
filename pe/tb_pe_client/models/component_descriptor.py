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
from tb_pe_client.models.component_clustering_mode import ComponentClusteringMode
from tb_pe_client.models.component_descriptor_id import ComponentDescriptorId
from tb_pe_client.models.component_scope import ComponentScope
from tb_pe_client.models.component_type import ComponentType
from typing import Optional, Set
from typing_extensions import Self

class ComponentDescriptor(BaseModel):
    """
    ComponentDescriptor
    """ # noqa: E501
    id: Optional[ComponentDescriptorId] = Field(default=None, description="JSON object with the descriptor Id. Specify existing descriptor id to update the descriptor. Referencing non-existing descriptor Id will cause error. Omit this field to create new descriptor.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the descriptor creation, in milliseconds", serialization_alias="createdTime")
    type: Optional[ComponentType] = Field(default=None, description="Type of the Rule Node")
    scope: Optional[ComponentScope] = Field(default=None, description="Scope of the Rule Node. Always set to 'TENANT', since no rule chains on the 'SYSTEM' level yet.")
    clustering_mode: Optional[ComponentClusteringMode] = Field(default=None, description="Clustering mode of the RuleNode. This mode represents the ability to start Rule Node in multiple microservices.", serialization_alias="clusteringMode")
    name: Optional[StrictStr] = Field(default=None, description="Name of the Rule Node. Taken from the @RuleNode annotation.")
    clazz: Optional[StrictStr] = Field(default=None, description="Full name of the Java class that implements the Rule Engine Node interface.")
    configuration_descriptor: Optional[Any] = Field(default=None, serialization_alias="configurationDescriptor")
    configuration_version: Optional[StrictInt] = Field(default=None, description="Rule node configuration version. By default, this value is 0. If the rule node is a versioned node, this value might be greater than 0.", serialization_alias="configurationVersion")
    actions: Optional[StrictStr] = Field(default=None, description="Rule Node Actions. Deprecated. Always null.")
    has_queue_name: Optional[StrictBool] = Field(default=None, description="Indicates that the RuleNode supports queue name configuration.", serialization_alias="hasQueueName")
    has_secrets: Optional[StrictBool] = Field(default=None, description="Indicates that the RuleNode configuration uses secrets placeholders.", serialization_alias="hasSecrets")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "type", "scope", "clusteringMode", "name", "clazz", "configurationDescriptor", "configurationVersion", "actions", "hasQueueName", "hasSecrets"]

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
        """Create an instance of ComponentDescriptor from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "type",
            "scope",
            "clustering_mode",
            "name",
            "clazz",
            "configuration_version",
            "actions",
            "has_queue_name",
            "has_secrets",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # set to None if configuration_descriptor (nullable) is None
        # and model_fields_set contains the field
        if self.configuration_descriptor is None and "configuration_descriptor" in self.model_fields_set:
            _dict['configurationDescriptor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ComponentDescriptor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": ComponentDescriptorId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "type": obj.get("type"),
            "scope": obj.get("scope"),
            "clustering_mode": obj.get("clusteringMode"),
            "name": obj.get("name"),
            "clazz": obj.get("clazz"),
            "configuration_descriptor": obj.get("configurationDescriptor"),
            "configuration_version": obj.get("configurationVersion"),
            "actions": obj.get("actions"),
            "has_queue_name": obj.get("hasQueueName"),
            "has_secrets": obj.get("hasSecrets")
        })
        return _obj


