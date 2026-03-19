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
from typing_extensions import Annotated
from uuid import UUID
from tb_pe_client.models.entity_id import EntityId
from tb_pe_client.models.notification_delivery_method import NotificationDeliveryMethod
from tb_pe_client.models.notification_info import NotificationInfo
from tb_pe_client.models.notification_request_config import NotificationRequestConfig
from tb_pe_client.models.notification_request_id import NotificationRequestId
from tb_pe_client.models.notification_request_stats import NotificationRequestStats
from tb_pe_client.models.notification_request_status import NotificationRequestStatus
from tb_pe_client.models.notification_rule_id import NotificationRuleId
from tb_pe_client.models.notification_template import NotificationTemplate
from tb_pe_client.models.notification_template_id import NotificationTemplateId
from tb_pe_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class NotificationRequestInfo(BaseModel):
    """
    NotificationRequestInfo
    """ # noqa: E501
    id: Optional[NotificationRequestId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, alias="tenantId")
    targets: Annotated[List[UUID], Field(min_length=1)]
    template_id: Optional[NotificationTemplateId] = Field(default=None, alias="templateId")
    template: Optional[NotificationTemplate] = None
    info: Optional[NotificationInfo] = None
    additional_config: Optional[NotificationRequestConfig] = Field(default=None, alias="additionalConfig")
    originator_entity_id: Optional[EntityId] = Field(default=None, alias="originatorEntityId")
    rule_id: Optional[NotificationRuleId] = Field(default=None, alias="ruleId")
    status: Optional[NotificationRequestStatus] = None
    stats: Optional[NotificationRequestStats] = None
    template_name: Optional[StrictStr] = Field(default=None, alias="templateName")
    delivery_methods: Optional[List[NotificationDeliveryMethod]] = Field(default=None, alias="deliveryMethods")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "targets", "templateId", "template", "info", "additionalConfig", "originatorEntityId", "ruleId", "status", "stats", "templateName", "deliveryMethods"]

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
        """Create an instance of NotificationRequestInfo from a JSON string"""
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
            "created_time",
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
        # override the default output from pydantic by calling `to_dict()` of template_id
        if self.template_id:
            _dict['templateId'] = self.template_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict['template'] = self.template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict['info'] = self.info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of additional_config
        if self.additional_config:
            _dict['additionalConfig'] = self.additional_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of originator_entity_id
        if self.originator_entity_id:
            _dict['originatorEntityId'] = self.originator_entity_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rule_id
        if self.rule_id:
            _dict['ruleId'] = self.rule_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": NotificationRequestId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "targets": obj.get("targets"),
            "templateId": NotificationTemplateId.from_dict(obj["templateId"]) if obj.get("templateId") is not None else None,
            "template": NotificationTemplate.from_dict(obj["template"]) if obj.get("template") is not None else None,
            "info": NotificationInfo.from_dict(obj["info"]) if obj.get("info") is not None else None,
            "additionalConfig": NotificationRequestConfig.from_dict(obj["additionalConfig"]) if obj.get("additionalConfig") is not None else None,
            "originatorEntityId": EntityId.from_dict(obj["originatorEntityId"]) if obj.get("originatorEntityId") is not None else None,
            "ruleId": NotificationRuleId.from_dict(obj["ruleId"]) if obj.get("ruleId") is not None else None,
            "status": obj.get("status"),
            "stats": NotificationRequestStats.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            "templateName": obj.get("templateName"),
            "deliveryMethods": obj.get("deliveryMethods")
        })
        return _obj


