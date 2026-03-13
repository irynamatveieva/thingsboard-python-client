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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tb_ce_client.models.two_fa_provider_config import TwoFaProviderConfig
from typing import Optional, Set
from typing_extensions import Self

class PlatformTwoFaSettings(BaseModel):
    """
    Settings value
    """ # noqa: E501
    providers: List[TwoFaProviderConfig]
    min_verification_code_send_period: Annotated[int, Field(strict=True, ge=5)] = Field(alias="minVerificationCodeSendPeriod")
    verification_code_check_rate_limit: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="verificationCodeCheckRateLimit")
    max_verification_failures_before_user_lockout: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="maxVerificationFailuresBeforeUserLockout")
    total_allowed_time_for_verification: Annotated[int, Field(strict=True, ge=60)] = Field(alias="totalAllowedTimeForVerification")
    enforce_two_fa: Optional[StrictBool] = Field(default=None, alias="enforceTwoFa")
    enforced_users_filter: Optional[Any] = Field(default=None, alias="enforcedUsersFilter")
    __properties: ClassVar[List[str]] = ["providers", "minVerificationCodeSendPeriod", "verificationCodeCheckRateLimit", "maxVerificationFailuresBeforeUserLockout", "totalAllowedTimeForVerification", "enforceTwoFa", "enforcedUsersFilter"]

    @field_validator('verification_code_check_rate_limit')
    def verification_code_check_rate_limit_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[1-9]\d*:[1-9]\d*", value):
            raise ValueError(r"must validate the regular expression /[1-9]\d*:[1-9]\d*/")
        return value

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
        """Create an instance of PlatformTwoFaSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in providers (list)
        _items = []
        if self.providers:
            for _item_providers in self.providers:
                if _item_providers:
                    _items.append(_item_providers.to_dict())
            _dict['providers'] = _items
        # set to None if enforced_users_filter (nullable) is None
        # and model_fields_set contains the field
        if self.enforced_users_filter is None and "enforced_users_filter" in self.model_fields_set:
            _dict['enforcedUsersFilter'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlatformTwoFaSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "providers": [TwoFaProviderConfig.from_dict(_item) for _item in obj["providers"]] if obj.get("providers") is not None else None,
            "minVerificationCodeSendPeriod": obj.get("minVerificationCodeSendPeriod"),
            "verificationCodeCheckRateLimit": obj.get("verificationCodeCheckRateLimit"),
            "maxVerificationFailuresBeforeUserLockout": obj.get("maxVerificationFailuresBeforeUserLockout"),
            "totalAllowedTimeForVerification": obj.get("totalAllowedTimeForVerification"),
            "enforceTwoFa": obj.get("enforceTwoFa"),
            "enforcedUsersFilter": obj.get("enforcedUsersFilter")
        })
        return _obj


