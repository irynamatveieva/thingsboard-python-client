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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.fixed_time_window import FixedTimeWindow
from tb_pe_client.models.interval import Interval
from tb_pe_client.models.quick_time_interval import QuickTimeInterval
from typing import Optional, Set
from typing_extensions import Self

class History(BaseModel):
    """
    History
    """ # noqa: E501
    history_type: Optional[StrictInt] = Field(default=None, alias="historyType")
    interval: Optional[Interval] = None
    timewindow_ms: Optional[StrictInt] = Field(default=None, alias="timewindowMs")
    fixed_timewindow: Optional[FixedTimeWindow] = Field(default=None, alias="fixedTimewindow")
    quick_interval: Optional[QuickTimeInterval] = Field(default=None, alias="quickInterval")
    __properties: ClassVar[List[str]] = ["historyType", "interval", "timewindowMs", "fixedTimewindow", "quickInterval"]

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
        """Create an instance of History from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of interval
        if self.interval:
            _dict['interval'] = self.interval.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fixed_timewindow
        if self.fixed_timewindow:
            _dict['fixedTimewindow'] = self.fixed_timewindow.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of History from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "historyType": obj.get("historyType"),
            "interval": Interval.from_dict(obj["interval"]) if obj.get("interval") is not None else None,
            "timewindowMs": obj.get("timewindowMs"),
            "fixedTimewindow": FixedTimeWindow.from_dict(obj["fixedTimewindow"]) if obj.get("fixedTimewindow") is not None else None,
            "quickInterval": obj.get("quickInterval")
        })
        return _obj


