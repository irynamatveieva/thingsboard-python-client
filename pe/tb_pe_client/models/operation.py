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


class Operation(str, Enum):
    """
    Operation
    """

    """
    allowed enum values
    """
    ALL = 'ALL'
    CREATE = 'CREATE'
    READ = 'READ'
    WRITE = 'WRITE'
    DELETE = 'DELETE'
    RPC_CALL = 'RPC_CALL'
    READ_CREDENTIALS = 'READ_CREDENTIALS'
    WRITE_CREDENTIALS = 'WRITE_CREDENTIALS'
    READ_ATTRIBUTES = 'READ_ATTRIBUTES'
    WRITE_ATTRIBUTES = 'WRITE_ATTRIBUTES'
    READ_TELEMETRY = 'READ_TELEMETRY'
    WRITE_TELEMETRY = 'WRITE_TELEMETRY'
    ADD_TO_GROUP = 'ADD_TO_GROUP'
    REMOVE_FROM_GROUP = 'REMOVE_FROM_GROUP'
    CHANGE_OWNER = 'CHANGE_OWNER'
    IMPERSONATE = 'IMPERSONATE'
    CLAIM_DEVICES = 'CLAIM_DEVICES'
    SHARE_GROUP = 'SHARE_GROUP'
    ASSIGN_TO_TENANT = 'ASSIGN_TO_TENANT'
    READ_CALCULATED_FIELD = 'READ_CALCULATED_FIELD'
    WRITE_CALCULATED_FIELD = 'WRITE_CALCULATED_FIELD'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Operation from a JSON string"""
        return cls(json.loads(json_str))


