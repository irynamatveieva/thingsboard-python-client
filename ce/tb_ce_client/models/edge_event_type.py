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
import json
from enum import Enum
from typing_extensions import Self


class EdgeEventType(str, Enum):
    """
    EdgeEventType
    """

    """
    allowed enum values
    """
    DASHBOARD = 'DASHBOARD'
    ASSET = 'ASSET'
    DEVICE = 'DEVICE'
    DEVICE_PROFILE = 'DEVICE_PROFILE'
    ASSET_PROFILE = 'ASSET_PROFILE'
    ENTITY_VIEW = 'ENTITY_VIEW'
    ALARM = 'ALARM'
    ALARM_COMMENT = 'ALARM_COMMENT'
    RULE_CHAIN = 'RULE_CHAIN'
    RULE_CHAIN_METADATA = 'RULE_CHAIN_METADATA'
    EDGE = 'EDGE'
    USER = 'USER'
    CUSTOMER = 'CUSTOMER'
    RELATION = 'RELATION'
    TENANT = 'TENANT'
    TENANT_PROFILE = 'TENANT_PROFILE'
    WIDGETS_BUNDLE = 'WIDGETS_BUNDLE'
    WIDGET_TYPE = 'WIDGET_TYPE'
    ADMIN_SETTINGS = 'ADMIN_SETTINGS'
    OTA_PACKAGE = 'OTA_PACKAGE'
    QUEUE = 'QUEUE'
    NOTIFICATION_RULE = 'NOTIFICATION_RULE'
    NOTIFICATION_TARGET = 'NOTIFICATION_TARGET'
    NOTIFICATION_TEMPLATE = 'NOTIFICATION_TEMPLATE'
    TB_RESOURCE = 'TB_RESOURCE'
    OAUTH2_CLIENT = 'OAUTH2_CLIENT'
    DOMAIN = 'DOMAIN'
    CALCULATED_FIELD = 'CALCULATED_FIELD'
    AI_MODEL = 'AI_MODEL'
    API_KEY = 'API_KEY'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EdgeEventType from a JSON string"""
        return cls(json.loads(json_str))


