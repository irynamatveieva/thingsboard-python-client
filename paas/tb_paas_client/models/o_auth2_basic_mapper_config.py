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
from tb_paas_client.models.tenant_name_strategy_type import TenantNameStrategyType
from typing import Optional, Set
from typing_extensions import Self

class OAuth2BasicMapperConfig(BaseModel):
    """
    OAuth2BasicMapperConfig
    """ # noqa: E501
    email_attribute_key: Optional[StrictStr] = Field(default=None, description="Email attribute key of OAuth2 principal attributes. Must be specified for BASIC mapper type and cannot be specified for GITHUB type", alias="emailAttributeKey")
    first_name_attribute_key: Optional[StrictStr] = Field(default=None, description="First name attribute key", alias="firstNameAttributeKey")
    last_name_attribute_key: Optional[StrictStr] = Field(default=None, description="Last name attribute key", alias="lastNameAttributeKey")
    tenant_name_strategy: TenantNameStrategyType = Field(description="Tenant naming strategy. For DOMAIN type, domain for tenant name will be taken from the email (substring before '@')", alias="tenantNameStrategy")
    tenant_name_pattern: Optional[StrictStr] = Field(default=None, description="Tenant name pattern for CUSTOM naming strategy. OAuth2 attributes in the pattern can be used by enclosing attribute key in '%{' and '}'", alias="tenantNamePattern")
    customer_name_pattern: Optional[StrictStr] = Field(default=None, description="Customer name pattern. When creating a user on the first OAuth2 log in, if specified, customer name will be used to create or find existing customer in the platform and assign customerId to the user", alias="customerNamePattern")
    default_dashboard_name: Optional[StrictStr] = Field(default=None, description="Name of the tenant's dashboard to set as default dashboard for newly created user", alias="defaultDashboardName")
    always_full_screen: Optional[StrictBool] = Field(default=None, description="Whether default dashboard should be open in full screen", alias="alwaysFullScreen")
    parent_customer_name_pattern: Optional[StrictStr] = Field(default=None, alias="parentCustomerNamePattern")
    user_groups_name_pattern: Optional[List[StrictStr]] = Field(default=None, alias="userGroupsNamePattern")
    __properties: ClassVar[List[str]] = ["emailAttributeKey", "firstNameAttributeKey", "lastNameAttributeKey", "tenantNameStrategy", "tenantNamePattern", "customerNamePattern", "defaultDashboardName", "alwaysFullScreen", "parentCustomerNamePattern", "userGroupsNamePattern"]

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
            "emailAttributeKey": obj.get("emailAttributeKey"),
            "firstNameAttributeKey": obj.get("firstNameAttributeKey"),
            "lastNameAttributeKey": obj.get("lastNameAttributeKey"),
            "tenantNameStrategy": obj.get("tenantNameStrategy"),
            "tenantNamePattern": obj.get("tenantNamePattern"),
            "customerNamePattern": obj.get("customerNamePattern"),
            "defaultDashboardName": obj.get("defaultDashboardName"),
            "alwaysFullScreen": obj.get("alwaysFullScreen"),
            "parentCustomerNamePattern": obj.get("parentCustomerNamePattern"),
            "userGroupsNamePattern": obj.get("userGroupsNamePattern")
        })
        return _obj


