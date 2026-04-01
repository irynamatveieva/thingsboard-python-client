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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.resource_sub_type import ResourceSubType
from tb_ce_client.models.resource_type import ResourceType
from tb_ce_client.models.tb_resource_id import TbResourceId
from tb_ce_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class TbResource(BaseModel):
    """
    A JSON value representing the Resource.
    """ # noqa: E501
    id: Optional[TbResourceId] = Field(default=None, description="JSON object with the Resource Id. Specify this field to update the Resource. Referencing non-existing Resource Id will cause error. Omit this field to create new Resource.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the resource creation, in milliseconds", serialization_alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id. Tenant Id of the resource can't be changed.", serialization_alias="tenantId")
    title: Optional[StrictStr] = Field(default=None, description="Resource title.")
    resource_type: Optional[ResourceType] = Field(default=None, description="Resource type.", serialization_alias="resourceType")
    resource_sub_type: Optional[ResourceSubType] = Field(default=None, description="Resource sub type.", serialization_alias="resourceSubType")
    resource_key: Optional[StrictStr] = Field(default=None, description="Resource key.", serialization_alias="resourceKey")
    public_resource_key: Optional[StrictStr] = Field(default=None, description="Public resource key.", serialization_alias="publicResourceKey")
    etag: Optional[StrictStr] = Field(default=None, description="Resource etag.")
    file_name: Optional[StrictStr] = Field(default=None, description="Resource file name.", serialization_alias="fileName")
    descriptor: Optional[Any] = Field(default=None, description="Resource descriptor.")
    data: Optional[StrictStr] = Field(default=None, description="Resource data.")
    preview: Optional[StrictStr] = None
    link: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    public: Optional[StrictBool] = None
    public_link: Optional[StrictStr] = Field(default=None, serialization_alias="publicLink")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "title", "resourceType", "resourceSubType", "resourceKey", "publicResourceKey", "etag", "fileName", "descriptor", "data", "preview", "link", "name", "public", "publicLink"]

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
        """Create an instance of TbResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "etag",
            "link",
            "name",
            "public_link",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenantId'] = self.tenant_id.to_dict()
        # set to None if descriptor (nullable) is None
        # and model_fields_set contains the field
        if self.descriptor is None and "descriptor" in self.model_fields_set:
            _dict['descriptor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TbResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": TbResourceId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "title": obj.get("title"),
            "resource_type": obj.get("resourceType"),
            "resource_sub_type": obj.get("resourceSubType"),
            "resource_key": obj.get("resourceKey"),
            "public_resource_key": obj.get("publicResourceKey"),
            "etag": obj.get("etag"),
            "file_name": obj.get("fileName"),
            "descriptor": obj.get("descriptor"),
            "data": obj.get("data"),
            "preview": obj.get("preview"),
            "link": obj.get("link"),
            "name": obj.get("name"),
            "public": obj.get("public"),
            "public_link": obj.get("publicLink")
        })
        return _obj


