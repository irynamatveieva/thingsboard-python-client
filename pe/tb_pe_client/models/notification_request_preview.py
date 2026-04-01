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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.delivery_method_notification_template import DeliveryMethodNotificationTemplate
from typing import Optional, Set
from typing_extensions import Self

class NotificationRequestPreview(BaseModel):
    """
    NotificationRequestPreview
    """ # noqa: E501
    processed_templates: Optional[Dict[str, DeliveryMethodNotificationTemplate]] = Field(default=None, serialization_alias="processedTemplates")
    total_recipients_count: Optional[StrictInt] = Field(default=None, serialization_alias="totalRecipientsCount")
    recipients_count_by_target: Optional[Dict[str, StrictInt]] = Field(default=None, serialization_alias="recipientsCountByTarget")
    recipients_preview: Optional[List[StrictStr]] = Field(default=None, serialization_alias="recipientsPreview")
    __properties: ClassVar[List[str]] = ["processedTemplates", "totalRecipientsCount", "recipientsCountByTarget", "recipientsPreview"]

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
        """Create an instance of NotificationRequestPreview from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in processed_templates (dict)
        _field_dict = {}
        if self.processed_templates:
            for _key_processed_templates in self.processed_templates:
                if self.processed_templates[_key_processed_templates]:
                    _field_dict[_key_processed_templates] = self.processed_templates[_key_processed_templates].to_dict()
            _dict['processedTemplates'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationRequestPreview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "processed_templates": dict(
                (_k, DeliveryMethodNotificationTemplate.from_dict(_v))
                for _k, _v in obj["processedTemplates"].items()
            )
            if obj.get("processedTemplates") is not None
            else None,
            "total_recipients_count": obj.get("totalRecipientsCount"),
            "recipients_count_by_target": obj.get("recipientsCountByTarget"),
            "recipients_preview": obj.get("recipientsPreview")
        })
        return _obj


