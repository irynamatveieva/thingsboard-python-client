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
from tb_pe_client.models.tenant_name_strategy_type import TenantNameStrategyType
from typing import Optional, Set
from typing_extensions import Self

class OAuth2BasicMapperConfig(BaseModel):
    """
    OAuth2BasicMapperConfig
    """ # noqa: E501
    email_attribute_key: Optional[StrictStr] = Field(default=None, description="Email attribute key of OAuth2 principal attributes. Must be specified for BASIC mapper type and cannot be specified for GITHUB type", serialization_alias="emailAttributeKey")
    first_name_attribute_key: Optional[StrictStr] = Field(default=None, description="First name attribute key", serialization_alias="firstNameAttributeKey")
    last_name_attribute_key: Optional[StrictStr] = Field(default=None, description="Last name attribute key", serialization_alias="lastNameAttributeKey")
    tenant_name_strategy: TenantNameStrategyType = Field(description="Tenant naming strategy. For DOMAIN type, domain for tenant name will be taken from the email (substring before '@')", serialization_alias="tenantNameStrategy")
    tenant_name_pattern: Optional[StrictStr] = Field(default=None, description="Tenant name pattern for CUSTOM naming strategy. OAuth2 attributes in the pattern can be used by enclosing attribute key in '%{' and '}'", serialization_alias="tenantNamePattern")
    customer_name_pattern: Optional[StrictStr] = Field(default=None, description="Customer name pattern. When creating a user on the first OAuth2 log in, if specified, customer name will be used to create or find existing customer in the platform and assign customerId to the user", serialization_alias="customerNamePattern")
    default_dashboard_name: Optional[StrictStr] = Field(default=None, description="Name of the tenant's dashboard to set as default dashboard for newly created user", serialization_alias="defaultDashboardName")
    always_full_screen: Optional[StrictBool] = Field(default=None, description="Whether default dashboard should be open in full screen", serialization_alias="alwaysFullScreen")
    parent_customer_name_pattern: Optional[StrictStr] = Field(default=None, serialization_alias="parentCustomerNamePattern")
    user_groups_name_pattern: Optional[List[StrictStr]] = Field(default=None, serialization_alias="userGroupsNamePattern")
    __properties: ClassVar[List[str]] = ["emailAttributeKey", "firstNameAttributeKey", "lastNameAttributeKey", "tenantNameStrategy", "tenantNamePattern", "customerNamePattern", "defaultDashboardName", "alwaysFullScreen", "parentCustomerNamePattern", "userGroupsNamePattern"]

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
        """Create an instance of OAuth2BasicMapperConfig from a JSON string"""
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
        """Create an instance of OAuth2BasicMapperConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email_attribute_key": obj.get("emailAttributeKey"),
            "first_name_attribute_key": obj.get("firstNameAttributeKey"),
            "last_name_attribute_key": obj.get("lastNameAttributeKey"),
            "tenant_name_strategy": obj.get("tenantNameStrategy"),
            "tenant_name_pattern": obj.get("tenantNamePattern"),
            "customer_name_pattern": obj.get("customerNamePattern"),
            "default_dashboard_name": obj.get("defaultDashboardName"),
            "always_full_screen": obj.get("alwaysFullScreen"),
            "parent_customer_name_pattern": obj.get("parentCustomerNamePattern"),
            "user_groups_name_pattern": obj.get("userGroupsNamePattern")
        })
        return _obj


