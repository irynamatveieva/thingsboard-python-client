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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.axis_position import AxisPosition
from tb_pe_client.models.font import Font
from typing import Optional, Set
from typing_extensions import Self

class TimeSeriesChartXAxisSettings(BaseModel):
    """
    TimeSeriesChartXAxisSettings
    """ # noqa: E501
    show: Optional[StrictBool] = None
    label: Optional[StrictStr] = None
    label_font: Optional[Font] = Field(default=None, alias="labelFont")
    label_color: Optional[StrictStr] = Field(default=None, alias="labelColor")
    position: Optional[AxisPosition] = None
    show_tick_labels: Optional[StrictBool] = Field(default=None, alias="showTickLabels")
    tick_label_font: Optional[Font] = Field(default=None, alias="tickLabelFont")
    tick_label_color: Optional[StrictStr] = Field(default=None, alias="tickLabelColor")
    show_ticks: Optional[StrictBool] = Field(default=None, alias="showTicks")
    ticks_color: Optional[StrictStr] = Field(default=None, alias="ticksColor")
    show_line: Optional[StrictBool] = Field(default=None, alias="showLine")
    line_color: Optional[StrictStr] = Field(default=None, alias="lineColor")
    show_split_lines: Optional[StrictBool] = Field(default=None, alias="showSplitLines")
    split_lines_color: Optional[StrictStr] = Field(default=None, alias="splitLinesColor")
    ticks_format: Optional[Dict[str, StrictStr]] = Field(default=None, alias="ticksFormat")
    __properties: ClassVar[List[str]] = ["show", "label", "labelFont", "labelColor", "position", "showTickLabels", "tickLabelFont", "tickLabelColor", "showTicks", "ticksColor", "showLine", "lineColor", "showSplitLines", "splitLinesColor", "ticksFormat"]

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
        """Create an instance of TimeSeriesChartXAxisSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of label_font
        if self.label_font:
            _dict['labelFont'] = self.label_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tick_label_font
        if self.tick_label_font:
            _dict['tickLabelFont'] = self.tick_label_font.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimeSeriesChartXAxisSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "show": obj.get("show"),
            "label": obj.get("label"),
            "labelFont": Font.from_dict(obj["labelFont"]) if obj.get("labelFont") is not None else None,
            "labelColor": obj.get("labelColor"),
            "position": obj.get("position"),
            "showTickLabels": obj.get("showTickLabels"),
            "tickLabelFont": Font.from_dict(obj["tickLabelFont"]) if obj.get("tickLabelFont") is not None else None,
            "tickLabelColor": obj.get("tickLabelColor"),
            "showTicks": obj.get("showTicks"),
            "ticksColor": obj.get("ticksColor"),
            "showLine": obj.get("showLine"),
            "lineColor": obj.get("lineColor"),
            "showSplitLines": obj.get("showSplitLines"),
            "splitLinesColor": obj.get("splitLinesColor"),
            "ticksFormat": obj.get("ticksFormat")
        })
        return _obj


