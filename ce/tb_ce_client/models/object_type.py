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


class ObjectType(str, Enum):
    """
    ObjectType
    """

    """
    allowed enum values
    """
    TENANT = 'TENANT'
    TENANT_PROFILE = 'TENANT_PROFILE'
    CUSTOMER = 'CUSTOMER'
    QUEUE = 'QUEUE'
    RPC = 'RPC'
    RULE_CHAIN = 'RULE_CHAIN'
    OTA_PACKAGE = 'OTA_PACKAGE'
    RESOURCE = 'RESOURCE'
    EVENT = 'EVENT'
    RULE_NODE = 'RULE_NODE'
    USER = 'USER'
    EDGE = 'EDGE'
    WIDGETS_BUNDLE = 'WIDGETS_BUNDLE'
    WIDGET_TYPE = 'WIDGET_TYPE'
    DASHBOARD = 'DASHBOARD'
    DEVICE_PROFILE = 'DEVICE_PROFILE'
    DEVICE = 'DEVICE'
    DEVICE_CREDENTIALS = 'DEVICE_CREDENTIALS'
    ASSET_PROFILE = 'ASSET_PROFILE'
    ASSET = 'ASSET'
    ENTITY_VIEW = 'ENTITY_VIEW'
    ALARM = 'ALARM'
    ENTITY_ALARM = 'ENTITY_ALARM'
    OAUTH2_CLIENT = 'OAUTH2_CLIENT'
    OAUTH2_DOMAIN = 'OAUTH2_DOMAIN'
    OAUTH2_MOBILE = 'OAUTH2_MOBILE'
    USER_SETTINGS = 'USER_SETTINGS'
    NOTIFICATION_TARGET = 'NOTIFICATION_TARGET'
    NOTIFICATION_TEMPLATE = 'NOTIFICATION_TEMPLATE'
    NOTIFICATION_RULE = 'NOTIFICATION_RULE'
    ALARM_COMMENT = 'ALARM_COMMENT'
    API_USAGE_STATE = 'API_USAGE_STATE'
    QUEUE_STATS = 'QUEUE_STATS'
    AUDIT_LOG = 'AUDIT_LOG'
    RELATION = 'RELATION'
    ATTRIBUTE_KV = 'ATTRIBUTE_KV'
    LATEST_TS_KV = 'LATEST_TS_KV'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ObjectType from a JSON string"""
        return cls(json.loads(json_str))


