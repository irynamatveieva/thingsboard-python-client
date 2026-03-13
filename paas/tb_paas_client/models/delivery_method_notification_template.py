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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_paas_client.models.email_delivery_method_notification_template import EmailDeliveryMethodNotificationTemplate
    from tb_paas_client.models.microsoft_teams_delivery_method_notification_template import MicrosoftTeamsDeliveryMethodNotificationTemplate
    from tb_paas_client.models.mobile_app_delivery_method_notification_template import MobileAppDeliveryMethodNotificationTemplate
    from tb_paas_client.models.slack_delivery_method_notification_template import SlackDeliveryMethodNotificationTemplate
    from tb_paas_client.models.sms_delivery_method_notification_template import SmsDeliveryMethodNotificationTemplate
    from tb_paas_client.models.web_delivery_method_notification_template import WebDeliveryMethodNotificationTemplate

class DeliveryMethodNotificationTemplate(BaseModel):
    """
    Base template for different delivery methods
    """ # noqa: E501
    enabled: Optional[StrictBool] = None
    body: Annotated[str, Field(min_length=1, strict=True)]
    method: StrictStr
    __properties: ClassVar[List[str]] = ["enabled", "body", "method"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'method'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'EMAIL': 'EmailDeliveryMethodNotificationTemplate','MICROSOFT_TEAMS': 'MicrosoftTeamsDeliveryMethodNotificationTemplate','MOBILE_APP': 'MobileAppDeliveryMethodNotificationTemplate','SLACK': 'SlackDeliveryMethodNotificationTemplate','SMS': 'SmsDeliveryMethodNotificationTemplate','WEB': 'WebDeliveryMethodNotificationTemplate'
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
    def from_json(cls, json_str: str) -> Optional[Union[EmailDeliveryMethodNotificationTemplate, MicrosoftTeamsDeliveryMethodNotificationTemplate, MobileAppDeliveryMethodNotificationTemplate, SlackDeliveryMethodNotificationTemplate, SmsDeliveryMethodNotificationTemplate, WebDeliveryMethodNotificationTemplate]]:
        """Create an instance of DeliveryMethodNotificationTemplate from a JSON string"""
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
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[EmailDeliveryMethodNotificationTemplate, MicrosoftTeamsDeliveryMethodNotificationTemplate, MobileAppDeliveryMethodNotificationTemplate, SlackDeliveryMethodNotificationTemplate, SmsDeliveryMethodNotificationTemplate, WebDeliveryMethodNotificationTemplate]]:
        """Create an instance of DeliveryMethodNotificationTemplate from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'EmailDeliveryMethodNotificationTemplate':
            return import_module("tb_paas_client.models.email_delivery_method_notification_template").EmailDeliveryMethodNotificationTemplate.from_dict(obj)
        if object_type ==  'MicrosoftTeamsDeliveryMethodNotificationTemplate':
            return import_module("tb_paas_client.models.microsoft_teams_delivery_method_notification_template").MicrosoftTeamsDeliveryMethodNotificationTemplate.from_dict(obj)
        if object_type ==  'MobileAppDeliveryMethodNotificationTemplate':
            return import_module("tb_paas_client.models.mobile_app_delivery_method_notification_template").MobileAppDeliveryMethodNotificationTemplate.from_dict(obj)
        if object_type ==  'SlackDeliveryMethodNotificationTemplate':
            return import_module("tb_paas_client.models.slack_delivery_method_notification_template").SlackDeliveryMethodNotificationTemplate.from_dict(obj)
        if object_type ==  'SmsDeliveryMethodNotificationTemplate':
            return import_module("tb_paas_client.models.sms_delivery_method_notification_template").SmsDeliveryMethodNotificationTemplate.from_dict(obj)
        if object_type ==  'WebDeliveryMethodNotificationTemplate':
            return import_module("tb_paas_client.models.web_delivery_method_notification_template").WebDeliveryMethodNotificationTemplate.from_dict(obj)

        raise ValueError("DeliveryMethodNotificationTemplate failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


