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
from tb_paas_client.models.cf_argument_dynamic_source_configuration import CfArgumentDynamicSourceConfiguration
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.referenced_entity_key import ReferencedEntityKey
from typing import Optional, Set
from typing_extensions import Self

class Argument(BaseModel):
    """
    Argument
    """ # noqa: E501
    ref_entity_id: Optional[EntityId] = Field(default=None, alias="refEntityId")
    ref_dynamic_source_configuration: Optional[CfArgumentDynamicSourceConfiguration] = Field(default=None, alias="refDynamicSourceConfiguration")
    ref_entity_key: Optional[ReferencedEntityKey] = Field(default=None, alias="refEntityKey")
    default_value: Optional[StrictStr] = Field(default=None, alias="defaultValue")
    limit: Optional[StrictInt] = None
    time_window: Optional[StrictInt] = Field(default=None, alias="timeWindow")
    __properties: ClassVar[List[str]] = ["refEntityId", "refDynamicSourceConfiguration", "refEntityKey", "defaultValue", "limit", "timeWindow"]

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
        """Create an instance of Argument from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ref_entity_id
        if self.ref_entity_id:
            _dict['refEntityId'] = self.ref_entity_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ref_dynamic_source_configuration
        if self.ref_dynamic_source_configuration:
            _dict['refDynamicSourceConfiguration'] = self.ref_dynamic_source_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ref_entity_key
        if self.ref_entity_key:
            _dict['refEntityKey'] = self.ref_entity_key.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Argument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "refEntityId": EntityId.from_dict(obj["refEntityId"]) if obj.get("refEntityId") is not None else None,
            "refDynamicSourceConfiguration": CfArgumentDynamicSourceConfiguration.from_dict(obj["refDynamicSourceConfiguration"]) if obj.get("refDynamicSourceConfiguration") is not None else None,
            "refEntityKey": ReferencedEntityKey.from_dict(obj["refEntityKey"]) if obj.get("refEntityKey") is not None else None,
            "defaultValue": obj.get("defaultValue"),
            "limit": obj.get("limit"),
            "timeWindow": obj.get("timeWindow")
        })
        return _obj


