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
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Union
from tb_pe_client.models.report_component_sub_type import ReportComponentSubType
from tb_pe_client.models.report_component_type import ReportComponentType
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_pe_client.models.alarm_table_component import AlarmTableComponent
    from tb_pe_client.models.dashboard_component import DashboardComponent
    from tb_pe_client.models.divider_component import DividerComponent
    from tb_pe_client.models.entity_table_component import EntityTableComponent
    from tb_pe_client.models.error_component import ErrorComponent
    from tb_pe_client.models.heading_component import HeadingComponent
    from tb_pe_client.models.image_component import ImageComponent
    from tb_pe_client.models.latest_chart_component import LatestChartComponent
    from tb_pe_client.models.page_break_component import PageBreakComponent
    from tb_pe_client.models.rich_text_component import RichTextComponent
    from tb_pe_client.models.split_view_component import SplitViewComponent
    from tb_pe_client.models.sub_report_component import SubReportComponent
    from tb_pe_client.models.timeseries_chart_component import TimeseriesChartComponent
    from tb_pe_client.models.timeseries_table_component import TimeseriesTableComponent

class ReportComponent(BaseModel):
    """
    ReportComponent
    """ # noqa: E501
    sub_type: ReportComponentSubType = Field(serialization_alias="subType")
    type: ReportComponentType
    __properties: ClassVar[List[str]] = ["subType", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ALARM_TABLE': 'AlarmTableComponent','DASHBOARD': 'DashboardComponent','DIVIDER': 'DividerComponent','ENTITY_TABLE': 'EntityTableComponent','ERROR': 'ErrorComponent','HEADING': 'HeadingComponent','IMAGE': 'ImageComponent','LATEST_CHART': 'LatestChartComponent','PAGE_BREAK': 'PageBreakComponent','RICH_TEXT': 'RichTextComponent','SPLIT_VIEW': 'SplitViewComponent','SUB_REPORT': 'SubReportComponent','TIME_SERIES_CHART': 'TimeseriesChartComponent','TIME_SERIES_TABLE': 'TimeseriesTableComponent'
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
    def from_json(cls, json_str: str) -> Optional[Union[AlarmTableComponent, DashboardComponent, DividerComponent, EntityTableComponent, ErrorComponent, HeadingComponent, ImageComponent, LatestChartComponent, PageBreakComponent, RichTextComponent, SplitViewComponent, SubReportComponent, TimeseriesChartComponent, TimeseriesTableComponent]]:
        """Create an instance of ReportComponent from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[AlarmTableComponent, DashboardComponent, DividerComponent, EntityTableComponent, ErrorComponent, HeadingComponent, ImageComponent, LatestChartComponent, PageBreakComponent, RichTextComponent, SplitViewComponent, SubReportComponent, TimeseriesChartComponent, TimeseriesTableComponent]]:
        """Create an instance of ReportComponent from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'AlarmTableComponent':
            return import_module("tb_pe_client.models.alarm_table_component").AlarmTableComponent.from_dict(obj)
        if object_type ==  'DashboardComponent':
            return import_module("tb_pe_client.models.dashboard_component").DashboardComponent.from_dict(obj)
        if object_type ==  'DividerComponent':
            return import_module("tb_pe_client.models.divider_component").DividerComponent.from_dict(obj)
        if object_type ==  'EntityTableComponent':
            return import_module("tb_pe_client.models.entity_table_component").EntityTableComponent.from_dict(obj)
        if object_type ==  'ErrorComponent':
            return import_module("tb_pe_client.models.error_component").ErrorComponent.from_dict(obj)
        if object_type ==  'HeadingComponent':
            return import_module("tb_pe_client.models.heading_component").HeadingComponent.from_dict(obj)
        if object_type ==  'ImageComponent':
            return import_module("tb_pe_client.models.image_component").ImageComponent.from_dict(obj)
        if object_type ==  'LatestChartComponent':
            return import_module("tb_pe_client.models.latest_chart_component").LatestChartComponent.from_dict(obj)
        if object_type ==  'PageBreakComponent':
            return import_module("tb_pe_client.models.page_break_component").PageBreakComponent.from_dict(obj)
        if object_type ==  'RichTextComponent':
            return import_module("tb_pe_client.models.rich_text_component").RichTextComponent.from_dict(obj)
        if object_type ==  'SplitViewComponent':
            return import_module("tb_pe_client.models.split_view_component").SplitViewComponent.from_dict(obj)
        if object_type ==  'SubReportComponent':
            return import_module("tb_pe_client.models.sub_report_component").SubReportComponent.from_dict(obj)
        if object_type ==  'TimeseriesChartComponent':
            return import_module("tb_pe_client.models.timeseries_chart_component").TimeseriesChartComponent.from_dict(obj)
        if object_type ==  'TimeseriesTableComponent':
            return import_module("tb_pe_client.models.timeseries_table_component").TimeseriesTableComponent.from_dict(obj)

        raise ValueError("ReportComponent failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


