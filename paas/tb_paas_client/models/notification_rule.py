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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tb_paas_client.models.notification_rule_config import NotificationRuleConfig
from tb_paas_client.models.notification_rule_id import NotificationRuleId
from tb_paas_client.models.notification_rule_recipients_config import NotificationRuleRecipientsConfig
from tb_paas_client.models.notification_rule_trigger_config import NotificationRuleTriggerConfig
from tb_paas_client.models.notification_rule_trigger_type import NotificationRuleTriggerType
from tb_paas_client.models.notification_template_id import NotificationTemplateId
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class NotificationRule(BaseModel):
    """
    NotificationRule
    """ # noqa: E501
    id: Optional[NotificationRuleId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, alias="tenantId")
    name: Annotated[str, Field(min_length=1, strict=True)]
    enabled: Optional[StrictBool] = None
    template_id: NotificationTemplateId = Field(alias="templateId")
    trigger_type: NotificationRuleTriggerType = Field(alias="triggerType")
    trigger_config: NotificationRuleTriggerConfig = Field(alias="triggerConfig")
    recipients_config: NotificationRuleRecipientsConfig = Field(alias="recipientsConfig")
    additional_config: Optional[NotificationRuleConfig] = Field(default=None, alias="additionalConfig")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "name", "enabled", "templateId", "triggerType", "triggerConfig", "recipientsConfig", "additionalConfig"]

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
        """Create an instance of NotificationRule from a JSON string"""
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
        """Create an instance of NotificationRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": NotificationRuleId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "name": obj.get("name"),
            "enabled": obj.get("enabled"),
            "templateId": NotificationTemplateId.from_dict(obj["templateId"]) if obj.get("templateId") is not None else None,
            "triggerType": obj.get("triggerType"),
            "triggerConfig": NotificationRuleTriggerConfig.from_dict(obj["triggerConfig"]) if obj.get("triggerConfig") is not None else None,
            "recipientsConfig": NotificationRuleRecipientsConfig.from_dict(obj["recipientsConfig"]) if obj.get("recipientsConfig") is not None else None,
            "additionalConfig": NotificationRuleConfig.from_dict(obj["additionalConfig"]) if obj.get("additionalConfig") is not None else None
        })
        return _obj


