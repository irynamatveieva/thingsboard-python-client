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
from typing import Optional, Set
from typing_extensions import Self

class SystemInfoData(BaseModel):
    """
    SystemInfoData
    """ # noqa: E501
    service_id: Optional[StrictStr] = Field(default=None, description="Service Id.", serialization_alias="serviceId")
    service_type: Optional[StrictStr] = Field(default=None, description="Service type.", serialization_alias="serviceType")
    cpu_usage: Optional[StrictInt] = Field(default=None, description="CPU usage, in percent.", serialization_alias="cpuUsage")
    cpu_count: Optional[StrictInt] = Field(default=None, description="Total CPU usage.", serialization_alias="cpuCount")
    memory_usage: Optional[StrictInt] = Field(default=None, description="Memory usage, in percent.", serialization_alias="memoryUsage")
    total_memory: Optional[StrictInt] = Field(default=None, description="Total memory in bytes.", serialization_alias="totalMemory")
    disc_usage: Optional[StrictInt] = Field(default=None, description="Disk usage, in percent.", serialization_alias="discUsage")
    total_disc_space: Optional[StrictInt] = Field(default=None, description="Total disc space in bytes.", serialization_alias="totalDiscSpace")
    __properties: ClassVar[List[str]] = ["serviceId", "serviceType", "cpuUsage", "cpuCount", "memoryUsage", "totalMemory", "discUsage", "totalDiscSpace"]

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
        """Create an instance of SystemInfoData from a JSON string"""
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
        """Create an instance of SystemInfoData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "service_id": obj.get("serviceId"),
            "service_type": obj.get("serviceType"),
            "cpu_usage": obj.get("cpuUsage"),
            "cpu_count": obj.get("cpuCount"),
            "memory_usage": obj.get("memoryUsage"),
            "total_memory": obj.get("totalMemory"),
            "disc_usage": obj.get("discUsage"),
            "total_disc_space": obj.get("totalDiscSpace")
        })
        return _obj


