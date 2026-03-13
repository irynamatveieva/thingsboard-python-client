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

from pydantic import ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.authentication_protocol import AuthenticationProtocol
from tb_paas_client.models.device_transport_configuration import DeviceTransportConfiguration
from tb_paas_client.models.privacy_protocol import PrivacyProtocol
from tb_paas_client.models.snmp_protocol_version import SnmpProtocolVersion
from typing import Optional, Set
from typing_extensions import Self

class SnmpDeviceTransportConfiguration(DeviceTransportConfiguration):
    """
    SnmpDeviceTransportConfiguration
    """ # noqa: E501
    host: Optional[StrictStr] = None
    port: Optional[StrictInt] = None
    protocol_version: Optional[SnmpProtocolVersion] = Field(default=None, alias="protocolVersion")
    community: Optional[StrictStr] = None
    username: Optional[StrictStr] = None
    security_name: Optional[StrictStr] = Field(default=None, alias="securityName")
    context_name: Optional[StrictStr] = Field(default=None, alias="contextName")
    authentication_protocol: Optional[AuthenticationProtocol] = Field(default=None, alias="authenticationProtocol")
    authentication_passphrase: Optional[StrictStr] = Field(default=None, alias="authenticationPassphrase")
    privacy_protocol: Optional[PrivacyProtocol] = Field(default=None, alias="privacyProtocol")
    privacy_passphrase: Optional[StrictStr] = Field(default=None, alias="privacyPassphrase")
    engine_id: Optional[StrictStr] = Field(default=None, alias="engineId")
    __properties: ClassVar[List[str]] = ["type", "host", "port", "protocolVersion", "community", "username", "securityName", "contextName", "authenticationProtocol", "authenticationPassphrase", "privacyProtocol", "privacyPassphrase", "engineId"]

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
        """Create an instance of SnmpDeviceTransportConfiguration from a JSON string"""
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
        """Create an instance of SnmpDeviceTransportConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "host": obj.get("host"),
            "port": obj.get("port"),
            "protocolVersion": obj.get("protocolVersion"),
            "community": obj.get("community"),
            "username": obj.get("username"),
            "securityName": obj.get("securityName"),
            "contextName": obj.get("contextName"),
            "authenticationProtocol": obj.get("authenticationProtocol"),
            "authenticationPassphrase": obj.get("authenticationPassphrase"),
            "privacyProtocol": obj.get("privacyProtocol"),
            "privacyPassphrase": obj.get("privacyPassphrase"),
            "engineId": obj.get("engineId")
        })
        return _obj


