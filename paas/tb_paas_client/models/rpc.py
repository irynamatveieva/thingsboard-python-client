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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.device_id import DeviceId
from tb_paas_client.models.rpc_id import RpcId
from tb_paas_client.models.rpc_status import RpcStatus
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class Rpc(BaseModel):
    """
    Rpc
    """ # noqa: E501
    id: Optional[RpcId] = Field(default=None, description="JSON object with the rpc Id. Referencing non-existing rpc Id will cause error.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the rpc creation, in milliseconds", serialization_alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id.", serialization_alias="tenantId")
    device_id: Optional[DeviceId] = Field(default=None, description="JSON object with Device Id.", serialization_alias="deviceId")
    expiration_time: Optional[StrictInt] = Field(default=None, description="Expiration time of the request.", serialization_alias="expirationTime")
    request: Optional[Any] = Field(default=None, description="The request body that will be used to send message to device.")
    response: Optional[Any] = Field(default=None, description="The response from the device.")
    status: Optional[RpcStatus] = Field(default=None, description="The current status of the RPC call.")
    additional_info: Optional[Any] = Field(default=None, description="Additional info used in the rule engine to process the updates to the RPC state.", serialization_alias="additionalInfo")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "deviceId", "expirationTime", "request", "response", "status", "additionalInfo"]

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
        """Create an instance of Rpc from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "device_id",
            "expiration_time",
            "request",
            "response",
            "status",
            "additional_info",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenantId'] = self.tenant_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device_id
        if self.device_id:
            _dict['deviceId'] = self.device_id.to_dict()
        # set to None if request (nullable) is None
        # and model_fields_set contains the field
        if self.request is None and "request" in self.model_fields_set:
            _dict['request'] = None

        # set to None if response (nullable) is None
        # and model_fields_set contains the field
        if self.response is None and "response" in self.model_fields_set:
            _dict['response'] = None

        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Rpc from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": RpcId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "device_id": DeviceId.from_dict(obj["deviceId"]) if obj.get("deviceId") is not None else None,
            "expiration_time": obj.get("expirationTime"),
            "request": obj.get("request"),
            "response": obj.get("response"),
            "status": obj.get("status"),
            "additional_info": obj.get("additionalInfo")
        })
        return _obj


