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
from tb_pe_client.models.checksum_algorithm import ChecksumAlgorithm
from tb_pe_client.models.device_profile_id import DeviceProfileId
from tb_pe_client.models.ota_package_id import OtaPackageId
from tb_pe_client.models.ota_package_type import OtaPackageType
from tb_pe_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class OtaPackageInfo(BaseModel):
    """
    OtaPackageInfo
    """ # noqa: E501
    id: Optional[OtaPackageId] = Field(default=None, description="JSON object with the ota package Id. Specify existing ota package Id to update the ota package. Referencing non-existing ota package id will cause error. Omit this field to create new ota package.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the ota package creation, in milliseconds", alias="createdTime")
    additional_info: Optional[Any] = Field(default=None, description="OTA Package description.", alias="additionalInfo")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id. Tenant Id of the ota package can't be changed.", alias="tenantId")
    device_profile_id: Optional[DeviceProfileId] = Field(default=None, description="JSON object with Device Profile Id. Device Profile Id of the ota package can't be changed.", alias="deviceProfileId")
    type: Optional[OtaPackageType] = Field(default=None, description="OTA Package type.")
    title: Optional[StrictStr] = Field(default=None, description="OTA Package title.")
    version: Optional[StrictStr] = Field(default=None, description="OTA Package version.")
    tag: Optional[StrictStr] = Field(default=None, description="OTA Package tag.")
    url: Optional[StrictStr] = Field(default=None, description="OTA Package url.")
    has_data: Optional[StrictBool] = Field(default=None, description="Indicates OTA Package 'has data'. Field is returned from DB ('true' if data exists or url is set).  If OTA Package 'has data' is 'false' we can not assign the OTA Package to the Device or Device Profile.", alias="hasData")
    file_name: Optional[StrictStr] = Field(default=None, description="OTA Package file name.", alias="fileName")
    content_type: Optional[StrictStr] = Field(default=None, description="OTA Package content type.", alias="contentType")
    checksum_algorithm: Optional[ChecksumAlgorithm] = Field(default=None, description="OTA Package checksum algorithm.", alias="checksumAlgorithm")
    checksum: Optional[StrictStr] = Field(default=None, description="OTA Package checksum.")
    data_size: Optional[StrictInt] = Field(default=None, description="OTA Package data size.", alias="dataSize")
    name: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "createdTime", "additionalInfo", "tenantId", "deviceProfileId", "type", "title", "version", "tag", "url", "hasData", "fileName", "contentType", "checksumAlgorithm", "checksum", "dataSize", "name"]

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
        """Create an instance of OtaPackageInfo from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "tag",
            "has_data",
            "file_name",
            "content_type",
            "checksum_algorithm",
            "checksum",
            "data_size",
            "name",
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
        # override the default output from pydantic by calling `to_dict()` of device_profile_id
        if self.device_profile_id:
            _dict['deviceProfileId'] = self.device_profile_id.to_dict()
        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OtaPackageInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": OtaPackageId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "additionalInfo": obj.get("additionalInfo"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "deviceProfileId": DeviceProfileId.from_dict(obj["deviceProfileId"]) if obj.get("deviceProfileId") is not None else None,
            "type": obj.get("type"),
            "title": obj.get("title"),
            "version": obj.get("version"),
            "tag": obj.get("tag"),
            "url": obj.get("url"),
            "hasData": obj.get("hasData"),
            "fileName": obj.get("fileName"),
            "contentType": obj.get("contentType"),
            "checksumAlgorithm": obj.get("checksumAlgorithm"),
            "checksum": obj.get("checksum"),
            "dataSize": obj.get("dataSize"),
            "name": obj.get("name")
        })
        return _obj


