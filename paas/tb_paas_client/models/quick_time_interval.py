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


class QuickTimeInterval(str, Enum):
    """
    QuickTimeInterval
    """

    """
    allowed enum values
    """
    YESTERDAY = 'YESTERDAY'
    DAY_BEFORE_YESTERDAY = 'DAY_BEFORE_YESTERDAY'
    THIS_DAY_LAST_WEEK = 'THIS_DAY_LAST_WEEK'
    PREVIOUS_WEEK = 'PREVIOUS_WEEK'
    PREVIOUS_WEEK_ISO = 'PREVIOUS_WEEK_ISO'
    PREVIOUS_MONTH = 'PREVIOUS_MONTH'
    PREVIOUS_QUARTER = 'PREVIOUS_QUARTER'
    PREVIOUS_HALF_YEAR = 'PREVIOUS_HALF_YEAR'
    PREVIOUS_YEAR = 'PREVIOUS_YEAR'
    CURRENT_HOUR = 'CURRENT_HOUR'
    CURRENT_DAY = 'CURRENT_DAY'
    CURRENT_DAY_SO_FAR = 'CURRENT_DAY_SO_FAR'
    CURRENT_WEEK = 'CURRENT_WEEK'
    CURRENT_WEEK_ISO = 'CURRENT_WEEK_ISO'
    CURRENT_WEEK_SO_FAR = 'CURRENT_WEEK_SO_FAR'
    CURRENT_WEEK_ISO_SO_FAR = 'CURRENT_WEEK_ISO_SO_FAR'
    CURRENT_MONTH = 'CURRENT_MONTH'
    CURRENT_MONTH_SO_FAR = 'CURRENT_MONTH_SO_FAR'
    CURRENT_QUARTER = 'CURRENT_QUARTER'
    CURRENT_QUARTER_SO_FAR = 'CURRENT_QUARTER_SO_FAR'
    CURRENT_HALF_YEAR = 'CURRENT_HALF_YEAR'
    CURRENT_HALF_YEAR_SO_FAR = 'CURRENT_HALF_YEAR_SO_FAR'
    CURRENT_YEAR = 'CURRENT_YEAR'
    CURRENT_YEAR_SO_FAR = 'CURRENT_YEAR_SO_FAR'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of QuickTimeInterval from a JSON string"""
        return cls(json.loads(json_str))


