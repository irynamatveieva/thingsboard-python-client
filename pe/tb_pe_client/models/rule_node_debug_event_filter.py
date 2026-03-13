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

from pydantic import ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.event_filter import EventFilter
from tb_pe_client.models.event_type import EventType
from typing import Optional, Set
from typing_extensions import Self

class RuleNodeDebugEventFilter(EventFilter):
    """
    RuleNodeDebugEventFilter
    """ # noqa: E501
    server: Optional[StrictStr] = Field(default=None, description="String value representing the server name, identifier or ip address where the platform is running")
    is_error: Optional[StrictBool] = Field(default=None, description="Boolean value to filter the errors", alias="isError")
    error_str: Optional[StrictStr] = Field(default=None, description="The case insensitive 'contains' filter based on error message", alias="errorStr")
    msg_direction_type: Optional[StrictStr] = Field(default=None, description="String value representing msg direction type (incoming to entity or outcoming from entity)", alias="msgDirectionType")
    entity_id: Optional[StrictStr] = Field(default=None, description="String value representing the entity id in the event body (originator of the message)", alias="entityId")
    entity_type: Optional[StrictStr] = Field(default=None, description="String value representing the entity type", alias="entityType")
    msg_id: Optional[StrictStr] = Field(default=None, description="String value representing the message id in the rule engine", alias="msgId")
    msg_type: Optional[StrictStr] = Field(default=None, description="String value representing the message type", alias="msgType")
    relation_type: Optional[StrictStr] = Field(default=None, description="String value representing the type of message routing", alias="relationType")
    data_search: Optional[StrictStr] = Field(default=None, description="The case insensitive 'contains' filter based on data (key and value) for the message.", alias="dataSearch")
    metadata_search: Optional[StrictStr] = Field(default=None, description="The case insensitive 'contains' filter based on metadata (key and value) for the message.", alias="metadataSearch")
    __properties: ClassVar[List[str]] = ["eventType", "notEmpty", "server", "isError", "errorStr", "msgDirectionType", "entityId", "entityType", "msgId", "msgType", "relationType", "dataSearch", "metadataSearch"]

    @field_validator('is_error')
    def is_error_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false', 'true']):
            raise ValueError("must be one of enum values ('false', 'true')")
        return value

    @field_validator('msg_direction_type')
    def msg_direction_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['IN', 'OUT']):
            raise ValueError("must be one of enum values ('IN', 'OUT')")
        return value

    @field_validator('entity_type')
    def entity_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DEVICE']):
            raise ValueError("must be one of enum values ('DEVICE')")
        return value

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
        """Create an instance of RuleNodeDebugEventFilter from a JSON string"""
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
        """Create an instance of RuleNodeDebugEventFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eventType": obj.get("eventType"),
            "notEmpty": obj.get("notEmpty"),
            "server": obj.get("server"),
            "isError": obj.get("isError"),
            "errorStr": obj.get("errorStr"),
            "msgDirectionType": obj.get("msgDirectionType"),
            "entityId": obj.get("entityId"),
            "entityType": obj.get("entityType"),
            "msgId": obj.get("msgId"),
            "msgType": obj.get("msgType"),
            "relationType": obj.get("relationType"),
            "dataSearch": obj.get("dataSearch"),
            "metadataSearch": obj.get("metadataSearch")
        })
        return _obj


