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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from tb_pe_client.models.notification_delivery_method_config import NotificationDeliveryMethodConfig
from typing import Optional, Set
from typing_extensions import Self

class NotificationSettings(BaseModel):
    """
    NotificationSettings
    """ # noqa: E501
    delivery_methods_configs: Dict[str, NotificationDeliveryMethodConfig] = Field(alias="deliveryMethodsConfigs")
    __properties: ClassVar[List[str]] = ["deliveryMethodsConfigs"]

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
        """Create an instance of NotificationSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in delivery_methods_configs (dict)
        _field_dict = {}
        if self.delivery_methods_configs:
            for _key_delivery_methods_configs in self.delivery_methods_configs:
                if self.delivery_methods_configs[_key_delivery_methods_configs]:
                    _field_dict[_key_delivery_methods_configs] = self.delivery_methods_configs[_key_delivery_methods_configs].to_dict()
            _dict['deliveryMethodsConfigs'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deliveryMethodsConfigs": dict(
                (_k, NotificationDeliveryMethodConfig.from_dict(_v))
                for _k, _v in obj["deliveryMethodsConfigs"].items()
            )
            if obj.get("deliveryMethodsConfigs") is not None
            else None
        })
        return _obj


