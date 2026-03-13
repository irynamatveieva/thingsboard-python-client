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


class EdgeEventActionType(str, Enum):
    """
    EdgeEventActionType
    """

    """
    allowed enum values
    """
    ADDED = 'ADDED'
    UPDATED = 'UPDATED'
    DELETED = 'DELETED'
    POST_ATTRIBUTES = 'POST_ATTRIBUTES'
    ATTRIBUTES_UPDATED = 'ATTRIBUTES_UPDATED'
    ATTRIBUTES_DELETED = 'ATTRIBUTES_DELETED'
    TIMESERIES_UPDATED = 'TIMESERIES_UPDATED'
    CREDENTIALS_UPDATED = 'CREDENTIALS_UPDATED'
    ASSIGNED_TO_CUSTOMER = 'ASSIGNED_TO_CUSTOMER'
    UNASSIGNED_FROM_CUSTOMER = 'UNASSIGNED_FROM_CUSTOMER'
    RELATION_ADD_OR_UPDATE = 'RELATION_ADD_OR_UPDATE'
    RELATION_DELETED = 'RELATION_DELETED'
    RPC_CALL = 'RPC_CALL'
    ALARM_ACK = 'ALARM_ACK'
    ALARM_CLEAR = 'ALARM_CLEAR'
    ALARM_DELETE = 'ALARM_DELETE'
    ALARM_ASSIGNED = 'ALARM_ASSIGNED'
    ALARM_UNASSIGNED = 'ALARM_UNASSIGNED'
    ADDED_COMMENT = 'ADDED_COMMENT'
    UPDATED_COMMENT = 'UPDATED_COMMENT'
    DELETED_COMMENT = 'DELETED_COMMENT'
    ASSIGNED_TO_EDGE = 'ASSIGNED_TO_EDGE'
    UNASSIGNED_FROM_EDGE = 'UNASSIGNED_FROM_EDGE'
    CREDENTIALS_REQUEST = 'CREDENTIALS_REQUEST'
    ENTITY_MERGE_REQUEST = 'ENTITY_MERGE_REQUEST'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EdgeEventActionType from a JSON string"""
        return cls(json.loads(json_str))


