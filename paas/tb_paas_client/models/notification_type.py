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
import json
from enum import Enum
from typing_extensions import Self


class NotificationType(str, Enum):
    """
    NotificationType
    """

    """
    allowed enum values
    """
    GENERAL = 'GENERAL'
    ALARM = 'ALARM'
    DEVICE_ACTIVITY = 'DEVICE_ACTIVITY'
    ENTITY_ACTION = 'ENTITY_ACTION'
    ALARM_COMMENT = 'ALARM_COMMENT'
    RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT = 'RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT'
    ALARM_ASSIGNMENT = 'ALARM_ASSIGNMENT'
    NEW_PLATFORM_VERSION = 'NEW_PLATFORM_VERSION'
    ENTITIES_LIMIT = 'ENTITIES_LIMIT'
    ENTITIES_LIMIT_INCREASE_REQUEST = 'ENTITIES_LIMIT_INCREASE_REQUEST'
    ADDON_ACCESS_REQUEST = 'ADDON_ACCESS_REQUEST'
    ADDON_ACCESS_ERROR = 'ADDON_ACCESS_ERROR'
    PLAN_UPGRADE_REQUEST = 'PLAN_UPGRADE_REQUEST'
    API_USAGE_LIMIT = 'API_USAGE_LIMIT'
    RULE_NODE = 'RULE_NODE'
    INTEGRATION_LIFECYCLE_EVENT = 'INTEGRATION_LIFECYCLE_EVENT'
    RATE_LIMITS = 'RATE_LIMITS'
    EDGE_CONNECTION = 'EDGE_CONNECTION'
    EDGE_COMMUNICATION_FAILURE = 'EDGE_COMMUNICATION_FAILURE'
    TASK_PROCESSING_FAILURE = 'TASK_PROCESSING_FAILURE'
    RESOURCES_SHORTAGE = 'RESOURCES_SHORTAGE'
    USER_ACTIVATED = 'USER_ACTIVATED'
    USER_REGISTERED = 'USER_REGISTERED'
    REPORT_GENERATED = 'REPORT_GENERATED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NotificationType from a JSON string"""
        return cls(json.loads(json_str))


