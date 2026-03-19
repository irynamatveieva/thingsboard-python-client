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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.action_status import ActionStatus
from tb_pe_client.models.action_type import ActionType
from tb_pe_client.models.audit_log_id import AuditLogId
from tb_pe_client.models.customer_id import CustomerId
from tb_pe_client.models.entity_id import EntityId
from tb_pe_client.models.tenant_id import TenantId
from tb_pe_client.models.user_id import UserId
from typing import Optional, Set
from typing_extensions import Self

class AuditLog(BaseModel):
    """
    AuditLog
    """ # noqa: E501
    id: Optional[AuditLogId] = Field(default=None, description="JSON object with the auditLog Id")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the auditLog creation, in milliseconds", alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id", alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, description="JSON object with Customer Id", alias="customerId")
    entity_id: Optional[EntityId] = Field(default=None, description="JSON object with Entity id", alias="entityId")
    entity_name: Optional[StrictStr] = Field(default=None, description="Name of the logged entity", alias="entityName")
    user_id: Optional[UserId] = Field(default=None, description="JSON object with User id.", alias="userId")
    user_name: Optional[StrictStr] = Field(default=None, description="Unique user name(email) of the user that performed some action on logged entity", alias="userName")
    action_type: Optional[ActionType] = Field(default=None, description="String represented Action type", alias="actionType")
    action_data: Optional[Any] = Field(default=None, description="JsonNode represented action data", alias="actionData")
    action_status: Optional[ActionStatus] = Field(default=None, description="String represented Action status", alias="actionStatus")
    action_failure_details: Optional[StrictStr] = Field(default=None, description="Failure action details info. An empty string in case of action status type 'SUCCESS', otherwise includes stack trace of the caused exception.", alias="actionFailureDetails")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "customerId", "entityId", "entityName", "userId", "userName", "actionType", "actionData", "actionStatus", "actionFailureDetails"]

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
        """Create an instance of AuditLog from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "customer_id",
            "entity_id",
            "entity_name",
            "user_id",
            "user_name",
            "action_type",
            "action_data",
            "action_status",
            "action_failure_details",
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
        # override the default output from pydantic by calling `to_dict()` of entity_id
        if self.entity_id:
            _dict['entityId'] = self.entity_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_id
        if self.user_id:
            _dict['userId'] = self.user_id.to_dict()
        # set to None if action_data (nullable) is None
        # and model_fields_set contains the field
        if self.action_data is None and "action_data" in self.model_fields_set:
            _dict['actionData'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuditLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": AuditLogId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customerId": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "entityId": EntityId.from_dict(obj["entityId"]) if obj.get("entityId") is not None else None,
            "entityName": obj.get("entityName"),
            "userId": UserId.from_dict(obj["userId"]) if obj.get("userId") is not None else None,
            "userName": obj.get("userName"),
            "actionType": obj.get("actionType"),
            "actionData": obj.get("actionData"),
            "actionStatus": obj.get("actionStatus"),
            "actionFailureDetails": obj.get("actionFailureDetails")
        })
        return _obj


