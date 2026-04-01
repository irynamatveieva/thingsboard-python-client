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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tb_ce_client.models.notification_delivery_method import NotificationDeliveryMethod
from tb_ce_client.models.notification_rule_config import NotificationRuleConfig
from tb_ce_client.models.notification_rule_id import NotificationRuleId
from tb_ce_client.models.notification_rule_recipients_config import NotificationRuleRecipientsConfig
from tb_ce_client.models.notification_rule_trigger_config import NotificationRuleTriggerConfig
from tb_ce_client.models.notification_rule_trigger_type import NotificationRuleTriggerType
from tb_ce_client.models.notification_template_id import NotificationTemplateId
from tb_ce_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class NotificationRuleInfo(BaseModel):
    """
    NotificationRuleInfo
    """ # noqa: E501
    id: Optional[NotificationRuleId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", serialization_alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, serialization_alias="tenantId")
    name: Annotated[str, Field(min_length=1, strict=True)]
    enabled: Optional[StrictBool] = None
    template_id: NotificationTemplateId = Field(serialization_alias="templateId")
    trigger_type: NotificationRuleTriggerType = Field(serialization_alias="triggerType")
    trigger_config: NotificationRuleTriggerConfig = Field(serialization_alias="triggerConfig")
    recipients_config: NotificationRuleRecipientsConfig = Field(serialization_alias="recipientsConfig")
    additional_config: Optional[NotificationRuleConfig] = Field(default=None, serialization_alias="additionalConfig")
    template_name: Optional[StrictStr] = Field(default=None, serialization_alias="templateName")
    delivery_methods: Optional[List[NotificationDeliveryMethod]] = Field(default=None, serialization_alias="deliveryMethods")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "name", "enabled", "templateId", "triggerType", "triggerConfig", "recipientsConfig", "additionalConfig", "templateName", "deliveryMethods"]

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
        """Create an instance of NotificationRuleInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of trigger_config
        if self.trigger_config:
            _dict['triggerConfig'] = self.trigger_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recipients_config
        if self.recipients_config:
            _dict['recipientsConfig'] = self.recipients_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of additional_config
        if self.additional_config:
            _dict['additionalConfig'] = self.additional_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationRuleInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": NotificationRuleId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "name": obj.get("name"),
            "enabled": obj.get("enabled"),
            "template_id": NotificationTemplateId.from_dict(obj["templateId"]) if obj.get("templateId") is not None else None,
            "trigger_type": obj.get("triggerType"),
            "trigger_config": NotificationRuleTriggerConfig.from_dict(obj["triggerConfig"]) if obj.get("triggerConfig") is not None else None,
            "recipients_config": NotificationRuleRecipientsConfig.from_dict(obj["recipientsConfig"]) if obj.get("recipientsConfig") is not None else None,
            "additional_config": NotificationRuleConfig.from_dict(obj["additionalConfig"]) if obj.get("additionalConfig") is not None else None,
            "template_name": obj.get("templateName"),
            "delivery_methods": obj.get("deliveryMethods")
        })
        return _obj


