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
from tb_paas_client.models.chart_line_type import ChartLineType
from tb_paas_client.models.chart_shape import ChartShape
from tb_paas_client.models.font import Font
from tb_paas_client.models.threshold_label_position import ThresholdLabelPosition
from tb_paas_client.models.value_source_type import ValueSourceType
from typing import Optional, Set
from typing_extensions import Self

class TimeSeriesChartThreshold(BaseModel):
    """
    TimeSeriesChartThreshold
    """ # noqa: E501
    type: Optional[ValueSourceType] = None
    value: Optional[Union[StrictFloat, StrictInt]] = None
    latest_key_type: Optional[StrictStr] = Field(default=None, alias="latestKeyType")
    latest_key: Optional[StrictStr] = Field(default=None, alias="latestKey")
    entity_key_type: Optional[StrictStr] = Field(default=None, alias="entityKeyType")
    entity_alias: Optional[StrictStr] = Field(default=None, alias="entityAlias")
    entity_key: Optional[StrictStr] = Field(default=None, alias="entityKey")
    y_axis_id: Optional[StrictStr] = Field(default=None, alias="yAxisId")
    units: Optional[StrictStr] = None
    decimals: Optional[StrictInt] = None
    line_color: Optional[StrictStr] = Field(default=None, alias="lineColor")
    line_type: Optional[ChartLineType] = Field(default=None, alias="lineType")
    line_width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="lineWidth")
    start_symbol: Optional[ChartShape] = Field(default=None, alias="startSymbol")
    start_symbol_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="startSymbolSize")
    end_symbol: Optional[ChartShape] = Field(default=None, alias="endSymbol")
    end_symbol_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="endSymbolSize")
    show_label: Optional[StrictBool] = Field(default=None, alias="showLabel")
    label_position: Optional[ThresholdLabelPosition] = Field(default=None, alias="labelPosition")
    label_font: Optional[Font] = Field(default=None, alias="labelFont")
    label_color: Optional[StrictStr] = Field(default=None, alias="labelColor")
    enable_label_background: Optional[StrictBool] = Field(default=None, alias="enableLabelBackground")
    label_background: Optional[StrictStr] = Field(default=None, alias="labelBackground")
    yaxis_id: Optional[StrictStr] = Field(default=None, alias="yaxisId")
    __properties: ClassVar[List[str]] = ["type", "value", "latestKeyType", "latestKey", "entityKeyType", "entityAlias", "entityKey", "yAxisId", "units", "decimals", "lineColor", "lineType", "lineWidth", "startSymbol", "startSymbolSize", "endSymbol", "endSymbolSize", "showLabel", "labelPosition", "labelFont", "labelColor", "enableLabelBackground", "labelBackground", "yaxisId"]

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
            "latestKeyType": obj.get("latestKeyType"),
            "latestKey": obj.get("latestKey"),
            "entityKeyType": obj.get("entityKeyType"),
            "entityAlias": obj.get("entityAlias"),
            "entityKey": obj.get("entityKey"),
            "yAxisId": obj.get("yAxisId"),
            "units": obj.get("units"),
            "decimals": obj.get("decimals"),
            "lineColor": obj.get("lineColor"),
            "lineType": obj.get("lineType"),
            "lineWidth": obj.get("lineWidth"),
            "startSymbol": obj.get("startSymbol"),
            "startSymbolSize": obj.get("startSymbolSize"),
            "endSymbol": obj.get("endSymbol"),
            "endSymbolSize": obj.get("endSymbolSize"),
            "showLabel": obj.get("showLabel"),
            "labelPosition": obj.get("labelPosition"),
            "labelFont": Font.from_dict(obj["labelFont"]) if obj.get("labelFont") is not None else None,
            "labelColor": obj.get("labelColor"),
            "enableLabelBackground": obj.get("enableLabelBackground"),
            "labelBackground": obj.get("labelBackground"),
            "yaxisId": obj.get("yaxisId")
        })
        return _obj


