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


class Authority(str, Enum):
    """
    Authority
    """

    """
    allowed enum values
    """
    SYS_ADMIN = 'SYS_ADMIN'
    TENANT_ADMIN = 'TENANT_ADMIN'
    CUSTOMER_USER = 'CUSTOMER_USER'
    BILLING_ADMIN = 'BILLING_ADMIN'
    BILLING_SERVICE = 'BILLING_SERVICE'
    REFRESH_TOKEN = 'REFRESH_TOKEN'
    PRE_VERIFICATION_TOKEN = 'PRE_VERIFICATION_TOKEN'
    MFA_CONFIGURATION_TOKEN = 'MFA_CONFIGURATION_TOKEN'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Authority from a JSON string"""
        return cls(json.loads(json_str))


