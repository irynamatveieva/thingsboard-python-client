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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.resource_sub_type import ResourceSubType
from tb_pe_client.models.resource_type import ResourceType
from typing import Optional, Set
from typing_extensions import Self

class ResourceExportData(BaseModel):
    """
    ResourceExportData
    """ # noqa: E501
    link: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    type: Optional[ResourceType] = None
    sub_type: Optional[ResourceSubType] = Field(default=None, serialization_alias="subType")
    resource_key: Optional[StrictStr] = Field(default=None, serialization_alias="resourceKey")
    file_name: Optional[StrictStr] = Field(default=None, serialization_alias="fileName")
    public_resource_key: Optional[StrictStr] = Field(default=None, serialization_alias="publicResourceKey")
    media_type: Optional[StrictStr] = Field(default=None, serialization_alias="mediaType")
    data: Optional[StrictStr] = None
    is_public: Optional[StrictBool] = Field(default=None, serialization_alias="isPublic")
    public: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["link", "title", "type", "subType", "resourceKey", "fileName", "publicResourceKey", "mediaType", "data", "isPublic", "public"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.model_dump(by_alias=False, mode='json'))

    def __str__(self) -> str:
        return self.to_str()

    def __repr__(self) -> str:
        return self.to_str()

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

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
            "sub_type": obj.get("subType"),
            "resource_key": obj.get("resourceKey"),
            "file_name": obj.get("fileName"),
            "public_resource_key": obj.get("publicResourceKey"),
            "media_type": obj.get("mediaType"),
            "data": obj.get("data"),
            "is_public": obj.get("isPublic"),
            "public": obj.get("public")
        })
        return _obj


