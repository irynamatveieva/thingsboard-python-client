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
from uuid import UUID
from tb_pe_client.models.edge_event_action_type import EdgeEventActionType
from tb_pe_client.models.edge_event_id import EdgeEventId
from tb_pe_client.models.edge_event_type import EdgeEventType
from tb_pe_client.models.edge_id import EdgeId
from tb_pe_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class EdgeEvent(BaseModel):
    """
    EdgeEvent
    """ # noqa: E501
    id: Optional[EdgeEventId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", serialization_alias="createdTime")
    seq_id: Optional[StrictInt] = Field(default=None, serialization_alias="seqId")
    tenant_id: Optional[TenantId] = Field(default=None, serialization_alias="tenantId")
    edge_id: Optional[EdgeId] = Field(default=None, serialization_alias="edgeId")
    action: Optional[EdgeEventActionType] = None
    entity_id: Optional[UUID] = Field(default=None, serialization_alias="entityId")
    uid: Optional[StrictStr] = None
    type: Optional[EdgeEventType] = None
    body: Optional[Any] = None
    entity_group_id: Optional[UUID] = Field(default=None, serialization_alias="entityGroupId")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "seqId", "tenantId", "edgeId", "action", "entityId", "uid", "type", "body", "entityGroupId"]

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
        """Create an instance of EdgeEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenantId'] = self.tenant_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of edge_id
        if self.edge_id:
            _dict['edgeId'] = self.edge_id.to_dict()
        # set to None if body (nullable) is None
        # and model_fields_set contains the field
        if self.body is None and "body" in self.model_fields_set:
            _dict['body'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EdgeEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": EdgeEventId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "seq_id": obj.get("seqId"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "edge_id": EdgeId.from_dict(obj["edgeId"]) if obj.get("edgeId") is not None else None,
            "action": obj.get("action"),
            "entity_id": obj.get("entityId"),
            "uid": obj.get("uid"),
            "type": obj.get("type"),
            "body": obj.get("body"),
            "entity_group_id": obj.get("entityGroupId")
        })
        return _obj


