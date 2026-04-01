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
    start_ts: Optional[StrictInt] = Field(default=None, serialization_alias="startTs")
    end_ts: Optional[StrictInt] = Field(default=None, serialization_alias="endTs")
    agg_parameters: Optional[AggregationParams] = Field(default=None, serialization_alias="aggParameters")
    limit: Optional[StrictInt] = None
    order: Optional[StrictStr] = None
    aggregation: Optional[Aggregation] = None
    interval: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "key", "startTs", "endTs", "aggParameters", "limit", "order", "aggregation", "interval"]

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
            "start_ts": obj.get("startTs"),
            "end_ts": obj.get("endTs"),
            "agg_parameters": AggregationParams.from_dict(obj["aggParameters"]) if obj.get("aggParameters") is not None else None,
            "limit": obj.get("limit"),
            "order": obj.get("order"),
            "aggregation": obj.get("aggregation"),
            "interval": obj.get("interval")
        })
        return _obj


