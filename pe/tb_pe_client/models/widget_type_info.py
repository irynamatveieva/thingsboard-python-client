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
from tb_pe_client.models.tenant_id import TenantId
from tb_pe_client.models.widget_bundle_info import WidgetBundleInfo
from tb_pe_client.models.widget_type_id import WidgetTypeId
from typing import Optional, Set
from typing_extensions import Self

class WidgetTypeInfo(BaseModel):
    """
    WidgetTypeInfo
    """ # noqa: E501
    id: Optional[WidgetTypeId] = Field(default=None, description="JSON object with the Widget Type Id. Specify this field to update the Widget Type. Referencing non-existing Widget Type Id will cause error. Omit this field to create new Widget Type.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the Widget Type creation, in milliseconds", alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id.", alias="tenantId")
    fqn: Optional[StrictStr] = Field(default=None, description="Unique FQN that is used in dashboards as a reference widget type")
    name: Optional[StrictStr] = Field(default=None, description="Widget name used in search and UI")
    deprecated: Optional[StrictBool] = Field(default=None, description="Whether widget type is deprecated.")
    scada: Optional[StrictBool] = Field(default=None, description="Whether widget type is SCADA symbol.")
    version: Optional[StrictInt] = None
    image: Optional[StrictStr] = Field(default=None, description="Base64 encoded widget thumbnail")
    description: Optional[StrictStr] = Field(default=None, description="Description of the widget type")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Tags of the widget type")
    widget_type: Optional[StrictStr] = Field(default=None, description="Type of the widget (timeseries, latest, control, alarm or static)", alias="widgetType")
    bundles: Optional[List[WidgetBundleInfo]] = Field(default=None, description="Bundles")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "fqn", "name", "deprecated", "scada", "version", "image", "description", "tags", "widgetType", "bundles"]

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
        """Create an instance of WidgetTypeInfo from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "fqn",
            "name",
            "image",
            "description",
            "widget_type",
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
        # override the default output from pydantic by calling `to_dict()` of each item in bundles (list)
        _items = []
        if self.bundles:
            for _item_bundles in self.bundles:
                if _item_bundles:
                    _items.append(_item_bundles.to_dict())
            _dict['bundles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WidgetTypeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": WidgetTypeId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "fqn": obj.get("fqn"),
            "name": obj.get("name"),
            "deprecated": obj.get("deprecated"),
            "scada": obj.get("scada"),
            "version": obj.get("version"),
            "image": obj.get("image"),
            "description": obj.get("description"),
            "tags": obj.get("tags"),
            "widgetType": obj.get("widgetType"),
            "bundles": [WidgetBundleInfo.from_dict(_item) for _item in obj["bundles"]] if obj.get("bundles") is not None else None
        })
        return _obj


