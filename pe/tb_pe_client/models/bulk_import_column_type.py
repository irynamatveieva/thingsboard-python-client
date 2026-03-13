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


class BulkImportColumnType(str, Enum):
    """
    BulkImportColumnType
    """

    """
    allowed enum values
    """
    NAME = 'NAME'
    TYPE = 'TYPE'
    LABEL = 'LABEL'
    SHARED_ATTRIBUTE = 'SHARED_ATTRIBUTE'
    SERVER_ATTRIBUTE = 'SERVER_ATTRIBUTE'
    TIMESERIES = 'TIMESERIES'
    ACCESS_TOKEN = 'ACCESS_TOKEN'
    X509 = 'X509'
    MQTT_CLIENT_ID = 'MQTT_CLIENT_ID'
    MQTT_USER_NAME = 'MQTT_USER_NAME'
    MQTT_PASSWORD = 'MQTT_PASSWORD'
    LWM2_M_CLIENT_ENDPOINT = 'LWM2M_CLIENT_ENDPOINT'
    LWM2_M_CLIENT_SECURITY_CONFIG_MODE = 'LWM2M_CLIENT_SECURITY_CONFIG_MODE'
    LWM2_M_CLIENT_IDENTITY = 'LWM2M_CLIENT_IDENTITY'
    LWM2_M_CLIENT_KEY = 'LWM2M_CLIENT_KEY'
    LWM2_M_CLIENT_CERT = 'LWM2M_CLIENT_CERT'
    LWM2_M_BOOTSTRAP_SERVER_SECURITY_MODE = 'LWM2M_BOOTSTRAP_SERVER_SECURITY_MODE'
    LWM2_M_BOOTSTRAP_SERVER_PUBLIC_KEY_OR_ID = 'LWM2M_BOOTSTRAP_SERVER_PUBLIC_KEY_OR_ID'
    LWM2_M_BOOTSTRAP_SERVER_SECRET_KEY = 'LWM2M_BOOTSTRAP_SERVER_SECRET_KEY'
    LWM2_M_SERVER_SECURITY_MODE = 'LWM2M_SERVER_SECURITY_MODE'
    LWM2_M_SERVER_CLIENT_PUBLIC_KEY_OR_ID = 'LWM2M_SERVER_CLIENT_PUBLIC_KEY_OR_ID'
    LWM2_M_SERVER_CLIENT_SECRET_KEY = 'LWM2M_SERVER_CLIENT_SECRET_KEY'
    SNMP_HOST = 'SNMP_HOST'
    SNMP_PORT = 'SNMP_PORT'
    SNMP_VERSION = 'SNMP_VERSION'
    SNMP_COMMUNITY_STRING = 'SNMP_COMMUNITY_STRING'
    IS_GATEWAY = 'IS_GATEWAY'
    DESCRIPTION = 'DESCRIPTION'
    EDGE_LICENSE_KEY = 'EDGE_LICENSE_KEY'
    CLOUD_ENDPOINT = 'CLOUD_ENDPOINT'
    ROUTING_KEY = 'ROUTING_KEY'
    SECRET = 'SECRET'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BulkImportColumnType from a JSON string"""
        return cls(json.loads(json_str))


