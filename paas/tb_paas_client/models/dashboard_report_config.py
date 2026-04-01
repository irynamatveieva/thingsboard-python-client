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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DashboardReportConfig(BaseModel):
    """
    DashboardReportConfig
    """ # noqa: E501
    base_url: StrictStr = Field(description="Base URL of ThingsBoard UI that should be accessible by Web Report Server.", serialization_alias="baseUrl")
    dashboard_id: StrictStr = Field(description="A string value representing the dashboard id.", serialization_alias="dashboardId")
    state: Optional[StrictStr] = Field(default=None, description="Target dashboard state for dashboard report generation.")
    timezone: StrictStr = Field(description="Timezone in which target dashboard will be presented in dashboard report.")
    use_dashboard_timewindow: Optional[StrictBool] = Field(default=None, description="If set, timewindow configured in the target dashboard will be used during dashboard report generation.", serialization_alias="useDashboardTimewindow")
    timewindow: Optional[Any] = Field(default=None, description="Specific dashboard timewindow that will be used during dashboard report generation.")
    name_pattern: StrictStr = Field(description="If set, timewindow configured in the target dashboard will be used during dashboard report generation.", serialization_alias="namePattern")
    type: Optional[StrictStr] = Field(default=None, description="Dashboard report file type, can be PDF | PNG | JPEG.")
    use_current_user_credentials: Optional[StrictBool] = Field(default=None, description="If set, credentials of user created this dashboard report configuration will be used to open dashboard UI during dashboard report generation.", serialization_alias="useCurrentUserCredentials")
    user_id: StrictStr = Field(description="A string value representing the user id.", serialization_alias="userId")
    __properties: ClassVar[List[str]] = ["baseUrl", "dashboardId", "state", "timezone", "useDashboardTimewindow", "timewindow", "namePattern", "type", "useCurrentUserCredentials", "userId"]

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
        """Create an instance of DashboardReportConfig from a JSON string"""
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
        # set to None if timewindow (nullable) is None
        # and model_fields_set contains the field
        if self.timewindow is None and "timewindow" in self.model_fields_set:
            _dict['timewindow'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DashboardReportConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "base_url": obj.get("baseUrl"),
            "dashboard_id": obj.get("dashboardId"),
            "state": obj.get("state"),
            "timezone": obj.get("timezone"),
            "use_dashboard_timewindow": obj.get("useDashboardTimewindow"),
            "timewindow": obj.get("timewindow"),
            "name_pattern": obj.get("namePattern"),
            "type": obj.get("type"),
            "use_current_user_credentials": obj.get("useCurrentUserCredentials"),
            "user_id": obj.get("userId")
        })
        return _obj


