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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.captcha_params import CaptchaParams
from tb_paas_client.models.sign_up_field import SignUpField
from typing import Optional, Set
from typing_extensions import Self

class SignUpSelfRegistrationParams(BaseModel):
    """
    SignUpSelfRegistrationParams
    """ # noqa: E501
    title: Optional[StrictStr] = None
    captcha: Optional[CaptchaParams] = None
    fields: Optional[List[SignUpField]] = None
    show_privacy_policy: Optional[StrictBool] = Field(default=None, alias="showPrivacyPolicy")
    show_terms_of_use: Optional[StrictBool] = Field(default=None, alias="showTermsOfUse")
    __properties: ClassVar[List[str]] = ["title", "captcha", "fields", "showPrivacyPolicy", "showTermsOfUse"]

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
        """Create an instance of SignUpSelfRegistrationParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of captcha
        if self.captcha:
            _dict['captcha'] = self.captcha.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item_fields in self.fields:
                if _item_fields:
                    _items.append(_item_fields.to_dict())
            _dict['fields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SignUpSelfRegistrationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "captcha": CaptchaParams.from_dict(obj["captcha"]) if obj.get("captcha") is not None else None,
            "fields": [SignUpField.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
            "showPrivacyPolicy": obj.get("showPrivacyPolicy"),
            "showTermsOfUse": obj.get("showTermsOfUse")
        })
        return _obj


