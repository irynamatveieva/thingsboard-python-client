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

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_paas_client.models.captcha_params import CaptchaParams
from tb_paas_client.models.custom_menu_id import CustomMenuId
from tb_paas_client.models.default_dashboard_params import DefaultDashboardParams
from tb_paas_client.models.entity_group_id import EntityGroupId
from tb_paas_client.models.group_permission import GroupPermission
from tb_paas_client.models.home_dashboard_params import HomeDashboardParams
from tb_paas_client.models.notification_target_id import NotificationTargetId
from tb_paas_client.models.self_registration_type import SelfRegistrationType
from tb_paas_client.models.sign_up_field import SignUpField
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_paas_client.models.mobile_self_registration_params import MobileSelfRegistrationParams
    from tb_paas_client.models.web_self_registration_params import WebSelfRegistrationParams

class SelfRegistrationParams(BaseModel):
    """
    SelfRegistrationParams
    """ # noqa: E501
    type: SelfRegistrationType
    enabled: Optional[StrictBool] = None
    title: Optional[StrictStr] = None
    captcha: Optional[CaptchaParams] = None
    permissions: Optional[List[GroupPermission]] = None
    notification_recipient: Optional[NotificationTargetId] = Field(default=None, alias="notificationRecipient")
    sign_up_fields: Optional[List[SignUpField]] = Field(default=None, alias="signUpFields")
    customer_title_prefix: Optional[StrictStr] = Field(default=None, alias="customerTitlePrefix")
    show_privacy_policy: Optional[StrictBool] = Field(default=None, alias="showPrivacyPolicy")
    show_terms_of_use: Optional[StrictBool] = Field(default=None, alias="showTermsOfUse")
    default_dashboard: Optional[DefaultDashboardParams] = Field(default=None, alias="defaultDashboard")
    home_dashboard: Optional[HomeDashboardParams] = Field(default=None, alias="homeDashboard")
    customer_group_id: Optional[EntityGroupId] = Field(default=None, alias="customerGroupId")
    custom_menu_id: Optional[CustomMenuId] = Field(default=None, alias="customMenuId")
    __properties: ClassVar[List[str]] = ["type", "enabled", "title", "captcha", "permissions", "notificationRecipient", "signUpFields", "customerTitlePrefix", "showPrivacyPolicy", "showTermsOfUse", "defaultDashboard", "homeDashboard", "customerGroupId", "customMenuId"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'MOBILE': 'MobileSelfRegistrationParams','WEB': 'WebSelfRegistrationParams'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[MobileSelfRegistrationParams, WebSelfRegistrationParams]]:
        """Create an instance of SelfRegistrationParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of captcha
        if self.captcha:
            _dict['captcha'] = self.captcha.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item_permissions in self.permissions:
                if _item_permissions:
                    _items.append(_item_permissions.to_dict())
            _dict['permissions'] = _items
        # override the default output from pydantic by calling `to_dict()` of notification_recipient
        if self.notification_recipient:
            _dict['notificationRecipient'] = self.notification_recipient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sign_up_fields (list)
        _items = []
        if self.sign_up_fields:
            for _item_sign_up_fields in self.sign_up_fields:
                if _item_sign_up_fields:
                    _items.append(_item_sign_up_fields.to_dict())
            _dict['signUpFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of default_dashboard
        if self.default_dashboard:
            _dict['defaultDashboard'] = self.default_dashboard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of home_dashboard
        if self.home_dashboard:
            _dict['homeDashboard'] = self.home_dashboard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_group_id
        if self.customer_group_id:
            _dict['customerGroupId'] = self.customer_group_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_menu_id
        if self.custom_menu_id:
            _dict['customMenuId'] = self.custom_menu_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[MobileSelfRegistrationParams, WebSelfRegistrationParams]]:
        """Create an instance of SelfRegistrationParams from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'MobileSelfRegistrationParams':
            return import_module("tb_paas_client.models.mobile_self_registration_params").MobileSelfRegistrationParams.from_dict(obj)
        if object_type ==  'WebSelfRegistrationParams':
            return import_module("tb_paas_client.models.web_self_registration_params").WebSelfRegistrationParams.from_dict(obj)

        raise ValueError("SelfRegistrationParams failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


