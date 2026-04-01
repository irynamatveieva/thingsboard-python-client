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

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_pe_client.models.comparison_duration import ComparisonDuration
from tb_pe_client.models.font import Font
from tb_pe_client.models.legend_config import LegendConfig
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

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_pe_client.models.report_bar_chart_with_labels_settings import ReportBarChartWithLabelsSettings
    from tb_pe_client.models.report_range_chart_settings import ReportRangeChartSettings

class ReportTimeSeriesChartSettings(BaseModel):
    """
    ReportTimeSeriesChartSettings
    """ # noqa: E501
    show_title: Optional[StrictBool] = Field(default=None, serialization_alias="showTitle")
    title: Optional[StrictStr] = None
    title_font: Optional[Font] = Field(default=None, serialization_alias="titleFont")
    title_color: Optional[StrictStr] = Field(default=None, serialization_alias="titleColor")
    title_alignment: Optional[TextAlignment] = Field(default=None, serialization_alias="titleAlignment")
    thresholds: Optional[List[TimeSeriesChartThreshold]] = None
    stack: Optional[StrictBool] = None
    grid: Optional[TimeSeriesChartGridSettings] = None
    y_axes: Optional[Dict[str, TimeSeriesChartYAxisSettings]] = Field(default=None, serialization_alias="yAxes")
    x_axis: Optional[TimeSeriesChartXAxisSettings] = Field(default=None, serialization_alias="xAxis")
    bar_width_settings: Optional[TimeSeriesChartBarWidthSettings] = Field(default=None, serialization_alias="barWidthSettings")
    no_aggregation_bar_width_settings: Optional[TimeSeriesChartNoAggregationBarWidthSettings] = Field(default=None, serialization_alias="noAggregationBarWidthSettings")
    states: Optional[List[TimeSeriesChartStateSettings]] = None
    comparison_enabled: Optional[StrictBool] = Field(default=None, serialization_alias="comparisonEnabled")
    time_for_comparison: Optional[ComparisonDuration] = Field(default=None, serialization_alias="timeForComparison")
    comparison_custom_interval_value: Optional[StrictInt] = Field(default=None, serialization_alias="comparisonCustomIntervalValue")
    comparison_x_axis: Optional[TimeSeriesChartXAxisSettings] = Field(default=None, serialization_alias="comparisonXAxis")
    show_legend: Optional[StrictBool] = Field(default=None, serialization_alias="showLegend")
    legend_column_title_font: Optional[Font] = Field(default=None, serialization_alias="legendColumnTitleFont")
    legend_column_title_color: Optional[StrictStr] = Field(default=None, serialization_alias="legendColumnTitleColor")
    legend_label_font: Optional[Font] = Field(default=None, serialization_alias="legendLabelFont")
    legend_label_color: Optional[StrictStr] = Field(default=None, serialization_alias="legendLabelColor")
    legend_value_font: Optional[Font] = Field(default=None, serialization_alias="legendValueFont")
    legend_value_color: Optional[StrictStr] = Field(default=None, serialization_alias="legendValueColor")
    legend_config: Optional[LegendConfig] = Field(default=None, serialization_alias="legendConfig")
    xaxis: Optional[TimeSeriesChartXAxisSettings] = None
    yaxes: Optional[Dict[str, TimeSeriesChartYAxisSettings]] = None
    __properties: ClassVar[List[str]] = ["showTitle", "title", "titleFont", "titleColor", "titleAlignment", "thresholds", "stack", "grid", "yAxes", "xAxis", "barWidthSettings", "noAggregationBarWidthSettings", "states", "comparisonEnabled", "timeForComparison", "comparisonCustomIntervalValue", "comparisonXAxis", "showLegend", "legendColumnTitleFont", "legendColumnTitleColor", "legendLabelFont", "legendLabelColor", "legendValueFont", "legendValueColor", "legendConfig", "xaxis", "yaxes"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'subType'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'barChartWithLabels': 'ReportBarChartWithLabelsSettings','rangeChart': 'ReportRangeChartSettings'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

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
    def from_json(cls, json_str: str) -> Optional[Union[ReportBarChartWithLabelsSettings, ReportRangeChartSettings]]:
        """Create an instance of ReportTimeSeriesChartSettings from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[ReportBarChartWithLabelsSettings, ReportRangeChartSettings]]:
        """Create an instance of ReportTimeSeriesChartSettings from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'ReportBarChartWithLabelsSettings':
            return import_module("tb_pe_client.models.report_bar_chart_with_labels_settings").ReportBarChartWithLabelsSettings.from_dict(obj)
        if object_type ==  'ReportRangeChartSettings':
            return import_module("tb_pe_client.models.report_range_chart_settings").ReportRangeChartSettings.from_dict(obj)

        raise ValueError("ReportTimeSeriesChartSettings failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


