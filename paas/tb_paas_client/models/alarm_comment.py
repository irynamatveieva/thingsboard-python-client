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
from tb_paas_client.models.alarm_comment_id import AlarmCommentId
from tb_paas_client.models.alarm_comment_type import AlarmCommentType
from tb_paas_client.models.alarm_id import AlarmId
from tb_paas_client.models.user_id import UserId
from typing import Optional, Set
from typing_extensions import Self

class AlarmComment(BaseModel):
    """
    AlarmComment
    """ # noqa: E501
    id: Optional[AlarmCommentId] = Field(default=None, description="JSON object with the alarm comment Id. Specify this field to update the alarm comment. Referencing non-existing alarm Id will cause error. Omit this field to create new alarm.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the alarm comment creation, in milliseconds", serialization_alias="createdTime")
    alarm_id: Optional[AlarmId] = Field(default=None, description="JSON object with Alarm id.", serialization_alias="alarmId")
    user_id: Optional[UserId] = Field(default=None, description="JSON object with User id.", serialization_alias="userId")
    type: Optional[AlarmCommentType] = Field(default=None, description="Defines origination of comment. System type means comment was created by TB. OTHER type means comment was created by user.")
    comment: Optional[Any] = Field(default=None, description="JSON object with text of comment.")
    name: Optional[StrictStr] = Field(default=None, description="representing comment text")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "alarmId", "userId", "type", "comment", "name"]

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
        """Create an instance of AlarmComment from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "alarm_id",
            "user_id",
            "name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of alarm_id
        if self.alarm_id:
            _dict['alarmId'] = self.alarm_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_id
        if self.user_id:
            _dict['userId'] = self.user_id.to_dict()
        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlarmComment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": AlarmCommentId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "alarm_id": AlarmId.from_dict(obj["alarmId"]) if obj.get("alarmId") is not None else None,
            "user_id": UserId.from_dict(obj["userId"]) if obj.get("userId") is not None else None,
            "type": obj.get("type"),
            "comment": obj.get("comment"),
            "name": obj.get("name")
        })
        return _obj


