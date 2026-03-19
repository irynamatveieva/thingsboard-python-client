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
from tb_pe_client.models.chart_fill_settings import ChartFillSettings
from tb_pe_client.models.chart_label_position import ChartLabelPosition
from tb_pe_client.models.chart_line_type import ChartLineType
from tb_pe_client.models.chart_shape import ChartShape
from tb_pe_client.models.font import Font
from tb_pe_client.models.line_series_step_type import LineSeriesStepType
from typing import Optional, Set
from typing_extensions import Self

class LineSeriesSettings(BaseModel):
    """
    LineSeriesSettings
    """ # noqa: E501
    show_line: Optional[StrictBool] = Field(default=None, alias="showLine")
    step: Optional[StrictBool] = None
    step_type: Optional[LineSeriesStepType] = Field(default=None, alias="stepType")
    smooth: Optional[StrictBool] = None
    line_type: Optional[ChartLineType] = Field(default=None, alias="lineType")
    line_width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="lineWidth")
    show_points: Optional[StrictBool] = Field(default=None, alias="showPoints")
    show_point_label: Optional[StrictBool] = Field(default=None, alias="showPointLabel")
    point_label_position: Optional[ChartLabelPosition] = Field(default=None, alias="pointLabelPosition")
    point_label_font: Optional[Font] = Field(default=None, alias="pointLabelFont")
    point_label_color: Optional[StrictStr] = Field(default=None, alias="pointLabelColor")
    enable_point_label_background: Optional[StrictBool] = Field(default=None, alias="enablePointLabelBackground")
    point_label_background: Optional[StrictStr] = Field(default=None, alias="pointLabelBackground")
    point_shape: Optional[ChartShape] = Field(default=None, alias="pointShape")
    point_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pointSize")
    fill_area_settings: Optional[ChartFillSettings] = Field(default=None, alias="fillAreaSettings")
    __properties: ClassVar[List[str]] = ["showLine", "step", "stepType", "smooth", "lineType", "lineWidth", "showPoints", "showPointLabel", "pointLabelPosition", "pointLabelFont", "pointLabelColor", "enablePointLabelBackground", "pointLabelBackground", "pointShape", "pointSize", "fillAreaSettings"]

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
        """Create an instance of LineSeriesSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of point_label_font
        if self.point_label_font:
            _dict['pointLabelFont'] = self.point_label_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fill_area_settings
        if self.fill_area_settings:
            _dict['fillAreaSettings'] = self.fill_area_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LineSeriesSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "showLine": obj.get("showLine"),
            "step": obj.get("step"),
            "stepType": obj.get("stepType"),
            "smooth": obj.get("smooth"),
            "lineType": obj.get("lineType"),
            "lineWidth": obj.get("lineWidth"),
            "showPoints": obj.get("showPoints"),
            "showPointLabel": obj.get("showPointLabel"),
            "pointLabelPosition": obj.get("pointLabelPosition"),
            "pointLabelFont": Font.from_dict(obj["pointLabelFont"]) if obj.get("pointLabelFont") is not None else None,
            "pointLabelColor": obj.get("pointLabelColor"),
            "enablePointLabelBackground": obj.get("enablePointLabelBackground"),
            "pointLabelBackground": obj.get("pointLabelBackground"),
            "pointShape": obj.get("pointShape"),
            "pointSize": obj.get("pointSize"),
            "fillAreaSettings": ChartFillSettings.from_dict(obj["fillAreaSettings"]) if obj.get("fillAreaSettings") is not None else None
        })
        return _obj


