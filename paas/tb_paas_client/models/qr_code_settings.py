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
from tb_paas_client.models.mobile_app_bundle_id import MobileAppBundleId
from tb_paas_client.models.qr_code_config import QRCodeConfig
from tb_paas_client.models.qr_code_settings_id import QrCodeSettingsId
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class QrCodeSettings(BaseModel):
    """
    A JSON value representing the mobile apps configuration
    """ # noqa: E501
    id: Optional[QrCodeSettingsId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id.", alias="tenantId")
    use_system_settings: Optional[StrictBool] = Field(default=None, description="Use settings from system level", alias="useSystemSettings")
    use_default_app: Optional[StrictBool] = Field(default=None, description="Type of application: true means use default Thingsboard app", alias="useDefaultApp")
    mobile_app_bundle_id: Optional[MobileAppBundleId] = Field(default=None, description="Mobile app bundle.", alias="mobileAppBundleId")
    qr_code_config: QRCodeConfig = Field(description="QR code config configuration.", alias="qrCodeConfig")
    android_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if google play link is available", alias="androidEnabled")
    ios_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if apple store link is available", alias="iosEnabled")
    google_play_link: Optional[StrictStr] = Field(default=None, alias="googlePlayLink")
    app_store_link: Optional[StrictStr] = Field(default=None, alias="appStoreLink")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "useSystemSettings", "useDefaultApp", "mobileAppBundleId", "qrCodeConfig", "androidEnabled", "iosEnabled", "googlePlayLink", "appStoreLink"]

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
        """Create an instance of QrCodeSettings from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "google_play_link",
            "app_store_link",
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
        # override the default output from pydantic by calling `to_dict()` of mobile_app_bundle_id
        if self.mobile_app_bundle_id:
            _dict['mobileAppBundleId'] = self.mobile_app_bundle_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of qr_code_config
        if self.qr_code_config:
            _dict['qrCodeConfig'] = self.qr_code_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QrCodeSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": QrCodeSettingsId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "useSystemSettings": obj.get("useSystemSettings"),
            "useDefaultApp": obj.get("useDefaultApp"),
            "mobileAppBundleId": MobileAppBundleId.from_dict(obj["mobileAppBundleId"]) if obj.get("mobileAppBundleId") is not None else None,
            "qrCodeConfig": QRCodeConfig.from_dict(obj["qrCodeConfig"]) if obj.get("qrCodeConfig") is not None else None,
            "androidEnabled": obj.get("androidEnabled"),
            "iosEnabled": obj.get("iosEnabled"),
            "googlePlayLink": obj.get("googlePlayLink"),
            "appStoreLink": obj.get("appStoreLink")
        })
        return _obj


