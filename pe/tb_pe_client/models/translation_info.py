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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TranslationInfo(BaseModel):
    """
    TranslationInfo
    """ # noqa: E501
    locale_code: Optional[StrictStr] = Field(default=None, description="Locale code formed by combining the ISO 639-1 language code and the ISO 3166-1 region code. For example, \"en_US\"", alias="localeCode")
    language: Optional[StrictStr] = Field(default=None, description="Locale code language display name. For example, \"Polish (Polski)\"")
    country: Optional[StrictStr] = Field(default=None, description="Locale code country display name. For example, \"Poland\"")
    progress: Optional[StrictInt] = Field(default=None, description="Number representing translation percentage progress. For example, 40 that means 40% of all keys are translated.")
    customized: Optional[StrictBool] = Field(default=None, description="Boolean representing if current language has customization.")
    __properties: ClassVar[List[str]] = ["localeCode", "language", "country", "progress", "customized"]

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
        """Create an instance of TranslationInfo from a JSON string"""
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
        """Create an instance of TranslationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "localeCode": obj.get("localeCode"),
            "language": obj.get("language"),
            "country": obj.get("country"),
            "progress": obj.get("progress"),
            "customized": obj.get("customized")
        })
        return _obj


