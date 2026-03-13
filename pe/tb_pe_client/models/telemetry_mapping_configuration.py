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
from tb_pe_client.models.object_attributes import ObjectAttributes
from tb_pe_client.models.telemetry_observe_strategy import TelemetryObserveStrategy
from typing import Optional, Set
from typing_extensions import Self

class TelemetryMappingConfiguration(BaseModel):
    """
    TelemetryMappingConfiguration
    """ # noqa: E501
    key_name: Optional[Dict[str, StrictStr]] = Field(default=None, description="Map of LwM2M resource paths to telemetry key names", alias="keyName")
    observe: Optional[List[StrictStr]] = Field(default=None, description="Set of resources to observe")
    attribute: Optional[List[StrictStr]] = Field(default=None, description="Set of attribute keys")
    telemetry: Optional[List[StrictStr]] = Field(default=None, description="Set of telemetry keys")
    attribute_lwm2m: Optional[Dict[str, ObjectAttributes]] = Field(default=None, description="Map of resource paths to specific LwM2M object attributes", alias="attributeLwm2m")
    init_attr_tel_as_obs_strategy: Optional[StrictBool] = Field(default=None, alias="initAttrTelAsObsStrategy")
    observe_strategy: Optional[TelemetryObserveStrategy] = Field(default=None, description="Observation strategy for telemetry", alias="observeStrategy")
    __properties: ClassVar[List[str]] = ["keyName", "observe", "attribute", "telemetry", "attributeLwm2m", "initAttrTelAsObsStrategy", "observeStrategy"]

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
        """Create an instance of TelemetryMappingConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in attribute_lwm2m (dict)
        _field_dict = {}
        if self.attribute_lwm2m:
            for _key_attribute_lwm2m in self.attribute_lwm2m:
                if self.attribute_lwm2m[_key_attribute_lwm2m]:
                    _field_dict[_key_attribute_lwm2m] = self.attribute_lwm2m[_key_attribute_lwm2m].to_dict()
            _dict['attributeLwm2m'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TelemetryMappingConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyName": obj.get("keyName"),
            "observe": obj.get("observe"),
            "attribute": obj.get("attribute"),
            "telemetry": obj.get("telemetry"),
            "attributeLwm2m": dict(
                (_k, ObjectAttributes.from_dict(_v))
                for _k, _v in obj["attributeLwm2m"].items()
            )
            if obj.get("attributeLwm2m") is not None
            else None,
            "initAttrTelAsObsStrategy": obj.get("initAttrTelAsObsStrategy"),
            "observeStrategy": obj.get("observeStrategy")
        })
        return _obj


