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
from tb_pe_client.models.delivery_method_notification_template import DeliveryMethodNotificationTemplate
from tb_pe_client.models.report_template_id import ReportTemplateId
from tb_pe_client.models.user_id import UserId
from typing import Optional, Set
from typing_extensions import Self

class NotificationTemplateConfig(BaseModel):
    """
    NotificationTemplateConfig
    """ # noqa: E501
    delivery_methods_templates: Dict[str, DeliveryMethodNotificationTemplate] = Field(alias="deliveryMethodsTemplates")
    attach_report: Optional[StrictBool] = Field(default=None, alias="attachReport")
    report_template_id: Optional[ReportTemplateId] = Field(default=None, alias="reportTemplateId")
    user_id: Optional[UserId] = Field(default=None, alias="userId")
    timezone: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["deliveryMethodsTemplates", "attachReport", "reportTemplateId", "userId", "timezone"]

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
        """Create an instance of NotificationTemplateConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in delivery_methods_templates (dict)
        _field_dict = {}
        if self.delivery_methods_templates:
            for _key_delivery_methods_templates in self.delivery_methods_templates:
                if self.delivery_methods_templates[_key_delivery_methods_templates]:
                    _field_dict[_key_delivery_methods_templates] = self.delivery_methods_templates[_key_delivery_methods_templates].to_dict()
            _dict['deliveryMethodsTemplates'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of report_template_id
        if self.report_template_id:
            _dict['reportTemplateId'] = self.report_template_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_id
        if self.user_id:
            _dict['userId'] = self.user_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationTemplateConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deliveryMethodsTemplates": dict(
                (_k, DeliveryMethodNotificationTemplate.from_dict(_v))
                for _k, _v in obj["deliveryMethodsTemplates"].items()
            )
            if obj.get("deliveryMethodsTemplates") is not None
            else None,
            "attachReport": obj.get("attachReport"),
            "reportTemplateId": ReportTemplateId.from_dict(obj["reportTemplateId"]) if obj.get("reportTemplateId") is not None else None,
            "userId": UserId.from_dict(obj["userId"]) if obj.get("userId") is not None else None,
            "timezone": obj.get("timezone")
        })
        return _obj


