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

from pydantic import ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.doughnut_layout import DoughnutLayout
from tb_pe_client.models.font import Font
from tb_pe_client.models.legend_position import LegendPosition
from tb_pe_client.models.report_latest_chart_settings import ReportLatestChartSettings
from tb_pe_client.models.text_alignment import TextAlignment
from typing import Optional, Set
from typing_extensions import Self

class ReportDoughnutChartSettings(ReportLatestChartSettings):
    """
    ReportDoughnutChartSettings
    """ # noqa: E501
    layout: Optional[DoughnutLayout] = None
    clockwise: Optional[StrictBool] = None
    total_value_font: Optional[Font] = Field(default=None, serialization_alias="totalValueFont")
    total_value_color: Optional[StrictStr] = Field(default=None, serialization_alias="totalValueColor")
    __properties: ClassVar[List[str]] = ["showTitle", "title", "titleFont", "titleColor", "titleAlignment", "units", "decimals", "autoScale", "sortSeries", "showTotal", "showLegend", "legendPosition", "legendLabelFont", "legendLabelColor", "legendValueFont", "legendValueColor", "legendShowTotal", "layout", "clockwise", "totalValueFont", "totalValueColor"]

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
        """Create an instance of ReportDoughnutChartSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of total_value_font
        if self.total_value_font:
            _dict['totalValueFont'] = self.total_value_font.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportDoughnutChartSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "show_title": obj.get("showTitle"),
            "title": obj.get("title"),
            "title_font": Font.from_dict(obj["titleFont"]) if obj.get("titleFont") is not None else None,
            "title_color": obj.get("titleColor"),
            "title_alignment": obj.get("titleAlignment"),
            "units": obj.get("units"),
            "decimals": obj.get("decimals"),
            "auto_scale": obj.get("autoScale"),
            "sort_series": obj.get("sortSeries"),
            "show_total": obj.get("showTotal"),
            "show_legend": obj.get("showLegend"),
            "legend_position": obj.get("legendPosition"),
            "legend_label_font": Font.from_dict(obj["legendLabelFont"]) if obj.get("legendLabelFont") is not None else None,
            "legend_label_color": obj.get("legendLabelColor"),
            "legend_value_font": Font.from_dict(obj["legendValueFont"]) if obj.get("legendValueFont") is not None else None,
            "legend_value_color": obj.get("legendValueColor"),
            "legend_show_total": obj.get("legendShowTotal"),
            "layout": obj.get("layout"),
            "clockwise": obj.get("clockwise"),
            "total_value_font": Font.from_dict(obj["totalValueFont"]) if obj.get("totalValueFont") is not None else None,
            "total_value_color": obj.get("totalValueColor")
        })
        return _obj


