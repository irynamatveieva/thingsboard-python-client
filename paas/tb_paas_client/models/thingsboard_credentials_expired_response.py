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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.subscription_entry import SubscriptionEntry
from tb_paas_client.models.subscription_exception_error_code import SubscriptionExceptionErrorCode
from tb_paas_client.models.thingsboard_error_code import ThingsboardErrorCode
from typing import Optional, Set
from typing_extensions import Self

class ThingsboardCredentialsExpiredResponse(BaseModel):
    """
    ThingsboardCredentialsExpiredResponse
    """ # noqa: E501
    status: Optional[StrictInt] = Field(default=None, description="HTTP Response Status Code")
    message: Optional[StrictStr] = Field(default=None, description="Error message")
    error_code: Optional[ThingsboardErrorCode] = Field(default=None, alias="errorCode")
    timestamp: Optional[StrictInt] = Field(default=None, description="Timestamp")
    subscription_error_code: Optional[SubscriptionExceptionErrorCode] = Field(default=None, alias="subscriptionErrorCode")
    subscription_entry: Optional[SubscriptionEntry] = Field(default=None, alias="subscriptionEntry")
    subscription_value: Optional[Any] = Field(default=None, alias="subscriptionValue")
    reset_token: Optional[StrictStr] = Field(default=None, description="Password reset token", alias="resetToken")
    __properties: ClassVar[List[str]] = ["status", "message", "errorCode", "timestamp", "subscriptionErrorCode", "subscriptionEntry", "subscriptionValue", "resetToken"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ThingsboardCredentialsExpiredResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "status",
            "message",
            "timestamp",
            "reset_token",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if subscription_value (nullable) is None
        # and model_fields_set contains the field
        if self.subscription_value is None and "subscription_value" in self.model_fields_set:
            _dict['subscriptionValue'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ThingsboardCredentialsExpiredResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "message": obj.get("message"),
            "errorCode": obj.get("errorCode"),
            "timestamp": obj.get("timestamp"),
            "subscriptionErrorCode": obj.get("subscriptionErrorCode"),
            "subscriptionEntry": obj.get("subscriptionEntry"),
            "subscriptionValue": obj.get("subscriptionValue"),
            "resetToken": obj.get("resetToken")
        })
        return _obj


