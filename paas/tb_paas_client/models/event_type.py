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


class EventType(str, Enum):
    """
    EventType
    """

    """
    allowed enum values
    """
    ERROR = 'ERROR'
    LC_EVENT = 'LC_EVENT'
    STATS = 'STATS'
    RAW_DATA = 'RAW_DATA'
    DEBUG_RULE_NODE = 'DEBUG_RULE_NODE'
    DEBUG_RULE_CHAIN = 'DEBUG_RULE_CHAIN'
    DEBUG_CONVERTER = 'DEBUG_CONVERTER'
    DEBUG_INTEGRATION = 'DEBUG_INTEGRATION'
    DEBUG_CALCULATED_FIELD = 'DEBUG_CALCULATED_FIELD'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EventType from a JSON string"""
        return cls(json.loads(json_str))


