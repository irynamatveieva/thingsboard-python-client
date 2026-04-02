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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.power_mode import PowerMode
from typing import Optional, Set
from typing_extensions import Self

class OtherConfiguration(BaseModel):
    """
    OtherConfiguration
    """ # noqa: E501
    power_mode: Optional[PowerMode] = Field(default=None, serialization_alias="powerMode")
    psm_activity_timer: Optional[StrictInt] = Field(default=None, serialization_alias="psmActivityTimer")
    edrx_cycle: Optional[StrictInt] = Field(default=None, serialization_alias="edrxCycle")
    paging_transmission_window: Optional[StrictInt] = Field(default=None, serialization_alias="pagingTransmissionWindow")
    use_object19_for_ota_info: Optional[StrictBool] = Field(default=None, serialization_alias="useObject19ForOtaInfo")
    fw_update_strategy: Optional[StrictInt] = Field(default=None, serialization_alias="fwUpdateStrategy")
    sw_update_strategy: Optional[StrictInt] = Field(default=None, serialization_alias="swUpdateStrategy")
    client_only_observe_after_connect: Optional[StrictInt] = Field(default=None, serialization_alias="clientOnlyObserveAfterConnect")
    fw_update_resource: Optional[StrictStr] = Field(default=None, serialization_alias="fwUpdateResource")
    sw_update_resource: Optional[StrictStr] = Field(default=None, serialization_alias="swUpdateResource")
    default_object_id_ver: Optional[StrictStr] = Field(default=None, serialization_alias="defaultObjectIDVer")
    __properties: ClassVar[List[str]] = ["powerMode", "psmActivityTimer", "edrxCycle", "pagingTransmissionWindow", "useObject19ForOtaInfo", "fwUpdateStrategy", "swUpdateStrategy", "clientOnlyObserveAfterConnect", "fwUpdateResource", "swUpdateResource", "defaultObjectIDVer"]

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
        """Create an instance of OtherConfiguration from a JSON string"""
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
        """Create an instance of OtherConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "power_mode": obj.get("powerMode"),
            "psm_activity_timer": obj.get("psmActivityTimer"),
            "edrx_cycle": obj.get("edrxCycle"),
            "paging_transmission_window": obj.get("pagingTransmissionWindow"),
            "use_object19_for_ota_info": obj.get("useObject19ForOtaInfo"),
            "fw_update_strategy": obj.get("fwUpdateStrategy"),
            "sw_update_strategy": obj.get("swUpdateStrategy"),
            "client_only_observe_after_connect": obj.get("clientOnlyObserveAfterConnect"),
            "fw_update_resource": obj.get("fwUpdateResource"),
            "sw_update_resource": obj.get("swUpdateResource"),
            "default_object_id_ver": obj.get("defaultObjectIDVer")
        })
        return _obj


