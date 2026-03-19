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

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Union
from tb_ce_client.models.notification_rule_trigger_type import NotificationRuleTriggerType
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_ce_client.models.alarm_notification_rule_trigger_config import AlarmNotificationRuleTriggerConfig
    from tb_ce_client.models.alarm_assignment_notification_rule_trigger_config import AlarmAssignmentNotificationRuleTriggerConfig
    from tb_ce_client.models.alarm_comment_notification_rule_trigger_config import AlarmCommentNotificationRuleTriggerConfig
    from tb_ce_client.models.api_usage_limit_notification_rule_trigger_config import ApiUsageLimitNotificationRuleTriggerConfig
    from tb_ce_client.models.device_activity_notification_rule_trigger_config import DeviceActivityNotificationRuleTriggerConfig
    from tb_ce_client.models.edge_communication_failure_notification_rule_trigger_config import EdgeCommunicationFailureNotificationRuleTriggerConfig
    from tb_ce_client.models.edge_connection_notification_rule_trigger_config import EdgeConnectionNotificationRuleTriggerConfig
    from tb_ce_client.models.entities_limit_notification_rule_trigger_config import EntitiesLimitNotificationRuleTriggerConfig
    from tb_ce_client.models.entity_action_notification_rule_trigger_config import EntityActionNotificationRuleTriggerConfig
    from tb_ce_client.models.new_platform_version_notification_rule_trigger_config import NewPlatformVersionNotificationRuleTriggerConfig
    from tb_ce_client.models.rate_limits_notification_rule_trigger_config import RateLimitsNotificationRuleTriggerConfig
    from tb_ce_client.models.resources_shortage_notification_rule_trigger_config import ResourcesShortageNotificationRuleTriggerConfig
    from tb_ce_client.models.rule_engine_component_lifecycle_event_notification_rule_trigger_config import RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig
    from tb_ce_client.models.task_processing_failure_notification_rule_trigger_config import TaskProcessingFailureNotificationRuleTriggerConfig

class NotificationRuleTriggerConfig(BaseModel):
    """
    Configuration for notification rule trigger
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
        'ALARM': 'AlarmNotificationRuleTriggerConfig','ALARM_ASSIGNMENT': 'AlarmAssignmentNotificationRuleTriggerConfig','ALARM_COMMENT': 'AlarmCommentNotificationRuleTriggerConfig','API_USAGE_LIMIT': 'ApiUsageLimitNotificationRuleTriggerConfig','DEVICE_ACTIVITY': 'DeviceActivityNotificationRuleTriggerConfig','EDGE_COMMUNICATION_FAILURE': 'EdgeCommunicationFailureNotificationRuleTriggerConfig','EDGE_CONNECTION': 'EdgeConnectionNotificationRuleTriggerConfig','ENTITIES_LIMIT': 'EntitiesLimitNotificationRuleTriggerConfig','ENTITY_ACTION': 'EntityActionNotificationRuleTriggerConfig','NEW_PLATFORM_VERSION': 'NewPlatformVersionNotificationRuleTriggerConfig','RATE_LIMITS': 'RateLimitsNotificationRuleTriggerConfig','RESOURCES_SHORTAGE': 'ResourcesShortageNotificationRuleTriggerConfig','RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT': 'RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig','TASK_PROCESSING_FAILURE': 'TaskProcessingFailureNotificationRuleTriggerConfig'
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
    def from_json(cls, json_str: str) -> Optional[Union[AlarmNotificationRuleTriggerConfig, AlarmAssignmentNotificationRuleTriggerConfig, AlarmCommentNotificationRuleTriggerConfig, ApiUsageLimitNotificationRuleTriggerConfig, DeviceActivityNotificationRuleTriggerConfig, EdgeCommunicationFailureNotificationRuleTriggerConfig, EdgeConnectionNotificationRuleTriggerConfig, EntitiesLimitNotificationRuleTriggerConfig, EntityActionNotificationRuleTriggerConfig, NewPlatformVersionNotificationRuleTriggerConfig, RateLimitsNotificationRuleTriggerConfig, ResourcesShortageNotificationRuleTriggerConfig, RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig, TaskProcessingFailureNotificationRuleTriggerConfig]]:
        """Create an instance of NotificationRuleTriggerConfig from a JSON string"""
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
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[AlarmNotificationRuleTriggerConfig, AlarmAssignmentNotificationRuleTriggerConfig, AlarmCommentNotificationRuleTriggerConfig, ApiUsageLimitNotificationRuleTriggerConfig, DeviceActivityNotificationRuleTriggerConfig, EdgeCommunicationFailureNotificationRuleTriggerConfig, EdgeConnectionNotificationRuleTriggerConfig, EntitiesLimitNotificationRuleTriggerConfig, EntityActionNotificationRuleTriggerConfig, NewPlatformVersionNotificationRuleTriggerConfig, RateLimitsNotificationRuleTriggerConfig, ResourcesShortageNotificationRuleTriggerConfig, RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig, TaskProcessingFailureNotificationRuleTriggerConfig]]:
        """Create an instance of NotificationRuleTriggerConfig from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'AlarmNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.alarm_notification_rule_trigger_config").AlarmNotificationRuleTriggerConfig.from_dict(obj)
        if object_type ==  'AlarmAssignmentNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.alarm_assignment_notification_rule_trigger_config").AlarmAssignmentNotificationRuleTriggerConfig.from_dict(obj)
        if object_type ==  'AlarmCommentNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.alarm_comment_notification_rule_trigger_config").AlarmCommentNotificationRuleTriggerConfig.from_dict(obj)
        if object_type ==  'ApiUsageLimitNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.api_usage_limit_notification_rule_trigger_config").ApiUsageLimitNotificationRuleTriggerConfig.from_dict(obj)
        if object_type ==  'DeviceActivityNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.device_activity_notification_rule_trigger_config").DeviceActivityNotificationRuleTriggerConfig.from_dict(obj)
        if object_type ==  'EdgeCommunicationFailureNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.edge_communication_failure_notification_rule_trigger_config").EdgeCommunicationFailureNotificationRuleTriggerConfig.from_dict(obj)
        if object_type ==  'EdgeConnectionNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.edge_connection_notification_rule_trigger_config").EdgeConnectionNotificationRuleTriggerConfig.from_dict(obj)
        if object_type ==  'EntitiesLimitNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.entities_limit_notification_rule_trigger_config").EntitiesLimitNotificationRuleTriggerConfig.from_dict(obj)
        if object_type ==  'EntityActionNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.entity_action_notification_rule_trigger_config").EntityActionNotificationRuleTriggerConfig.from_dict(obj)
        if object_type ==  'NewPlatformVersionNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.new_platform_version_notification_rule_trigger_config").NewPlatformVersionNotificationRuleTriggerConfig.from_dict(obj)
        if object_type ==  'RateLimitsNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.rate_limits_notification_rule_trigger_config").RateLimitsNotificationRuleTriggerConfig.from_dict(obj)
        if object_type ==  'ResourcesShortageNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.resources_shortage_notification_rule_trigger_config").ResourcesShortageNotificationRuleTriggerConfig.from_dict(obj)
        if object_type ==  'RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.rule_engine_component_lifecycle_event_notification_rule_trigger_config").RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.from_dict(obj)
        if object_type ==  'TaskProcessingFailureNotificationRuleTriggerConfig':
            return import_module("tb_ce_client.models.task_processing_failure_notification_rule_trigger_config").TaskProcessingFailureNotificationRuleTriggerConfig.from_dict(obj)

        raise ValueError("NotificationRuleTriggerConfig failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


