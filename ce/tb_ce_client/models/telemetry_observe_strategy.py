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


class TelemetryObserveStrategy(str, Enum):
    """
    TelemetryObserveStrategy
    """

    """
    allowed enum values
    """
    SINGLE_LEFT_PARENTHESIS_0_RIGHT_PARENTHESIS_COLON__ONE_RESOURCE_EQUALS_ONE_SINGLE_OBSERVE_REQUEST = 'SINGLE (0): One resource equals one single observe request'
    COMPOSITE_ALL_LEFT_PARENTHESIS_1_RIGHT_PARENTHESIS_COLON__ALL_RESOURCES_IN_ONE_COMPOSITE_OBSERVE_REQUEST = 'COMPOSITE_ALL (1): All resources in one composite observe request'
    COMPOSITE_BY_OBJECT_LEFT_PARENTHESIS_2_RIGHT_PARENTHESIS_COLON__GROUPED_COMPOSITE_OBSERVE_REQUESTS_BY_OBJECT = 'COMPOSITE_BY_OBJECT (2): Grouped composite observe requests by object'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TelemetryObserveStrategy from a JSON string"""
        return cls(json.loads(json_str))


