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

from pydantic import ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.alias_entity_id import AliasEntityId
from tb_pe_client.models.entity_filter import EntityFilter
from typing import Optional, Set
from typing_extensions import Self

class SchedulerEventFilter(EntityFilter):
    """
    SchedulerEventFilter
    """ # noqa: E501
    originator: Optional[AliasEntityId] = None
    event_type: Optional[StrictStr] = Field(default=None, alias="eventType")
    originator_state_entity: Optional[StrictBool] = Field(default=None, alias="originatorStateEntity")
    default_state_entity: Optional[AliasEntityId] = Field(default=None, alias="defaultStateEntity")
    __properties: ClassVar[List[str]] = ["type", "originator", "eventType", "originatorStateEntity", "defaultStateEntity"]

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
        """Create an instance of SchedulerEventFilter from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of originator
        if self.originator:
            _dict['originator'] = self.originator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_state_entity
        if self.default_state_entity:
            _dict['defaultStateEntity'] = self.default_state_entity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SchedulerEventFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "originator": AliasEntityId.from_dict(obj["originator"]) if obj.get("originator") is not None else None,
            "eventType": obj.get("eventType"),
            "originatorStateEntity": obj.get("originatorStateEntity"),
            "defaultStateEntity": AliasEntityId.from_dict(obj["defaultStateEntity"]) if obj.get("defaultStateEntity") is not None else None
        })
        return _obj


