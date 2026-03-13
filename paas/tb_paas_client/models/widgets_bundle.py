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
from tb_paas_client.models.tenant_id import TenantId
from tb_paas_client.models.widgets_bundle_id import WidgetsBundleId
from typing import Optional, Set
from typing_extensions import Self

class WidgetsBundle(BaseModel):
    """
    A JSON value representing the Widget Bundle.
    """ # noqa: E501
    id: Optional[WidgetsBundleId] = Field(default=None, description="JSON object with the Widget Bundle Id. Specify this field to update the Widget Bundle. Referencing non-existing Widget Bundle Id will cause error. Omit this field to create new Widget Bundle.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the Widget Bundle creation, in milliseconds", alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id.", alias="tenantId")
    alias: Optional[StrictStr] = Field(default=None, description="Unique alias that is used in widget types as a reference widget bundle")
    title: Optional[StrictStr] = Field(default=None, description="Title used in search and UI")
    image: Optional[StrictStr] = Field(default=None, description="Relative or external image URL. Replaced with image data URL (Base64) in case of relative URL and 'inlineImages' option enabled.")
    scada: Optional[StrictBool] = Field(default=None, description="Whether widgets bundle contains SCADA symbol widget types.")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    order: Optional[StrictInt] = Field(default=None, description="Order")
    version: Optional[StrictInt] = None
    name: Optional[StrictStr] = Field(default=None, description="Same as title of the Widget Bundle. Read-only field. Update the 'title' to change the 'name' of the Widget Bundle.")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "alias", "title", "image", "scada", "description", "order", "version", "name"]

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
        """Create an instance of WidgetsBundle from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "alias",
            "title",
            "image",
            "scada",
            "description",
            "order",
            "name",
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WidgetsBundle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": WidgetsBundleId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "alias": obj.get("alias"),
            "title": obj.get("title"),
            "image": obj.get("image"),
            "scada": obj.get("scada"),
            "description": obj.get("description"),
            "order": obj.get("order"),
            "version": obj.get("version"),
            "name": obj.get("name")
        })
        return _obj


