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
from tb_ce_client.models.notification_delivery_method import NotificationDeliveryMethod
from tb_ce_client.models.notification_id import NotificationId
from tb_ce_client.models.notification_info import NotificationInfo
from tb_ce_client.models.notification_request_id import NotificationRequestId
from tb_ce_client.models.notification_status import NotificationStatus
from tb_ce_client.models.notification_type import NotificationType
from tb_ce_client.models.user_id import UserId
from typing import Optional, Set
from typing_extensions import Self

class Notification(BaseModel):
    """
    Notification
    """ # noqa: E501
    id: Optional[NotificationId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", serialization_alias="createdTime")
    request_id: Optional[NotificationRequestId] = Field(default=None, serialization_alias="requestId")
    recipient_id: Optional[UserId] = Field(default=None, serialization_alias="recipientId")
    type: Optional[NotificationType] = None
    delivery_method: Optional[NotificationDeliveryMethod] = Field(default=None, serialization_alias="deliveryMethod")
    subject: Optional[StrictStr] = None
    text: Optional[StrictStr] = None
    additional_config: Optional[Any] = Field(default=None, serialization_alias="additionalConfig")
    info: Optional[NotificationInfo] = None
    status: Optional[NotificationStatus] = None
    __properties: ClassVar[List[str]] = ["id", "createdTime", "requestId", "recipientId", "type", "deliveryMethod", "subject", "text", "additionalConfig", "info", "status"]

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
        """Create an instance of Notification from a JSON string"""
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
            "created_time",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of request_id
        if self.request_id:
            _dict['requestId'] = self.request_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recipient_id
        if self.recipient_id:
            _dict['recipientId'] = self.recipient_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict['info'] = self.info.to_dict()
        # set to None if additional_config (nullable) is None
        # and model_fields_set contains the field
        if self.additional_config is None and "additional_config" in self.model_fields_set:
            _dict['additionalConfig'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Notification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": NotificationId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "request_id": NotificationRequestId.from_dict(obj["requestId"]) if obj.get("requestId") is not None else None,
            "recipient_id": UserId.from_dict(obj["recipientId"]) if obj.get("recipientId") is not None else None,
            "type": obj.get("type"),
            "delivery_method": obj.get("deliveryMethod"),
            "subject": obj.get("subject"),
            "text": obj.get("text"),
            "additional_config": obj.get("additionalConfig"),
            "info": NotificationInfo.from_dict(obj["info"]) if obj.get("info") is not None else None,
            "status": obj.get("status")
        })
        return _obj


