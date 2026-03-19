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
from tb_pe_client.models.font import Font
from typing import Optional, Set
from typing_extensions import Self

class BarSeriesSettings(BaseModel):
    """
    BarSeriesSettings
    """ # noqa: E501
    show_border: Optional[StrictBool] = Field(default=None, alias="showBorder")
    border_width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="borderWidth")
    border_radius: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="borderRadius")
    bar_width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="barWidth")
    show_label: Optional[StrictBool] = Field(default=None, alias="showLabel")
    label_position: Optional[ChartLabelPosition] = Field(default=None, alias="labelPosition")
    label_font: Optional[Font] = Field(default=None, alias="labelFont")
    label_color: Optional[StrictStr] = Field(default=None, alias="labelColor")
    enable_label_background: Optional[StrictBool] = Field(default=None, alias="enableLabelBackground")
    label_background: Optional[StrictStr] = Field(default=None, alias="labelBackground")
    background_settings: Optional[ChartFillSettings] = Field(default=None, alias="backgroundSettings")
    __properties: ClassVar[List[str]] = ["showBorder", "borderWidth", "borderRadius", "barWidth", "showLabel", "labelPosition", "labelFont", "labelColor", "enableLabelBackground", "labelBackground", "backgroundSettings"]

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
        """Create an instance of BarSeriesSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of background_settings
        if self.background_settings:
            _dict['backgroundSettings'] = self.background_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BarSeriesSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "showBorder": obj.get("showBorder"),
            "borderWidth": obj.get("borderWidth"),
            "borderRadius": obj.get("borderRadius"),
            "barWidth": obj.get("barWidth"),
            "showLabel": obj.get("showLabel"),
            "labelPosition": obj.get("labelPosition"),
            "labelFont": Font.from_dict(obj["labelFont"]) if obj.get("labelFont") is not None else None,
            "labelColor": obj.get("labelColor"),
            "enableLabelBackground": obj.get("enableLabelBackground"),
            "labelBackground": obj.get("labelBackground"),
            "backgroundSettings": ChartFillSettings.from_dict(obj["backgroundSettings"]) if obj.get("backgroundSettings") is not None else None
        })
        return _obj


