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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UserPasswordPolicy(BaseModel):
    """
    UserPasswordPolicy
    """ # noqa: E501
    minimum_length: Optional[StrictInt] = Field(default=None, description="Minimum number of symbols in the password.", alias="minimumLength")
    maximum_length: Optional[StrictInt] = Field(default=None, description="Maximum number of symbols in the password.", alias="maximumLength")
    minimum_uppercase_letters: Optional[StrictInt] = Field(default=None, description="Minimum number of uppercase letters in the password.", alias="minimumUppercaseLetters")
    minimum_lowercase_letters: Optional[StrictInt] = Field(default=None, description="Minimum number of lowercase letters in the password.", alias="minimumLowercaseLetters")
    minimum_digits: Optional[StrictInt] = Field(default=None, description="Minimum number of digits in the password.", alias="minimumDigits")
    minimum_special_characters: Optional[StrictInt] = Field(default=None, description="Minimum number of special in the password.", alias="minimumSpecialCharacters")
    allow_whitespaces: Optional[StrictBool] = Field(default=None, description="Allow whitespaces", alias="allowWhitespaces")
    force_user_to_reset_password_if_not_valid: Optional[StrictBool] = Field(default=None, description="Force user to update password if existing one does not pass validation", alias="forceUserToResetPasswordIfNotValid")
    password_expiration_period_days: Optional[StrictInt] = Field(default=None, description="Password expiration period (days). Force expiration of the password.", alias="passwordExpirationPeriodDays")
    password_reuse_frequency_days: Optional[StrictInt] = Field(default=None, description="Password reuse frequency (days). Disallow to use the same password for the defined number of days", alias="passwordReuseFrequencyDays")
    __properties: ClassVar[List[str]] = ["minimumLength", "maximumLength", "minimumUppercaseLetters", "minimumLowercaseLetters", "minimumDigits", "minimumSpecialCharacters", "allowWhitespaces", "forceUserToResetPasswordIfNotValid", "passwordExpirationPeriodDays", "passwordReuseFrequencyDays"]

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
        """Create an instance of UserPasswordPolicy from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserPasswordPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "minimumLength": obj.get("minimumLength"),
            "maximumLength": obj.get("maximumLength"),
            "minimumUppercaseLetters": obj.get("minimumUppercaseLetters"),
            "minimumLowercaseLetters": obj.get("minimumLowercaseLetters"),
            "minimumDigits": obj.get("minimumDigits"),
            "minimumSpecialCharacters": obj.get("minimumSpecialCharacters"),
            "allowWhitespaces": obj.get("allowWhitespaces"),
            "forceUserToResetPasswordIfNotValid": obj.get("forceUserToResetPasswordIfNotValid"),
            "passwordExpirationPeriodDays": obj.get("passwordExpirationPeriodDays"),
            "passwordReuseFrequencyDays": obj.get("passwordReuseFrequencyDays")
        })
        return _obj


