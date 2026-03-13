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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.mapper_type import MapperType
from tb_ce_client.models.o_auth2_basic_mapper_config import OAuth2BasicMapperConfig
from tb_ce_client.models.o_auth2_custom_mapper_config import OAuth2CustomMapperConfig
from typing import Optional, Set
from typing_extensions import Self

class OAuth2MapperConfig(BaseModel):
    """
    OAuth2MapperConfig
    """ # noqa: E501
    allow_user_creation: Optional[StrictBool] = Field(default=None, description="Whether user should be created if not yet present on the platform after successful authentication", alias="allowUserCreation")
    activate_user: Optional[StrictBool] = Field(default=None, description="Whether user credentials should be activated when user is created after successful authentication", alias="activateUser")
    type: MapperType = Field(description="Type of OAuth2 mapper. Depending on this param, different mapper config fields must be specified")
    basic: Optional[OAuth2BasicMapperConfig] = Field(default=None, description="Mapper config for BASIC and GITHUB mapper types")
    custom: Optional[OAuth2CustomMapperConfig] = Field(default=None, description="Mapper config for CUSTOM mapper type")
    __properties: ClassVar[List[str]] = ["allowUserCreation", "activateUser", "type", "basic", "custom"]

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
        """Create an instance of OAuth2MapperConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of basic
        if self.basic:
            _dict['basic'] = self.basic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom
        if self.custom:
            _dict['custom'] = self.custom.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OAuth2MapperConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowUserCreation": obj.get("allowUserCreation"),
            "activateUser": obj.get("activateUser"),
            "type": obj.get("type"),
            "basic": OAuth2BasicMapperConfig.from_dict(obj["basic"]) if obj.get("basic") is not None else None,
            "custom": OAuth2CustomMapperConfig.from_dict(obj["custom"]) if obj.get("custom") is not None else None
        })
        return _obj


