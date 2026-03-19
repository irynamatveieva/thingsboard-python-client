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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from tb_ce_client.models.sync_strategy import SyncStrategy
from typing import Optional, Set
from typing_extensions import Self

class EntityTypeVersionCreateConfig(BaseModel):
    """
    EntityTypeVersionCreateConfig
    """ # noqa: E501
    save_relations: Optional[StrictBool] = Field(default=None, alias="saveRelations")
    save_attributes: Optional[StrictBool] = Field(default=None, alias="saveAttributes")
    save_credentials: Optional[StrictBool] = Field(default=None, alias="saveCredentials")
    save_calculated_fields: Optional[StrictBool] = Field(default=None, alias="saveCalculatedFields")
    sync_strategy: Optional[SyncStrategy] = Field(default=None, alias="syncStrategy")
    entity_ids: Optional[List[UUID]] = Field(default=None, alias="entityIds")
    all_entities: Optional[StrictBool] = Field(default=None, alias="allEntities")
    __properties: ClassVar[List[str]] = ["saveRelations", "saveAttributes", "saveCredentials", "saveCalculatedFields", "syncStrategy", "entityIds", "allEntities"]

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
        """Create an instance of EntityTypeVersionCreateConfig from a JSON string"""
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
        """Create an instance of EntityTypeVersionCreateConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "saveRelations": obj.get("saveRelations"),
            "saveAttributes": obj.get("saveAttributes"),
            "saveCredentials": obj.get("saveCredentials"),
            "saveCalculatedFields": obj.get("saveCalculatedFields"),
            "syncStrategy": obj.get("syncStrategy"),
            "entityIds": obj.get("entityIds"),
            "allEntities": obj.get("allEntities")
        })
        return _obj


