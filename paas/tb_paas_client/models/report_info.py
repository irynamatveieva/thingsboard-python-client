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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tb_paas_client.models.customer_id import CustomerId
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.entity_info import EntityInfo
from tb_paas_client.models.report_id import ReportId
from tb_paas_client.models.report_template_id import ReportTemplateId
from tb_paas_client.models.tb_report_format import TbReportFormat
from tb_paas_client.models.tenant_id import TenantId
from tb_paas_client.models.user_id import UserId
from typing import Optional, Set
from typing_extensions import Self

class ReportInfo(BaseModel):
    """
    ReportInfo
    """ # noqa: E501
    id: Optional[ReportId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", alias="createdTime")
    tenant_id: TenantId = Field(alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, alias="customerId")
    template_id: ReportTemplateId = Field(alias="templateId")
    format: TbReportFormat
    name: Annotated[str, Field(min_length=1, strict=True)]
    user_id: UserId = Field(alias="userId")
    template_info: Optional[EntityInfo] = Field(default=None, alias="templateInfo")
    customer_title: Optional[StrictStr] = Field(default=None, alias="customerTitle")
    user_name: Optional[StrictStr] = Field(default=None, alias="userName")
    owner_id: Optional[EntityId] = Field(default=None, description="JSON object with Customer or Tenant Id", alias="ownerId")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "customerId", "templateId", "format", "name", "userId", "templateInfo", "customerTitle", "userName", "ownerId"]

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
        """Create an instance of ReportInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "owner_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenantId'] = self.tenant_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_id
        if self.customer_id:
            _dict['customerId'] = self.customer_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of template_id
        if self.template_id:
            _dict['templateId'] = self.template_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_id
        if self.user_id:
            _dict['userId'] = self.user_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of template_info
        if self.template_info:
            _dict['templateInfo'] = self.template_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner_id
        if self.owner_id:
            _dict['ownerId'] = self.owner_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": ReportId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customerId": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "templateId": ReportTemplateId.from_dict(obj["templateId"]) if obj.get("templateId") is not None else None,
            "format": obj.get("format"),
            "name": obj.get("name"),
            "userId": UserId.from_dict(obj["userId"]) if obj.get("userId") is not None else None,
            "templateInfo": EntityInfo.from_dict(obj["templateInfo"]) if obj.get("templateInfo") is not None else None,
            "customerTitle": obj.get("customerTitle"),
            "userName": obj.get("userName"),
            "ownerId": EntityId.from_dict(obj["ownerId"]) if obj.get("ownerId") is not None else None
        })
        return _obj


