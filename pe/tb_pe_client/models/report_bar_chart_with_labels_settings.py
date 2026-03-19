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

from pydantic import ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_pe_client.models.chart_fill_settings import ChartFillSettings
from tb_pe_client.models.comparison_duration import ComparisonDuration
from tb_pe_client.models.font import Font
from tb_pe_client.models.legend_config import LegendConfig
from tb_pe_client.models.report_time_series_chart_settings import ReportTimeSeriesChartSettings
from tb_pe_client.models.text_alignment import TextAlignment
from tb_pe_client.models.time_series_chart_bar_width_settings import TimeSeriesChartBarWidthSettings
from tb_pe_client.models.time_series_chart_grid_settings import TimeSeriesChartGridSettings
from tb_pe_client.models.time_series_chart_no_aggregation_bar_width_settings import TimeSeriesChartNoAggregationBarWidthSettings
from tb_pe_client.models.time_series_chart_state_settings import TimeSeriesChartStateSettings
from tb_pe_client.models.time_series_chart_threshold import TimeSeriesChartThreshold
from tb_pe_client.models.time_series_chart_x_axis_settings import TimeSeriesChartXAxisSettings
from tb_pe_client.models.time_series_chart_y_axis_settings import TimeSeriesChartYAxisSettings
from typing import Optional, Set
from typing_extensions import Self

class ReportBarChartWithLabelsSettings(ReportTimeSeriesChartSettings):
    """
    ReportBarChartWithLabelsSettings
    """ # noqa: E501
    show_bar_label: Optional[StrictBool] = Field(default=None, alias="showBarLabel")
    bar_label_font: Optional[Font] = Field(default=None, alias="barLabelFont")
    bar_label_color: Optional[StrictStr] = Field(default=None, alias="barLabelColor")
    show_bar_value: Optional[StrictBool] = Field(default=None, alias="showBarValue")
    bar_value_font: Optional[Font] = Field(default=None, alias="barValueFont")
    bar_value_color: Optional[StrictStr] = Field(default=None, alias="barValueColor")
    show_bar_border: Optional[StrictBool] = Field(default=None, alias="showBarBorder")
    bar_border_width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="barBorderWidth")
    bar_border_radius: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="barBorderRadius")
    bar_background_settings: Optional[ChartFillSettings] = Field(default=None, alias="barBackgroundSettings")
    bar_units: Optional[StrictStr] = Field(default=None, alias="barUnits")
    bar_decimals: Optional[StrictInt] = Field(default=None, alias="barDecimals")
    __properties: ClassVar[List[str]] = ["showTitle", "title", "titleFont", "titleColor", "titleAlignment", "thresholds", "stack", "grid", "yAxes", "xAxis", "barWidthSettings", "noAggregationBarWidthSettings", "states", "comparisonEnabled", "timeForComparison", "comparisonCustomIntervalValue", "comparisonXAxis", "showLegend", "legendColumnTitleFont", "legendColumnTitleColor", "legendLabelFont", "legendLabelColor", "legendValueFont", "legendValueColor", "legendConfig", "xaxis", "yaxes", "showBarLabel", "barLabelFont", "barLabelColor", "showBarValue", "barValueFont", "barValueColor", "showBarBorder", "barBorderWidth", "barBorderRadius", "barBackgroundSettings", "barUnits", "barDecimals"]

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
        """Create an instance of ReportBarChartWithLabelsSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in thresholds (list)
        _items = []
        if self.thresholds:
            for _item_thresholds in self.thresholds:
                if _item_thresholds:
                    _items.append(_item_thresholds.to_dict())
            _dict['thresholds'] = _items
        # override the default output from pydantic by calling `to_dict()` of grid
        if self.grid:
            _dict['grid'] = self.grid.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in y_axes (dict)
        _field_dict = {}
        if self.y_axes:
            for _key_y_axes in self.y_axes:
                if self.y_axes[_key_y_axes]:
                    _field_dict[_key_y_axes] = self.y_axes[_key_y_axes].to_dict()
            _dict['yAxes'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of x_axis
        if self.x_axis:
            _dict['xAxis'] = self.x_axis.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bar_width_settings
        if self.bar_width_settings:
            _dict['barWidthSettings'] = self.bar_width_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of no_aggregation_bar_width_settings
        if self.no_aggregation_bar_width_settings:
            _dict['noAggregationBarWidthSettings'] = self.no_aggregation_bar_width_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in states (list)
        _items = []
        if self.states:
            for _item_states in self.states:
                if _item_states:
                    _items.append(_item_states.to_dict())
            _dict['states'] = _items
        # override the default output from pydantic by calling `to_dict()` of comparison_x_axis
        if self.comparison_x_axis:
            _dict['comparisonXAxis'] = self.comparison_x_axis.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legend_column_title_font
        if self.legend_column_title_font:
            _dict['legendColumnTitleFont'] = self.legend_column_title_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legend_label_font
        if self.legend_label_font:
            _dict['legendLabelFont'] = self.legend_label_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legend_value_font
        if self.legend_value_font:
            _dict['legendValueFont'] = self.legend_value_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legend_config
        if self.legend_config:
            _dict['legendConfig'] = self.legend_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of xaxis
        if self.xaxis:
            _dict['xaxis'] = self.xaxis.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in yaxes (dict)
        _field_dict = {}
        if self.yaxes:
            for _key_yaxes in self.yaxes:
                if self.yaxes[_key_yaxes]:
                    _field_dict[_key_yaxes] = self.yaxes[_key_yaxes].to_dict()
            _dict['yaxes'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of bar_label_font
        if self.bar_label_font:
            _dict['barLabelFont'] = self.bar_label_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bar_value_font
        if self.bar_value_font:
            _dict['barValueFont'] = self.bar_value_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bar_background_settings
        if self.bar_background_settings:
            _dict['barBackgroundSettings'] = self.bar_background_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportBarChartWithLabelsSettings from a dict"""
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
            "thresholds": [TimeSeriesChartThreshold.from_dict(_item) for _item in obj["thresholds"]] if obj.get("thresholds") is not None else None,
            "stack": obj.get("stack"),
            "grid": TimeSeriesChartGridSettings.from_dict(obj["grid"]) if obj.get("grid") is not None else None,
            "yAxes": dict(
                (_k, TimeSeriesChartYAxisSettings.from_dict(_v))
                for _k, _v in obj["yAxes"].items()
            )
            if obj.get("yAxes") is not None
            else None,
            "xAxis": TimeSeriesChartXAxisSettings.from_dict(obj["xAxis"]) if obj.get("xAxis") is not None else None,
            "barWidthSettings": TimeSeriesChartBarWidthSettings.from_dict(obj["barWidthSettings"]) if obj.get("barWidthSettings") is not None else None,
            "noAggregationBarWidthSettings": TimeSeriesChartNoAggregationBarWidthSettings.from_dict(obj["noAggregationBarWidthSettings"]) if obj.get("noAggregationBarWidthSettings") is not None else None,
            "states": [TimeSeriesChartStateSettings.from_dict(_item) for _item in obj["states"]] if obj.get("states") is not None else None,
            "comparisonEnabled": obj.get("comparisonEnabled"),
            "timeForComparison": obj.get("timeForComparison"),
            "comparisonCustomIntervalValue": obj.get("comparisonCustomIntervalValue"),
            "comparisonXAxis": TimeSeriesChartXAxisSettings.from_dict(obj["comparisonXAxis"]) if obj.get("comparisonXAxis") is not None else None,
            "showLegend": obj.get("showLegend"),
            "legendColumnTitleFont": Font.from_dict(obj["legendColumnTitleFont"]) if obj.get("legendColumnTitleFont") is not None else None,
            "legendColumnTitleColor": obj.get("legendColumnTitleColor"),
            "legendLabelFont": Font.from_dict(obj["legendLabelFont"]) if obj.get("legendLabelFont") is not None else None,
            "legendLabelColor": obj.get("legendLabelColor"),
            "legendValueFont": Font.from_dict(obj["legendValueFont"]) if obj.get("legendValueFont") is not None else None,
            "legendValueColor": obj.get("legendValueColor"),
            "legendConfig": LegendConfig.from_dict(obj["legendConfig"]) if obj.get("legendConfig") is not None else None,
            "xaxis": TimeSeriesChartXAxisSettings.from_dict(obj["xaxis"]) if obj.get("xaxis") is not None else None,
            "yaxes": dict(
                (_k, TimeSeriesChartYAxisSettings.from_dict(_v))
                for _k, _v in obj["yaxes"].items()
            )
            if obj.get("yaxes") is not None
            else None,
            "showBarLabel": obj.get("showBarLabel"),
            "barLabelFont": Font.from_dict(obj["barLabelFont"]) if obj.get("barLabelFont") is not None else None,
            "barLabelColor": obj.get("barLabelColor"),
            "showBarValue": obj.get("showBarValue"),
            "barValueFont": Font.from_dict(obj["barValueFont"]) if obj.get("barValueFont") is not None else None,
            "barValueColor": obj.get("barValueColor"),
            "showBarBorder": obj.get("showBarBorder"),
            "barBorderWidth": obj.get("barBorderWidth"),
            "barBorderRadius": obj.get("barBorderRadius"),
            "barBackgroundSettings": ChartFillSettings.from_dict(obj["barBackgroundSettings"]) if obj.get("barBackgroundSettings") is not None else None,
            "barUnits": obj.get("barUnits"),
            "barDecimals": obj.get("barDecimals")
        })
        return _obj


