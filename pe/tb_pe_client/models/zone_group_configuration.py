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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tb_pe_client.models.cf_argument_dynamic_source_configuration import CfArgumentDynamicSourceConfiguration
from tb_pe_client.models.entity_id import EntityId
from tb_pe_client.models.entity_search_direction import EntitySearchDirection
from tb_pe_client.models.geofencing_report_strategy import GeofencingReportStrategy
from typing import Optional, Set
from typing_extensions import Self

class ZoneGroupConfiguration(BaseModel):
    """
    ZoneGroupConfiguration
    """ # noqa: E501
    ref_entity_id: Optional[EntityId] = Field(default=None, serialization_alias="refEntityId")
    ref_dynamic_source_configuration: Optional[CfArgumentDynamicSourceConfiguration] = Field(default=None, serialization_alias="refDynamicSourceConfiguration")
    perimeter_key_name: Annotated[str, Field(min_length=1, strict=True)] = Field(serialization_alias="perimeterKeyName")
    report_strategy: GeofencingReportStrategy = Field(serialization_alias="reportStrategy")
    create_relations_with_matched_zones: Optional[StrictBool] = Field(default=None, serialization_alias="createRelationsWithMatchedZones")
    relation_type: Optional[StrictStr] = Field(default=None, serialization_alias="relationType")
    direction: Optional[EntitySearchDirection] = None
    __properties: ClassVar[List[str]] = ["refEntityId", "refDynamicSourceConfiguration", "perimeterKeyName", "reportStrategy", "createRelationsWithMatchedZones", "relationType", "direction"]

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
        """Create an instance of ZoneGroupConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ref_entity_id
        if self.ref_entity_id:
            _dict['refEntityId'] = self.ref_entity_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ref_dynamic_source_configuration
        if self.ref_dynamic_source_configuration:
            _dict['refDynamicSourceConfiguration'] = self.ref_dynamic_source_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ZoneGroupConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ref_entity_id": EntityId.from_dict(obj["refEntityId"]) if obj.get("refEntityId") is not None else None,
            "ref_dynamic_source_configuration": CfArgumentDynamicSourceConfiguration.from_dict(obj["refDynamicSourceConfiguration"]) if obj.get("refDynamicSourceConfiguration") is not None else None,
            "perimeter_key_name": obj.get("perimeterKeyName"),
            "report_strategy": obj.get("reportStrategy"),
            "create_relations_with_matched_zones": obj.get("createRelationsWithMatchedZones"),
            "relation_type": obj.get("relationType"),
            "direction": obj.get("direction")
        })
        return _obj


