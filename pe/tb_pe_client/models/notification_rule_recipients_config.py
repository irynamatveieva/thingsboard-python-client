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

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Union
from tb_pe_client.models.notification_rule_trigger_type import NotificationRuleTriggerType
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_pe_client.models.escalated_notification_rule_recipients_config import EscalatedNotificationRuleRecipientsConfig
    from tb_pe_client.models.alarm_assignment_recipients_config import AlarmAssignmentRecipientsConfig
    from tb_pe_client.models.alarm_comment_recipients_config import AlarmCommentRecipientsConfig
    from tb_pe_client.models.api_usage_limit_recipients_config import ApiUsageLimitRecipientsConfig
    from tb_pe_client.models.device_activity_recipients_config import DeviceActivityRecipientsConfig
    from tb_pe_client.models.edge_communication_failure_recipients_config import EdgeCommunicationFailureRecipientsConfig
    from tb_pe_client.models.edge_connection_recipients_config import EdgeConnectionRecipientsConfig
    from tb_pe_client.models.entities_limit_recipients_config import EntitiesLimitRecipientsConfig
    from tb_pe_client.models.entity_action_recipients_config import EntityActionRecipientsConfig
    from tb_pe_client.models.integration_lifecycle_event_recipients_config import IntegrationLifecycleEventRecipientsConfig
    from tb_pe_client.models.new_platform_version_recipients_config import NewPlatformVersionRecipientsConfig
    from tb_pe_client.models.rate_limits_recipients_config import RateLimitsRecipientsConfig
    from tb_pe_client.models.resource_shortage_recipients_config import ResourceShortageRecipientsConfig
    from tb_pe_client.models.rule_engine_component_lifecycle_event_recipients_config import RuleEngineComponentLifecycleEventRecipientsConfig
    from tb_pe_client.models.task_processing_failure_recipients_config import TaskProcessingFailureRecipientsConfig

class NotificationRuleRecipientsConfig(BaseModel):
    """
    NotificationRuleRecipientsConfig
    """ # noqa: E501
    trigger_type: NotificationRuleTriggerType = Field(alias="triggerType")
    __properties: ClassVar[List[str]] = ["triggerType"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'triggerType'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ALARM': 'EscalatedNotificationRuleRecipientsConfig','ALARM_ASSIGNMENT': 'AlarmAssignmentRecipientsConfig','ALARM_COMMENT': 'AlarmCommentRecipientsConfig','API_USAGE_LIMIT': 'ApiUsageLimitRecipientsConfig','DEVICE_ACTIVITY': 'DeviceActivityRecipientsConfig','EDGE_COMMUNICATION_FAILURE': 'EdgeCommunicationFailureRecipientsConfig','EDGE_CONNECTION': 'EdgeConnectionRecipientsConfig','ENTITIES_LIMIT': 'EntitiesLimitRecipientsConfig','ENTITY_ACTION': 'EntityActionRecipientsConfig','INTEGRATION_LIFECYCLE_EVENT': 'IntegrationLifecycleEventRecipientsConfig','NEW_PLATFORM_VERSION': 'NewPlatformVersionRecipientsConfig','RATE_LIMITS': 'RateLimitsRecipientsConfig','RESOURCES_SHORTAGE': 'ResourceShortageRecipientsConfig','RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT': 'RuleEngineComponentLifecycleEventRecipientsConfig','TASK_PROCESSING_FAILURE': 'TaskProcessingFailureRecipientsConfig'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[EscalatedNotificationRuleRecipientsConfig, AlarmAssignmentRecipientsConfig, AlarmCommentRecipientsConfig, ApiUsageLimitRecipientsConfig, DeviceActivityRecipientsConfig, EdgeCommunicationFailureRecipientsConfig, EdgeConnectionRecipientsConfig, EntitiesLimitRecipientsConfig, EntityActionRecipientsConfig, IntegrationLifecycleEventRecipientsConfig, NewPlatformVersionRecipientsConfig, RateLimitsRecipientsConfig, ResourceShortageRecipientsConfig, RuleEngineComponentLifecycleEventRecipientsConfig, TaskProcessingFailureRecipientsConfig]]:
        """Create an instance of NotificationRuleRecipientsConfig from a JSON string"""
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
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[EscalatedNotificationRuleRecipientsConfig, AlarmAssignmentRecipientsConfig, AlarmCommentRecipientsConfig, ApiUsageLimitRecipientsConfig, DeviceActivityRecipientsConfig, EdgeCommunicationFailureRecipientsConfig, EdgeConnectionRecipientsConfig, EntitiesLimitRecipientsConfig, EntityActionRecipientsConfig, IntegrationLifecycleEventRecipientsConfig, NewPlatformVersionRecipientsConfig, RateLimitsRecipientsConfig, ResourceShortageRecipientsConfig, RuleEngineComponentLifecycleEventRecipientsConfig, TaskProcessingFailureRecipientsConfig]]:
        """Create an instance of NotificationRuleRecipientsConfig from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'EscalatedNotificationRuleRecipientsConfig':
            return import_module("tb_pe_client.models.escalated_notification_rule_recipients_config").EscalatedNotificationRuleRecipientsConfig.from_dict(obj)
        if object_type ==  'AlarmAssignmentRecipientsConfig':
            return import_module("tb_pe_client.models.alarm_assignment_recipients_config").AlarmAssignmentRecipientsConfig.from_dict(obj)
        if object_type ==  'AlarmCommentRecipientsConfig':
            return import_module("tb_pe_client.models.alarm_comment_recipients_config").AlarmCommentRecipientsConfig.from_dict(obj)
        if object_type ==  'ApiUsageLimitRecipientsConfig':
            return import_module("tb_pe_client.models.api_usage_limit_recipients_config").ApiUsageLimitRecipientsConfig.from_dict(obj)
        if object_type ==  'DeviceActivityRecipientsConfig':
            return import_module("tb_pe_client.models.device_activity_recipients_config").DeviceActivityRecipientsConfig.from_dict(obj)
        if object_type ==  'EdgeCommunicationFailureRecipientsConfig':
            return import_module("tb_pe_client.models.edge_communication_failure_recipients_config").EdgeCommunicationFailureRecipientsConfig.from_dict(obj)
        if object_type ==  'EdgeConnectionRecipientsConfig':
            return import_module("tb_pe_client.models.edge_connection_recipients_config").EdgeConnectionRecipientsConfig.from_dict(obj)
        if object_type ==  'EntitiesLimitRecipientsConfig':
            return import_module("tb_pe_client.models.entities_limit_recipients_config").EntitiesLimitRecipientsConfig.from_dict(obj)
        if object_type ==  'EntityActionRecipientsConfig':
            return import_module("tb_pe_client.models.entity_action_recipients_config").EntityActionRecipientsConfig.from_dict(obj)
        if object_type ==  'IntegrationLifecycleEventRecipientsConfig':
            return import_module("tb_pe_client.models.integration_lifecycle_event_recipients_config").IntegrationLifecycleEventRecipientsConfig.from_dict(obj)
        if object_type ==  'NewPlatformVersionRecipientsConfig':
            return import_module("tb_pe_client.models.new_platform_version_recipients_config").NewPlatformVersionRecipientsConfig.from_dict(obj)
        if object_type ==  'RateLimitsRecipientsConfig':
            return import_module("tb_pe_client.models.rate_limits_recipients_config").RateLimitsRecipientsConfig.from_dict(obj)
        if object_type ==  'ResourceShortageRecipientsConfig':
            return import_module("tb_pe_client.models.resource_shortage_recipients_config").ResourceShortageRecipientsConfig.from_dict(obj)
        if object_type ==  'RuleEngineComponentLifecycleEventRecipientsConfig':
            return import_module("tb_pe_client.models.rule_engine_component_lifecycle_event_recipients_config").RuleEngineComponentLifecycleEventRecipientsConfig.from_dict(obj)
        if object_type ==  'TaskProcessingFailureRecipientsConfig':
            return import_module("tb_pe_client.models.task_processing_failure_recipients_config").TaskProcessingFailureRecipientsConfig.from_dict(obj)

        raise ValueError("NotificationRuleRecipientsConfig failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


