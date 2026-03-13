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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.device_credentials_id import DeviceCredentialsId
from tb_ce_client.models.device_credentials_type import DeviceCredentialsType
from tb_ce_client.models.device_id import DeviceId
from typing import Optional, Set
from typing_extensions import Self

class DeviceCredentials(BaseModel):
    """
    A JSON value representing the device credentials.
    """ # noqa: E501
    id: DeviceCredentialsId = Field(description="The Id is automatically generated during device creation. Use 'getDeviceCredentialsByDeviceId' to obtain the id based on device id. Use 'updateDeviceCredentials' to update device credentials. ")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the device credentials creation, in milliseconds", alias="createdTime")
    device_id: DeviceId = Field(description="JSON object with the device Id.", alias="deviceId")
    credentials_type: Optional[DeviceCredentialsType] = Field(default=None, description="Type of the credentials", alias="credentialsType")
    credentials_id: StrictStr = Field(description="Unique Credentials Id per platform instance. Used to lookup credentials from the database. By default, new access token for your device. Depends on the type of the credentials.", alias="credentialsId")
    credentials_value: Optional[StrictStr] = Field(default=None, description="Value of the credentials. Null in case of ACCESS_TOKEN credentials type. Base64 value in case of X509_CERTIFICATE. Complex object in case of MQTT_BASIC and LWM2M_CREDENTIALS", alias="credentialsValue")
    version: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "createdTime", "deviceId", "credentialsType", "credentialsId", "credentialsValue", "version"]

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
        """Create an instance of DeviceCredentials from a JSON string"""
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
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device_id
        if self.device_id:
            _dict['deviceId'] = self.device_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceCredentials from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": DeviceCredentialsId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "deviceId": DeviceId.from_dict(obj["deviceId"]) if obj.get("deviceId") is not None else None,
            "credentialsType": obj.get("credentialsType"),
            "credentialsId": obj.get("credentialsId"),
            "credentialsValue": obj.get("credentialsValue"),
            "version": obj.get("version")
        })
        return _obj


