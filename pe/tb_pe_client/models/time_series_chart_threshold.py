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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_pe_client.models.chart_line_type import ChartLineType
from tb_pe_client.models.chart_shape import ChartShape
from tb_pe_client.models.font import Font
from tb_pe_client.models.threshold_label_position import ThresholdLabelPosition
from tb_pe_client.models.value_source_type import ValueSourceType
from typing import Optional, Set
from typing_extensions import Self

class TimeSeriesChartThreshold(BaseModel):
    """
    TimeSeriesChartThreshold
    """ # noqa: E501
    type: Optional[ValueSourceType] = None
    value: Optional[Union[StrictFloat, StrictInt]] = None
    latest_key_type: Optional[StrictStr] = Field(default=None, serialization_alias="latestKeyType")
    latest_key: Optional[StrictStr] = Field(default=None, serialization_alias="latestKey")
    entity_key_type: Optional[StrictStr] = Field(default=None, serialization_alias="entityKeyType")
    entity_alias: Optional[StrictStr] = Field(default=None, serialization_alias="entityAlias")
    entity_key: Optional[StrictStr] = Field(default=None, serialization_alias="entityKey")
    y_axis_id: Optional[StrictStr] = Field(default=None, serialization_alias="yAxisId")
    units: Optional[StrictStr] = None
    decimals: Optional[StrictInt] = None
    line_color: Optional[StrictStr] = Field(default=None, serialization_alias="lineColor")
    line_type: Optional[ChartLineType] = Field(default=None, serialization_alias="lineType")
    line_width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, serialization_alias="lineWidth")
    start_symbol: Optional[ChartShape] = Field(default=None, serialization_alias="startSymbol")
    start_symbol_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, serialization_alias="startSymbolSize")
    end_symbol: Optional[ChartShape] = Field(default=None, serialization_alias="endSymbol")
    end_symbol_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, serialization_alias="endSymbolSize")
    show_label: Optional[StrictBool] = Field(default=None, serialization_alias="showLabel")
    label_position: Optional[ThresholdLabelPosition] = Field(default=None, serialization_alias="labelPosition")
    label_font: Optional[Font] = Field(default=None, serialization_alias="labelFont")
    label_color: Optional[StrictStr] = Field(default=None, serialization_alias="labelColor")
    enable_label_background: Optional[StrictBool] = Field(default=None, serialization_alias="enableLabelBackground")
    label_background: Optional[StrictStr] = Field(default=None, serialization_alias="labelBackground")
    yaxis_id: Optional[StrictStr] = Field(default=None, serialization_alias="yaxisId")
    __properties: ClassVar[List[str]] = ["type", "value", "latestKeyType", "latestKey", "entityKeyType", "entityAlias", "entityKey", "yAxisId", "units", "decimals", "lineColor", "lineType", "lineWidth", "startSymbol", "startSymbolSize", "endSymbol", "endSymbolSize", "showLabel", "labelPosition", "labelFont", "labelColor", "enableLabelBackground", "labelBackground", "yaxisId"]

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
        """Create an instance of TimeSeriesChartThreshold from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimeSeriesChartThreshold from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "value": obj.get("value"),
            "latest_key_type": obj.get("latestKeyType"),
            "latest_key": obj.get("latestKey"),
            "entity_key_type": obj.get("entityKeyType"),
            "entity_alias": obj.get("entityAlias"),
            "entity_key": obj.get("entityKey"),
            "y_axis_id": obj.get("yAxisId"),
            "units": obj.get("units"),
            "decimals": obj.get("decimals"),
            "line_color": obj.get("lineColor"),
            "line_type": obj.get("lineType"),
            "line_width": obj.get("lineWidth"),
            "start_symbol": obj.get("startSymbol"),
            "start_symbol_size": obj.get("startSymbolSize"),
            "end_symbol": obj.get("endSymbol"),
            "end_symbol_size": obj.get("endSymbolSize"),
            "show_label": obj.get("showLabel"),
            "label_position": obj.get("labelPosition"),
            "label_font": Font.from_dict(obj["labelFont"]) if obj.get("labelFont") is not None else None,
            "label_color": obj.get("labelColor"),
            "enable_label_background": obj.get("enableLabelBackground"),
            "label_background": obj.get("labelBackground"),
            "yaxis_id": obj.get("yaxisId")
        })
        return _obj


