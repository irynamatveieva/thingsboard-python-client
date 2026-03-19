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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.device_profile_alarm import DeviceProfileAlarm
from tb_ce_client.models.device_profile_configuration import DeviceProfileConfiguration
from tb_ce_client.models.device_profile_provision_configuration import DeviceProfileProvisionConfiguration
from tb_ce_client.models.device_profile_transport_configuration import DeviceProfileTransportConfiguration
from typing import Optional, Set
from typing_extensions import Self

class DeviceProfileData(BaseModel):
    """
    DeviceProfileData
    """ # noqa: E501
    configuration: Optional[DeviceProfileConfiguration] = Field(default=None, description="JSON object of device profile configuration")
    transport_configuration: Optional[DeviceProfileTransportConfiguration] = Field(default=None, description="JSON object of device profile transport configuration", alias="transportConfiguration")
    provision_configuration: Optional[DeviceProfileProvisionConfiguration] = Field(default=None, description="JSON object of provisioning strategy type per device profile", alias="provisionConfiguration")
    alarms: Optional[List[DeviceProfileAlarm]] = None
    __properties: ClassVar[List[str]] = ["configuration", "transportConfiguration", "provisionConfiguration", "alarms"]

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
        """Create an instance of DeviceProfileData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transport_configuration
        if self.transport_configuration:
            _dict['transportConfiguration'] = self.transport_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of provision_configuration
        if self.provision_configuration:
            _dict['provisionConfiguration'] = self.provision_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in alarms (list)
        _items = []
        if self.alarms:
            for _item_alarms in self.alarms:
                if _item_alarms:
                    _items.append(_item_alarms.to_dict())
            _dict['alarms'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceProfileData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configuration": DeviceProfileConfiguration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None,
            "transportConfiguration": DeviceProfileTransportConfiguration.from_dict(obj["transportConfiguration"]) if obj.get("transportConfiguration") is not None else None,
            "provisionConfiguration": DeviceProfileProvisionConfiguration.from_dict(obj["provisionConfiguration"]) if obj.get("provisionConfiguration") is not None else None,
            "alarms": [DeviceProfileAlarm.from_dict(_item) for _item in obj["alarms"]] if obj.get("alarms") is not None else None
        })
        return _obj


