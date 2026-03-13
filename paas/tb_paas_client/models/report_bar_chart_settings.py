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

from pydantic import ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_paas_client.models.bar_series_settings import BarSeriesSettings
from tb_paas_client.models.font import Font
from tb_paas_client.models.legend_position import LegendPosition
from tb_paas_client.models.report_latest_chart_settings import ReportLatestChartSettings
from tb_paas_client.models.text_alignment import TextAlignment
from typing import Optional, Set
from typing_extensions import Self

class ReportBarChartSettings(ReportLatestChartSettings):
    """
    ReportBarChartSettings
    """ # noqa: E501
    axis_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="axisMin")
    axis_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="axisMax")
    axis_tick_label_font: Optional[Font] = Field(default=None, alias="axisTickLabelFont")
    axis_tick_label_color: Optional[StrictStr] = Field(default=None, alias="axisTickLabelColor")
    bar_settings: Optional[BarSeriesSettings] = Field(default=None, alias="barSettings")
    __properties: ClassVar[List[str]] = ["showTitle", "title", "titleFont", "titleColor", "titleAlignment", "units", "decimals", "autoScale", "sortSeries", "showTotal", "showLegend", "legendPosition", "legendLabelFont", "legendLabelColor", "legendValueFont", "legendValueColor", "legendShowTotal", "axisMin", "axisMax", "axisTickLabelFont", "axisTickLabelColor", "barSettings"]

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
        """Create an instance of ReportBarChartSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of title_font
        if self.title_font:
            _dict['titleFont'] = self.title_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legend_label_font
        if self.legend_label_font:
            _dict['legendLabelFont'] = self.legend_label_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legend_value_font
        if self.legend_value_font:
            _dict['legendValueFont'] = self.legend_value_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of axis_tick_label_font
        if self.axis_tick_label_font:
            _dict['axisTickLabelFont'] = self.axis_tick_label_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bar_settings
        if self.bar_settings:
            _dict['barSettings'] = self.bar_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportBarChartSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "showTitle": obj.get("showTitle"),
            "title": obj.get("title"),
            "titleFont": Font.from_dict(obj["titleFont"]) if obj.get("titleFont") is not None else None,
            "titleColor": obj.get("titleColor"),
            "titleAlignment": obj.get("titleAlignment"),
            "units": obj.get("units"),
            "decimals": obj.get("decimals"),
            "autoScale": obj.get("autoScale"),
            "sortSeries": obj.get("sortSeries"),
            "showTotal": obj.get("showTotal"),
            "showLegend": obj.get("showLegend"),
            "legendPosition": obj.get("legendPosition"),
            "legendLabelFont": Font.from_dict(obj["legendLabelFont"]) if obj.get("legendLabelFont") is not None else None,
            "legendLabelColor": obj.get("legendLabelColor"),
            "legendValueFont": Font.from_dict(obj["legendValueFont"]) if obj.get("legendValueFont") is not None else None,
            "legendValueColor": obj.get("legendValueColor"),
            "legendShowTotal": obj.get("legendShowTotal"),
            "axisMin": obj.get("axisMin"),
            "axisMax": obj.get("axisMax"),
            "axisTickLabelFont": Font.from_dict(obj["axisTickLabelFont"]) if obj.get("axisTickLabelFont") is not None else None,
            "axisTickLabelColor": obj.get("axisTickLabelColor"),
            "barSettings": BarSeriesSettings.from_dict(obj["barSettings"]) if obj.get("barSettings") is not None else None
        })
        return _obj


