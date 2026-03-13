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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.blob_entity_id import BlobEntityId
from tb_paas_client.models.customer_id import CustomerId
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class BlobEntityWithCustomerInfo(BaseModel):
    """
    BlobEntityWithCustomerInfo
    """ # noqa: E501
    id: Optional[BlobEntityId] = Field(default=None, description="JSON object with the blob entity Id. Referencing non-existing blob entity Id will cause error")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the blob entity creation, in milliseconds", alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id", alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, description="JSON object with Customer Id", alias="customerId")
    name: Optional[StrictStr] = Field(default=None, description="blob entity name")
    type: Optional[StrictStr] = Field(default=None, description="blob entity type")
    content_type: Optional[StrictStr] = Field(default=None, description="blob content type", alias="contentType")
    customer_title: Optional[StrictStr] = Field(default=None, description="Title of the customer", alias="customerTitle")
    customer_is_public: Optional[StrictBool] = Field(default=None, description="Parameter that specifies if customer is public", alias="customerIsPublic")
    owner_id: Optional[EntityId] = Field(default=None, description="JSON object with Customer or Tenant Id", alias="ownerId")
    additional_info: Optional[Any] = Field(default=None, description="Additional parameters of the blob entity", alias="additionalInfo")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "customerId", "name", "type", "contentType", "customerTitle", "customerIsPublic", "ownerId", "additionalInfo"]

    @field_validator('content_type')
    def content_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['application/pdf', 'image/jpeg', 'image/png']):
            raise ValueError("must be one of enum values ('application/pdf', 'image/jpeg', 'image/png')")
        return value

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
        """Create an instance of BlobEntityWithCustomerInfo from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "customer_id",
            "name",
            "type",
            "content_type",
            "customer_is_public",
            "owner_id",
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
        # override the default output from pydantic by calling `to_dict()` of customer_id
        if self.customer_id:
            _dict['customerId'] = self.customer_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner_id
        if self.owner_id:
            _dict['ownerId'] = self.owner_id.to_dict()
        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BlobEntityWithCustomerInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": BlobEntityId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customerId": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "name": obj.get("name"),
            "type": obj.get("type"),
            "contentType": obj.get("contentType"),
            "customerTitle": obj.get("customerTitle"),
            "customerIsPublic": obj.get("customerIsPublic"),
            "ownerId": EntityId.from_dict(obj["ownerId"]) if obj.get("ownerId") is not None else None,
            "additionalInfo": obj.get("additionalInfo")
        })
        return _obj


