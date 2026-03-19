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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.sms_provider_configuration import SmsProviderConfiguration
from typing import Optional, Set
from typing_extensions import Self

class TestSmsRequest(BaseModel):
    """
    A JSON value representing the Test SMS request.
    """ # noqa: E501
    provider_configuration: Optional[SmsProviderConfiguration] = Field(default=None, description="The SMS provider configuration", alias="providerConfiguration")
    number_to: Optional[StrictStr] = Field(default=None, description="The phone number or other identifier to specify as a recipient of the SMS.", alias="numberTo")
    message: Optional[StrictStr] = Field(default=None, description="The test message")
    __properties: ClassVar[List[str]] = ["providerConfiguration", "numberTo", "message"]

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
        """Create an instance of TestSmsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of provider_configuration
        if self.provider_configuration:
            _dict['providerConfiguration'] = self.provider_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestSmsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "providerConfiguration": SmsProviderConfiguration.from_dict(obj["providerConfiguration"]) if obj.get("providerConfiguration") is not None else None,
            "numberTo": obj.get("numberTo"),
            "message": obj.get("message")
        })
        return _obj


