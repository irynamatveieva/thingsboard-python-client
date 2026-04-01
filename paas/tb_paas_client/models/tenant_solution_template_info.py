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
from tb_paas_client.models.solution_template_level import SolutionTemplateLevel
from typing import Optional, Set
from typing_extensions import Self

class TenantSolutionTemplateInfo(BaseModel):
    """
    TenantSolutionTemplateInfo
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="ID of the solution template")
    title: Optional[StrictStr] = Field(default=None, description="Template Title")
    level: Optional[SolutionTemplateLevel] = Field(default=None, description="Level of the subscription that is required to unlock the template")
    install_timeout_ms: Optional[StrictInt] = Field(default=None, description="Timeout for the installation UI to wait while template is installing", serialization_alias="installTimeoutMs")
    tenant_telemetry_keys: Optional[List[StrictStr]] = Field(default=None, description="What keys to delete during template uninstall", serialization_alias="tenantTelemetryKeys")
    tenant_attribute_keys: Optional[List[StrictStr]] = Field(default=None, description="What attributes to delete during template uninstall", serialization_alias="tenantAttributeKeys")
    preview_image_url: Optional[StrictStr] = Field(default=None, description="URL of the preview image", serialization_alias="previewImageUrl")
    video_preview_image_url: Optional[StrictStr] = Field(default=None, description="Video preview image URL", serialization_alias="videoPreviewImageUrl")
    preview_mp4_url: Optional[StrictStr] = Field(default=None, description="Video MP4 URL", serialization_alias="previewMp4Url")
    preview_webm_url: Optional[StrictStr] = Field(default=None, description="Video WEBM URL", serialization_alias="previewWebmUrl")
    installed: Optional[StrictBool] = Field(default=None, description="Indicates that template is already installed for the current tenant")
    __properties: ClassVar[List[str]] = ["id", "title", "level", "installTimeoutMs", "tenantTelemetryKeys", "tenantAttributeKeys", "previewImageUrl", "videoPreviewImageUrl", "previewMp4Url", "previewWebmUrl", "installed"]

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
        """Create an instance of TenantSolutionTemplateInfo from a JSON string"""
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
        """Create an instance of TenantSolutionTemplateInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "level": obj.get("level"),
            "install_timeout_ms": obj.get("installTimeoutMs"),
            "tenant_telemetry_keys": obj.get("tenantTelemetryKeys"),
            "tenant_attribute_keys": obj.get("tenantAttributeKeys"),
            "preview_image_url": obj.get("previewImageUrl"),
            "video_preview_image_url": obj.get("videoPreviewImageUrl"),
            "preview_mp4_url": obj.get("previewMp4Url"),
            "preview_webm_url": obj.get("previewWebmUrl"),
            "installed": obj.get("installed")
        })
        return _obj


