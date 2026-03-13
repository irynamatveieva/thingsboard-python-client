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
from tb_ce_client.models.entity_key import EntityKey
from tb_ce_client.models.entity_key_value_type import EntityKeyValueType
from tb_ce_client.models.key_filter_predicate import KeyFilterPredicate
from typing import Optional, Set
from typing_extensions import Self

class KeyFilter(BaseModel):
    """
    KeyFilter
    """ # noqa: E501
    key: Optional[EntityKey] = None
    value_type: Optional[EntityKeyValueType] = Field(default=None, alias="valueType")
    predicate: Optional[KeyFilterPredicate] = None
    __properties: ClassVar[List[str]] = ["key", "valueType", "predicate"]

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
        """Create an instance of KeyFilter from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of key
        if self.key:
            _dict['key'] = self.key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of predicate
        if self.predicate:
            _dict['predicate'] = self.predicate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeyFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "key": EntityKey.from_dict(obj["key"]) if obj.get("key") is not None else None,
            "valueType": obj.get("valueType"),
            "predicate": KeyFilterPredicate.from_dict(obj["predicate"]) if obj.get("predicate") is not None else None
        })
        return _obj


