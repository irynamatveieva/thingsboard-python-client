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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.relation_type_group import RelationTypeGroup
from typing import Optional, Set
from typing_extensions import Self

class EntityRelationInfo(BaseModel):
    """
    EntityRelationInfo
    """ # noqa: E501
    var_from: EntityId = Field(description="JSON object with [from] Entity Id.", serialization_alias="from")
    to: EntityId = Field(description="JSON object with [to] Entity Id.")
    type: Annotated[str, Field(min_length=1, strict=True)] = Field(description="String value of relation type.")
    type_group: RelationTypeGroup = Field(description="Represents the type group of the relation.", serialization_alias="typeGroup")
    version: Optional[StrictInt] = None
    additional_info: Optional[Any] = Field(default=None, description="Additional parameters of the relation.", serialization_alias="additionalInfo")
    from_name: Optional[StrictStr] = Field(default=None, description="Name of the entity for [from] direction.", serialization_alias="fromName")
    to_name: Optional[StrictStr] = Field(default=None, description="Name of the entity for [to] direction.", serialization_alias="toName")
    __properties: ClassVar[List[str]] = ["from", "to", "type", "typeGroup", "version", "additionalInfo", "fromName", "toName"]

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
        """Create an instance of EntityRelationInfo from a JSON string"""
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
            "from_name",
            "to_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of var_from
        if self.var_from:
            _dict['from'] = self.var_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to
        if self.to:
            _dict['to'] = self.to.to_dict()
        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EntityRelationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "from": EntityId.from_dict(obj["from"]) if obj.get("from") is not None else None,
            "to": EntityId.from_dict(obj["to"]) if obj.get("to") is not None else None,
            "type": obj.get("type"),
            "type_group": obj.get("typeGroup"),
            "version": obj.get("version"),
            "additional_info": obj.get("additionalInfo"),
            "from_name": obj.get("fromName"),
            "to_name": obj.get("toName")
        })
        return _obj


