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


class IntegrationType(str, Enum):
    """
    IntegrationType
    """

    """
    allowed enum values
    """
    OCEANCONNECT = 'OCEANCONNECT'
    SIGFOX = 'SIGFOX'
    THINGPARK = 'THINGPARK'
    TPE = 'TPE'
    CHIRPSTACK = 'CHIRPSTACK'
    PARTICLE = 'PARTICLE'
    TMOBILE_IOT_CDP = 'TMOBILE_IOT_CDP'
    HTTP = 'HTTP'
    MQTT = 'MQTT'
    PUB_SUB = 'PUB_SUB'
    AWS_IOT = 'AWS_IOT'
    AWS_SQS = 'AWS_SQS'
    AWS_KINESIS = 'AWS_KINESIS'
    TTN = 'TTN'
    TTI = 'TTI'
    AZURE_EVENT_HUB = 'AZURE_EVENT_HUB'
    OPC_UA = 'OPC_UA'
    CUSTOM = 'CUSTOM'
    UDP = 'UDP'
    TCP = 'TCP'
    KAFKA = 'KAFKA'
    AZURE_IOT_HUB = 'AZURE_IOT_HUB'
    APACHE_PULSAR = 'APACHE_PULSAR'
    RABBITMQ = 'RABBITMQ'
    LORIOT = 'LORIOT'
    COAP = 'COAP'
    TUYA = 'TUYA'
    AZURE_SERVICE_BUS = 'AZURE_SERVICE_BUS'
    KPN = 'KPN'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IntegrationType from a JSON string"""
        return cls(json.loads(json_str))


