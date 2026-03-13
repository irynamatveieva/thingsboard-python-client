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


class ThingsboardErrorCode(int, Enum):
    """
    Platform error code
    """

    """
    allowed enum values
    """
    NUMBER_2 = 2
    NUMBER_10 = 10
    NUMBER_11 = 11
    NUMBER_15 = 15
    NUMBER_20 = 20
    NUMBER_30 = 30
    NUMBER_31 = 31
    NUMBER_32 = 32
    NUMBER_33 = 33
    NUMBER_34 = 34
    NUMBER_35 = 35
    NUMBER_40 = 40
    NUMBER_41 = 41
    NUMBER_45 = 45
    NUMBER_46 = 46

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ThingsboardErrorCode from a JSON string"""
        return cls(json.loads(json_str))


