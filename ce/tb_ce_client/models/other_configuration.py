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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.power_mode import PowerMode
from typing import Optional, Set
from typing_extensions import Self

class OtherConfiguration(BaseModel):
    """
    OtherConfiguration
    """ # noqa: E501
    use_object19_for_ota_info: Optional[StrictBool] = Field(default=None, alias="useObject19ForOtaInfo")
    fw_update_strategy: Optional[StrictInt] = Field(default=None, alias="fwUpdateStrategy")
    sw_update_strategy: Optional[StrictInt] = Field(default=None, alias="swUpdateStrategy")
    client_only_observe_after_connect: Optional[StrictInt] = Field(default=None, alias="clientOnlyObserveAfterConnect")
    power_mode: Optional[PowerMode] = Field(default=None, alias="powerMode")
    psm_activity_timer: Optional[StrictInt] = Field(default=None, alias="psmActivityTimer")
    edrx_cycle: Optional[StrictInt] = Field(default=None, alias="edrxCycle")
    paging_transmission_window: Optional[StrictInt] = Field(default=None, alias="pagingTransmissionWindow")
    fw_update_resource: Optional[StrictStr] = Field(default=None, alias="fwUpdateResource")
    sw_update_resource: Optional[StrictStr] = Field(default=None, alias="swUpdateResource")
    default_object_id_ver: Optional[StrictStr] = Field(default=None, alias="defaultObjectIDVer")
    __properties: ClassVar[List[str]] = ["useObject19ForOtaInfo", "fwUpdateStrategy", "swUpdateStrategy", "clientOnlyObserveAfterConnect", "powerMode", "psmActivityTimer", "edrxCycle", "pagingTransmissionWindow", "fwUpdateResource", "swUpdateResource", "defaultObjectIDVer"]

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
            "useObject19ForOtaInfo": obj.get("useObject19ForOtaInfo"),
            "fwUpdateStrategy": obj.get("fwUpdateStrategy"),
            "swUpdateStrategy": obj.get("swUpdateStrategy"),
            "clientOnlyObserveAfterConnect": obj.get("clientOnlyObserveAfterConnect"),
            "powerMode": obj.get("powerMode"),
            "psmActivityTimer": obj.get("psmActivityTimer"),
            "edrxCycle": obj.get("edrxCycle"),
            "pagingTransmissionWindow": obj.get("pagingTransmissionWindow"),
            "fwUpdateResource": obj.get("fwUpdateResource"),
            "swUpdateResource": obj.get("swUpdateResource"),
            "defaultObjectIDVer": obj.get("defaultObjectIDVer")
        })
        return _obj


