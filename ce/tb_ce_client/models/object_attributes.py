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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_ce_client.models.lw_m2m_version import LwM2mVersion
from typing import Optional, Set
from typing_extensions import Self

class ObjectAttributes(BaseModel):
    """
    ObjectAttributes
    """ # noqa: E501
    dim: Optional[StrictInt] = None
    ssid: Optional[StrictInt] = None
    uri: Optional[StrictStr] = None
    ver: Optional[Any] = None
    lwm2m: Optional[LwM2mVersion] = None
    pmin: Optional[StrictInt] = None
    pmax: Optional[StrictInt] = None
    gt: Optional[Union[StrictFloat, StrictInt]] = None
    lt: Optional[Union[StrictFloat, StrictInt]] = None
    st: Optional[Union[StrictFloat, StrictInt]] = None
    epmin: Optional[StrictInt] = None
    epmax: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["dim", "ssid", "uri", "ver", "lwm2m", "pmin", "pmax", "gt", "lt", "st", "epmin", "epmax"]

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
        """Create an instance of ObjectAttributes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of lwm2m
        if self.lwm2m:
            _dict['lwm2m'] = self.lwm2m.to_dict()
        # set to None if ver (nullable) is None
        # and model_fields_set contains the field
        if self.ver is None and "ver" in self.model_fields_set:
            _dict['ver'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dim": obj.get("dim"),
            "ssid": obj.get("ssid"),
            "uri": obj.get("uri"),
            "ver": obj.get("ver"),
            "lwm2m": LwM2mVersion.from_dict(obj["lwm2m"]) if obj.get("lwm2m") is not None else None,
            "pmin": obj.get("pmin"),
            "pmax": obj.get("pmax"),
            "gt": obj.get("gt"),
            "lt": obj.get("lt"),
            "st": obj.get("st"),
            "epmin": obj.get("epmin"),
            "epmax": obj.get("epmax")
        })
        return _obj


