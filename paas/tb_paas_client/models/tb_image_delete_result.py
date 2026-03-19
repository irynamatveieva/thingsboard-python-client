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
from tb_paas_client.models.has_id_object import HasIdObject
from tb_paas_client.models.white_labeling import WhiteLabeling
from typing import Optional, Set
from typing_extensions import Self

class TbImageDeleteResult(BaseModel):
    """
    TbImageDeleteResult
    """ # noqa: E501
    success: Optional[StrictBool] = None
    white_labeling_list: Optional[List[WhiteLabeling]] = Field(default=None, alias="whiteLabelingList")
    references: Optional[Dict[str, List[HasIdObject]]] = None
    __properties: ClassVar[List[str]] = ["success", "whiteLabelingList", "references"]

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
        """Create an instance of TbImageDeleteResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in white_labeling_list (list)
        _items = []
        if self.white_labeling_list:
            for _item_white_labeling_list in self.white_labeling_list:
                if _item_white_labeling_list:
                    _items.append(_item_white_labeling_list.to_dict())
            _dict['whiteLabelingList'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in references (dict of array)
        _field_dict_of_array = {}
        if self.references:
            for _key_references in self.references:
                if self.references[_key_references] is not None:
                    _field_dict_of_array[_key_references] = [
                        _item.to_dict() for _item in self.references[_key_references]
                    ]
            _dict['references'] = _field_dict_of_array
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TbImageDeleteResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "success": obj.get("success"),
            "whiteLabelingList": [WhiteLabeling.from_dict(_item) for _item in obj["whiteLabelingList"]] if obj.get("whiteLabelingList") is not None else None,
            "references": dict(
                (_k,
                        [HasIdObject.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("references", {}).items()
            )
        })
        return _obj


