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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.favicon import Favicon
from tb_paas_client.models.palette_settings import PaletteSettings
from typing import Optional, Set
from typing_extensions import Self

class WhiteLabelingParams(BaseModel):
    """
    A JSON value representing the white labeling configuration
    """ # noqa: E501
    logo_image_url: Optional[StrictStr] = Field(default=None, description="Logo image URL", alias="logoImageUrl")
    logo_image_height: Optional[StrictInt] = Field(default=None, description="The height of a logo container. Logo image will be automatically scaled.", alias="logoImageHeight")
    app_title: Optional[StrictStr] = Field(default=None, description="White-labeled name of the platform", alias="appTitle")
    favicon: Optional[Favicon] = Field(default=None, description="JSON object that contains website icon url and type")
    palette_settings: Optional[PaletteSettings] = Field(default=None, description="Complex JSON that describes structure of the Angular Material Palette. See [theming](https://material.angular.io/guide/theming) for more details", alias="paletteSettings")
    help_link_base_url: Optional[StrictStr] = Field(default=None, description="Base URL for help link", alias="helpLinkBaseUrl")
    ui_help_base_url: Optional[StrictStr] = Field(default=None, description="Base URL for the repository with the UI help components (markdown)", alias="uiHelpBaseUrl")
    enable_help_links: Optional[StrictBool] = Field(default=None, description="Enable or Disable help links", alias="enableHelpLinks")
    white_labeling_enabled: Optional[StrictBool] = Field(default=None, description="Enable white-labeling", alias="whiteLabelingEnabled")
    show_name_version: Optional[StrictBool] = Field(default=None, description="Show platform name and version on UI and login screen", alias="showNameVersion")
    platform_name: Optional[StrictStr] = Field(default=None, description="White-labeled platform name", alias="platformName")
    platform_version: Optional[StrictStr] = Field(default=None, description="White-labeled platform version", alias="platformVersion")
    custom_css: Optional[StrictStr] = Field(default=None, description="Custom CSS content", alias="customCss")
    hide_connectivity_dialog: Optional[StrictBool] = Field(default=None, description="Hide device connectivity dialog", alias="hideConnectivityDialog")
    override_trendz_name: Optional[StrictBool] = Field(default=None, description="Override Trendz Add-on name", alias="overrideTrendzName")
    hide_chat_bot: Optional[StrictBool] = Field(default=None, description="Hide chat bot", alias="hideChatBot")
    __properties: ClassVar[List[str]] = ["logoImageUrl", "logoImageHeight", "appTitle", "favicon", "paletteSettings", "helpLinkBaseUrl", "uiHelpBaseUrl", "enableHelpLinks", "whiteLabelingEnabled", "showNameVersion", "platformName", "platformVersion", "customCss", "hideConnectivityDialog", "overrideTrendzName", "hideChatBot"]

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
        """Create an instance of WhiteLabelingParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "white_labeling_enabled",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of favicon
        if self.favicon:
            _dict['favicon'] = self.favicon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of palette_settings
        if self.palette_settings:
            _dict['paletteSettings'] = self.palette_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WhiteLabelingParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "logoImageUrl": obj.get("logoImageUrl"),
            "logoImageHeight": obj.get("logoImageHeight"),
            "appTitle": obj.get("appTitle"),
            "favicon": Favicon.from_dict(obj["favicon"]) if obj.get("favicon") is not None else None,
            "paletteSettings": PaletteSettings.from_dict(obj["paletteSettings"]) if obj.get("paletteSettings") is not None else None,
            "helpLinkBaseUrl": obj.get("helpLinkBaseUrl"),
            "uiHelpBaseUrl": obj.get("uiHelpBaseUrl"),
            "enableHelpLinks": obj.get("enableHelpLinks"),
            "whiteLabelingEnabled": obj.get("whiteLabelingEnabled"),
            "showNameVersion": obj.get("showNameVersion"),
            "platformName": obj.get("platformName"),
            "platformVersion": obj.get("platformVersion"),
            "customCss": obj.get("customCss"),
            "hideConnectivityDialog": obj.get("hideConnectivityDialog"),
            "overrideTrendzName": obj.get("overrideTrendzName"),
            "hideChatBot": obj.get("hideChatBot")
        })
        return _obj


