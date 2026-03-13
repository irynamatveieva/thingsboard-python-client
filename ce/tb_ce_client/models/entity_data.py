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
from tb_ce_client.models.comparison_ts_value import ComparisonTsValue
from tb_ce_client.models.entity_id import EntityId
from tb_ce_client.models.ts_value import TsValue
from typing import Optional, Set
from typing_extensions import Self

class EntityData(BaseModel):
    """
    EntityData
    """ # noqa: E501
    entity_id: Optional[EntityId] = Field(default=None, alias="entityId")
    latest: Optional[Dict[str, Dict[str, TsValue]]] = None
    timeseries: Optional[Dict[str, List[TsValue]]] = None
    agg_latest: Optional[Dict[str, ComparisonTsValue]] = Field(default=None, alias="aggLatest")
    __properties: ClassVar[List[str]] = ["entityId", "latest", "timeseries", "aggLatest"]

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
        """Create an instance of EntityData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of entity_id
        if self.entity_id:
            _dict['entityId'] = self.entity_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in latest (dict)
        _field_dict = {}
        if self.latest:
            for _key_latest in self.latest:
                if self.latest[_key_latest]:
                    _field_dict[_key_latest] = self.latest[_key_latest].to_dict()
            _dict['latest'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in timeseries (dict of array)
        _field_dict_of_array = {}
        if self.timeseries:
            for _key_timeseries in self.timeseries:
                if self.timeseries[_key_timeseries] is not None:
                    _field_dict_of_array[_key_timeseries] = [
                        _item.to_dict() for _item in self.timeseries[_key_timeseries]
                    ]
            _dict['timeseries'] = _field_dict_of_array
        # override the default output from pydantic by calling `to_dict()` of each value in agg_latest (dict)
        _field_dict = {}
        if self.agg_latest:
            for _key_agg_latest in self.agg_latest:
                if self.agg_latest[_key_agg_latest]:
                    _field_dict[_key_agg_latest] = self.agg_latest[_key_agg_latest].to_dict()
            _dict['aggLatest'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EntityData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entityId": EntityId.from_dict(obj["entityId"]) if obj.get("entityId") is not None else None,
            "latest": dict(
                (_k, dict(
                    (_ik, TsValue.from_dict(_iv))
                        for _ik, _iv in _v.items()
                    )
                    if _v is not None
                    else None
                )
                for _k, _v in obj.get("latest").items()
            )
            if obj.get("latest") is not None
            else None,
            "timeseries": dict(
                (_k,
                        [TsValue.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("timeseries", {}).items()
            ),
            "aggLatest": dict(
                (_k, ComparisonTsValue.from_dict(_v))
                for _k, _v in obj["aggLatest"].items()
            )
            if obj.get("aggLatest") is not None
            else None
        })
        return _obj


