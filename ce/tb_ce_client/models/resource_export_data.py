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
from tb_ce_client.models.resource_sub_type import ResourceSubType
from tb_ce_client.models.resource_type import ResourceType
from typing import Optional, Set
from typing_extensions import Self

class ResourceExportData(BaseModel):
    """
    ResourceExportData
    """ # noqa: E501
    link: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    type: Optional[ResourceType] = None
    sub_type: Optional[ResourceSubType] = Field(default=None, alias="subType")
    resource_key: Optional[StrictStr] = Field(default=None, alias="resourceKey")
    file_name: Optional[StrictStr] = Field(default=None, alias="fileName")
    public_resource_key: Optional[StrictStr] = Field(default=None, alias="publicResourceKey")
    is_public: Optional[StrictBool] = Field(default=None, alias="isPublic")
    media_type: Optional[StrictStr] = Field(default=None, alias="mediaType")
    data: Optional[StrictStr] = None
    public: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["link", "title", "type", "subType", "resourceKey", "fileName", "publicResourceKey", "isPublic", "mediaType", "data", "public"]

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
        """Create an instance of ResourceExportData from a JSON string"""
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
        """Create an instance of ResourceExportData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "link": obj.get("link"),
            "title": obj.get("title"),
            "type": obj.get("type"),
            "subType": obj.get("subType"),
            "resourceKey": obj.get("resourceKey"),
            "fileName": obj.get("fileName"),
            "publicResourceKey": obj.get("publicResourceKey"),
            "isPublic": obj.get("isPublic"),
            "mediaType": obj.get("mediaType"),
            "data": obj.get("data"),
            "public": obj.get("public")
        })
        return _obj


