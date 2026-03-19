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

from pydantic import ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from tb_pe_client.models.two_fa_account_config import TwoFaAccountConfig
from typing import Optional, Set
from typing_extensions import Self

class SmsTwoFaAccountConfig(TwoFaAccountConfig):
    """
    SmsTwoFaAccountConfig
    """ # noqa: E501
    phone_number: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="phoneNumber")
    __properties: ClassVar[List[str]] = ["useByDefault", "providerType", "phoneNumber"]

    @field_validator('phone_number')
    def phone_number_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\+[1-9]\d{1,14}$", value):
            raise ValueError(r"must validate the regular expression /^\+[1-9]\d{1,14}$/")
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
        """Create an instance of SmsTwoFaAccountConfig from a JSON string"""
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
        """Create an instance of SmsTwoFaAccountConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "useByDefault": obj.get("useByDefault"),
            "providerType": obj.get("providerType"),
            "phoneNumber": obj.get("phoneNumber")
        })
        return _obj


