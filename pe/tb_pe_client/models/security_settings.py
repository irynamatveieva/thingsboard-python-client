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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tb_pe_client.models.user_password_policy import UserPasswordPolicy
from typing import Optional, Set
from typing_extensions import Self

class SecuritySettings(BaseModel):
    """
    A JSON value representing the Security Settings.
    """ # noqa: E501
    password_policy: Optional[UserPasswordPolicy] = Field(default=None, description="The user password policy object.", alias="passwordPolicy")
    max_failed_login_attempts: Optional[StrictInt] = Field(default=None, description="Maximum number of failed login attempts allowed before user account is locked.", alias="maxFailedLoginAttempts")
    user_lockout_notification_email: Optional[StrictStr] = Field(default=None, description="Email to use for notifications about locked users.", alias="userLockoutNotificationEmail")
    mobile_secret_key_length: Optional[StrictInt] = Field(default=None, description="Mobile secret key length", alias="mobileSecretKeyLength")
    user_activation_token_ttl: Annotated[int, Field(le=24, strict=True, ge=1)] = Field(description="TTL in hours for user activation link", alias="userActivationTokenTtl")
    password_reset_token_ttl: Annotated[int, Field(le=24, strict=True, ge=1)] = Field(description="TTL in hours for password reset link", alias="passwordResetTokenTtl")
    __properties: ClassVar[List[str]] = ["passwordPolicy", "maxFailedLoginAttempts", "userLockoutNotificationEmail", "mobileSecretKeyLength", "userActivationTokenTtl", "passwordResetTokenTtl"]

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
        """Create an instance of SecuritySettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of password_policy
        if self.password_policy:
            _dict['passwordPolicy'] = self.password_policy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SecuritySettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "passwordPolicy": UserPasswordPolicy.from_dict(obj["passwordPolicy"]) if obj.get("passwordPolicy") is not None else None,
            "maxFailedLoginAttempts": obj.get("maxFailedLoginAttempts"),
            "userLockoutNotificationEmail": obj.get("userLockoutNotificationEmail"),
            "mobileSecretKeyLength": obj.get("mobileSecretKeyLength"),
            "userActivationTokenTtl": obj.get("userActivationTokenTtl"),
            "passwordResetTokenTtl": obj.get("passwordResetTokenTtl")
        })
        return _obj


