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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.customer_id import CustomerId
from tb_paas_client.models.domain_id import DomainId
from tb_paas_client.models.tenant_id import TenantId
from tb_paas_client.models.white_labeling_type import WhiteLabelingType
from typing import Optional, Set
from typing_extensions import Self

class WhiteLabeling(BaseModel):
    """
    WhiteLabeling
    """ # noqa: E501
    tenant_id: Optional[TenantId] = Field(default=None, alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, alias="customerId")
    type: Optional[WhiteLabelingType] = None
    settings: Optional[Any] = None
    legacy_domain: Optional[StrictStr] = Field(default=None, alias="legacyDomain")
    domain_id: Optional[DomainId] = Field(default=None, alias="domainId")
    __properties: ClassVar[List[str]] = ["tenantId", "customerId", "type", "settings", "legacyDomain", "domainId"]

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
        """Create an instance of WhiteLabeling from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "legacy_domain",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenantId'] = self.tenant_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_id
        if self.customer_id:
            _dict['customerId'] = self.customer_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_id
        if self.domain_id:
            _dict['domainId'] = self.domain_id.to_dict()
        # set to None if settings (nullable) is None
        # and model_fields_set contains the field
        if self.settings is None and "settings" in self.model_fields_set:
            _dict['settings'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WhiteLabeling from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customerId": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "type": obj.get("type"),
            "settings": obj.get("settings"),
            "legacyDomain": obj.get("legacyDomain"),
            "domainId": DomainId.from_dict(obj["domainId"]) if obj.get("domainId") is not None else None
        })
        return _obj


