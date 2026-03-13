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
from typing import Optional, Set
from typing_extensions import Self

class LicenseUsageInfo(BaseModel):
    """
    LicenseUsageInfo
    """ # noqa: E501
    max_devices: Optional[StrictInt] = Field(default=None, alias="maxDevices")
    max_assets: Optional[StrictInt] = Field(default=None, alias="maxAssets")
    white_labeling_enabled: Optional[StrictBool] = Field(default=None, alias="whiteLabelingEnabled")
    development: Optional[StrictBool] = None
    plan: Optional[StrictStr] = None
    devices_count: Optional[StrictInt] = Field(default=None, alias="devicesCount")
    assets_count: Optional[StrictInt] = Field(default=None, alias="assetsCount")
    dashboards_count: Optional[StrictInt] = Field(default=None, alias="dashboardsCount")
    integrations_count: Optional[StrictInt] = Field(default=None, alias="integrationsCount")
    __properties: ClassVar[List[str]] = ["maxDevices", "maxAssets", "whiteLabelingEnabled", "development", "plan", "devicesCount", "assetsCount", "dashboardsCount", "integrationsCount"]

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
        """Create an instance of LicenseUsageInfo from a JSON string"""
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LicenseUsageInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maxDevices": obj.get("maxDevices"),
            "maxAssets": obj.get("maxAssets"),
            "whiteLabelingEnabled": obj.get("whiteLabelingEnabled"),
            "development": obj.get("development"),
            "plan": obj.get("plan"),
            "devicesCount": obj.get("devicesCount"),
            "assetsCount": obj.get("assetsCount"),
            "dashboardsCount": obj.get("dashboardsCount"),
            "integrationsCount": obj.get("integrationsCount")
        })
        return _obj


