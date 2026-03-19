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
from tb_pe_client.models.font import Font
from tb_pe_client.models.legend_position import LegendPosition
from tb_pe_client.models.text_alignment import TextAlignment
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_pe_client.models.report_doughnut_chart_settings import ReportDoughnutChartSettings
    from tb_pe_client.models.report_doughnut_chart_settings import ReportDoughnutChartSettings
    from tb_pe_client.models.report_bar_chart_settings import ReportBarChartSettings
    from tb_pe_client.models.report_pie_chart_settings import ReportPieChartSettings

class ReportLatestChartSettings(BaseModel):
    """
    ReportLatestChartSettings
    """ # noqa: E501
    show_title: Optional[StrictBool] = Field(default=None, alias="showTitle")
    title: Optional[StrictStr] = None
    title_font: Optional[Font] = Field(default=None, alias="titleFont")
    title_color: Optional[StrictStr] = Field(default=None, alias="titleColor")
    title_alignment: Optional[TextAlignment] = Field(default=None, alias="titleAlignment")
    units: Optional[StrictStr] = None
    decimals: Optional[StrictInt] = None
    auto_scale: Optional[StrictBool] = Field(default=None, alias="autoScale")
    sort_series: Optional[StrictBool] = Field(default=None, alias="sortSeries")
    show_total: Optional[StrictBool] = Field(default=None, alias="showTotal")
    show_legend: Optional[StrictBool] = Field(default=None, alias="showLegend")
    legend_position: Optional[LegendPosition] = Field(default=None, alias="legendPosition")
    legend_label_font: Optional[Font] = Field(default=None, alias="legendLabelFont")
    legend_label_color: Optional[StrictStr] = Field(default=None, alias="legendLabelColor")
    legend_value_font: Optional[Font] = Field(default=None, alias="legendValueFont")
    legend_value_color: Optional[StrictStr] = Field(default=None, alias="legendValueColor")
    legend_show_total: Optional[StrictBool] = Field(default=None, alias="legendShowTotal")
    __properties: ClassVar[List[str]] = ["showTitle", "title", "titleFont", "titleColor", "titleAlignment", "units", "decimals", "autoScale", "sortSeries", "showTotal", "showLegend", "legendPosition", "legendLabelFont", "legendLabelColor", "legendValueFont", "legendValueColor", "legendShowTotal"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'subType'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'doughnutChart': 'ReportDoughnutChartSettings','horizontalDoughnutChart': 'ReportDoughnutChartSettings','latestBarChart': 'ReportBarChartSettings','pieChart': 'ReportPieChartSettings'
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
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[ReportDoughnutChartSettings, ReportDoughnutChartSettings, ReportBarChartSettings, ReportPieChartSettings]]:
        """Create an instance of ReportLatestChartSettings from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[ReportDoughnutChartSettings, ReportDoughnutChartSettings, ReportBarChartSettings, ReportPieChartSettings]]:
        """Create an instance of ReportLatestChartSettings from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'ReportDoughnutChartSettings':
            return import_module("tb_pe_client.models.report_doughnut_chart_settings").ReportDoughnutChartSettings.from_dict(obj)
        if object_type ==  'ReportDoughnutChartSettings':
            return import_module("tb_pe_client.models.report_doughnut_chart_settings").ReportDoughnutChartSettings.from_dict(obj)
        if object_type ==  'ReportBarChartSettings':
            return import_module("tb_pe_client.models.report_bar_chart_settings").ReportBarChartSettings.from_dict(obj)
        if object_type ==  'ReportPieChartSettings':
            return import_module("tb_pe_client.models.report_pie_chart_settings").ReportPieChartSettings.from_dict(obj)

        raise ValueError("ReportLatestChartSettings failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


