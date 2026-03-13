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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_paas_client.models.time_series_chart_state_source_type import TimeSeriesChartStateSourceType
from typing import Optional, Set
from typing_extensions import Self

class TimeSeriesChartStateSettings(BaseModel):
    """
    TimeSeriesChartStateSettings
    """ # noqa: E501
    label: Optional[StrictStr] = None
    value: Optional[Union[StrictFloat, StrictInt]] = None
    source_type: Optional[TimeSeriesChartStateSourceType] = Field(default=None, alias="sourceType")
    source_range_from: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sourceRangeFrom")
    source_range_to: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sourceRangeTo")
    source_value: Optional[Any] = Field(default=None, alias="sourceValue")
    __properties: ClassVar[List[str]] = ["label", "value", "sourceType", "sourceRangeFrom", "sourceRangeTo", "sourceValue"]

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
        """Create an instance of TimeSeriesChartStateSettings from a JSON string"""
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
        # set to None if source_value (nullable) is None
        # and model_fields_set contains the field
        if self.source_value is None and "source_value" in self.model_fields_set:
            _dict['sourceValue'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimeSeriesChartStateSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "label": obj.get("label"),
            "value": obj.get("value"),
            "sourceType": obj.get("sourceType"),
            "sourceRangeFrom": obj.get("sourceRangeFrom"),
            "sourceRangeTo": obj.get("sourceRangeTo"),
            "sourceValue": obj.get("sourceValue")
        })
        return _obj


