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
from tb_paas_client.models.bar_series_settings import BarSeriesSettings
from tb_paas_client.models.data_key_comparison_settings import DataKeyComparisonSettings
from tb_paas_client.models.data_key_settings import DataKeySettings
from tb_paas_client.models.data_key_settings_type import DataKeySettingsType
from tb_paas_client.models.line_series_settings import LineSeriesSettings
from tb_paas_client.models.time_series_chart_series_type import TimeSeriesChartSeriesType
from typing import Optional, Set
from typing_extensions import Self

class TimeSeriesChartKeySettings(DataKeySettings):
    """
    TimeSeriesChartKeySettings
    """ # noqa: E501
    y_axis_id: Optional[StrictStr] = Field(default=None, alias="yAxisId")
    show_in_legend: Optional[StrictBool] = Field(default=None, alias="showInLegend")
    series_type: Optional[TimeSeriesChartSeriesType] = Field(default=None, alias="seriesType")
    line_settings: Optional[LineSeriesSettings] = Field(default=None, alias="lineSettings")
    bar_settings: Optional[BarSeriesSettings] = Field(default=None, alias="barSettings")
    comparison_settings: Optional[DataKeyComparisonSettings] = Field(default=None, alias="comparisonSettings")
    yaxis_id: Optional[StrictStr] = Field(default=None, alias="yaxisId")
    __properties: ClassVar[List[str]] = ["type", "yAxisId", "showInLegend", "seriesType", "lineSettings", "barSettings", "comparisonSettings", "yaxisId"]

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
        """Create an instance of TimeSeriesChartKeySettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of line_settings
        if self.line_settings:
            _dict['lineSettings'] = self.line_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bar_settings
        if self.bar_settings:
            _dict['barSettings'] = self.bar_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of comparison_settings
        if self.comparison_settings:
            _dict['comparisonSettings'] = self.comparison_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimeSeriesChartKeySettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "yAxisId": obj.get("yAxisId"),
            "showInLegend": obj.get("showInLegend"),
            "seriesType": obj.get("seriesType"),
            "lineSettings": LineSeriesSettings.from_dict(obj["lineSettings"]) if obj.get("lineSettings") is not None else None,
            "barSettings": BarSeriesSettings.from_dict(obj["barSettings"]) if obj.get("barSettings") is not None else None,
            "comparisonSettings": DataKeyComparisonSettings.from_dict(obj["comparisonSettings"]) if obj.get("comparisonSettings") is not None else None,
            "yaxisId": obj.get("yaxisId")
        })
        return _obj


