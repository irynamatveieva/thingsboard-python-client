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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.aggregation import Aggregation
from tb_pe_client.models.aggregation_params import AggregationParams
from typing import Optional, Set
from typing_extensions import Self

class BaseReadTsKvQuery(BaseModel):
    """
    BaseReadTsKvQuery
    """ # noqa: E501
    id: Optional[StrictInt] = None
    key: Optional[StrictStr] = None
    start_ts: Optional[StrictInt] = Field(default=None, alias="startTs")
    end_ts: Optional[StrictInt] = Field(default=None, alias="endTs")
    agg_parameters: Optional[AggregationParams] = Field(default=None, alias="aggParameters")
    limit: Optional[StrictInt] = None
    order: Optional[StrictStr] = None
    interval: Optional[StrictInt] = None
    aggregation: Optional[Aggregation] = None
    __properties: ClassVar[List[str]] = ["id", "key", "startTs", "endTs", "aggParameters", "limit", "order", "interval", "aggregation"]

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
        """Create an instance of BaseReadTsKvQuery from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of agg_parameters
        if self.agg_parameters:
            _dict['aggParameters'] = self.agg_parameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BaseReadTsKvQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "key": obj.get("key"),
            "startTs": obj.get("startTs"),
            "endTs": obj.get("endTs"),
            "aggParameters": AggregationParams.from_dict(obj["aggParameters"]) if obj.get("aggParameters") is not None else None,
            "limit": obj.get("limit"),
            "order": obj.get("order"),
            "interval": obj.get("interval"),
            "aggregation": obj.get("aggregation")
        })
        return _obj


