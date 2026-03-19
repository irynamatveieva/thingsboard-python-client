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
from tb_pe_client.models.customer_id import CustomerId
from tb_pe_client.models.dashboard_id import DashboardId
from tb_pe_client.models.entity_group_id import EntityGroupId
from typing import Optional, Set
from typing_extensions import Self

class TenantSolutionTemplateInstructions(BaseModel):
    """
    TenantSolutionTemplateInstructions
    """ # noqa: E501
    dashboard_group_id: Optional[EntityGroupId] = Field(default=None, description="Id of the group that contains main dashboard of the solution", alias="dashboardGroupId")
    dashboard_id: Optional[DashboardId] = Field(default=None, description="Id of the main dashboard of the solution", alias="dashboardId")
    public_id: Optional[CustomerId] = Field(default=None, description="Id of the public customer if solution has public entities", alias="publicId")
    main_dashboard_public: Optional[StrictBool] = Field(default=None, description="Is the main dashboard public", alias="mainDashboardPublic")
    details: Optional[StrictStr] = Field(default=None, description="Markdown with solution usage instructions")
    __properties: ClassVar[List[str]] = ["dashboardGroupId", "dashboardId", "publicId", "mainDashboardPublic", "details"]

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
        """Create an instance of TenantSolutionTemplateInstructions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dashboard_group_id
        if self.dashboard_group_id:
            _dict['dashboardGroupId'] = self.dashboard_group_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dashboard_id
        if self.dashboard_id:
            _dict['dashboardId'] = self.dashboard_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of public_id
        if self.public_id:
            _dict['publicId'] = self.public_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantSolutionTemplateInstructions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dashboardGroupId": EntityGroupId.from_dict(obj["dashboardGroupId"]) if obj.get("dashboardGroupId") is not None else None,
            "dashboardId": DashboardId.from_dict(obj["dashboardId"]) if obj.get("dashboardId") is not None else None,
            "publicId": CustomerId.from_dict(obj["publicId"]) if obj.get("publicId") is not None else None,
            "mainDashboardPublic": obj.get("mainDashboardPublic"),
            "details": obj.get("details")
        })
        return _obj


