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
from tb_paas_client.models.converter_id import ConverterId
from tb_paas_client.models.converter_type import ConverterType
from tb_paas_client.models.debug_settings import DebugSettings
from tb_paas_client.models.integration_type import IntegrationType
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class Converter(BaseModel):
    """
    Converter
    """ # noqa: E501
    id: Optional[ConverterId] = Field(default=None, description="JSON object with the Converter Id. Specify this field to update the Converter. Referencing non-existing Converter Id will cause error. Omit this field to create new Converter.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the converter creation, in milliseconds", alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id", alias="tenantId")
    name: StrictStr = Field(description="Unique Converter Name in scope of Tenant")
    type: ConverterType = Field(description="The type of the converter to process incoming or outgoing messages")
    integration_type: Optional[IntegrationType] = Field(default=None, description="The type of the integration to which the converter is dedicated", alias="integrationType")
    debug_mode: Optional[StrictBool] = Field(default=None, description="Enable/disable debug. ", alias="debugMode")
    debug_settings: Optional[DebugSettings] = Field(default=None, description="Debug settings object.", alias="debugSettings")
    configuration: Optional[Any] = Field(default=None, description="JSON object representing converter configuration. It should contain one of two possible fields: 'decoder' or 'encoder'. The former is used when the converter has UPLINK type, the latter is used - when DOWNLINK type. It can contain both 'decoder' and 'encoder' fields, when the correct one is specified for the appropriate converter type, another one can be set to 'null'")
    additional_info: Optional[Any] = Field(default=None, description="Additional parameters of the converter", alias="additionalInfo")
    edge_template: Optional[StrictBool] = Field(default=None, description="Boolean flag that specifies that is regular or edge template converter", alias="edgeTemplate")
    converter_version: Optional[StrictInt] = Field(default=None, alias="converterVersion")
    version: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "name", "type", "integrationType", "debugMode", "debugSettings", "configuration", "additionalInfo", "edgeTemplate", "converterVersion", "version"]

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
        """Create an instance of Converter from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
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
        # override the default output from pydantic by calling `to_dict()` of debug_settings
        if self.debug_settings:
            _dict['debugSettings'] = self.debug_settings.to_dict()
        # set to None if configuration (nullable) is None
        # and model_fields_set contains the field
        if self.configuration is None and "configuration" in self.model_fields_set:
            _dict['configuration'] = None

        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Converter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": ConverterId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "name": obj.get("name"),
            "type": obj.get("type"),
            "integrationType": obj.get("integrationType"),
            "debugMode": obj.get("debugMode"),
            "debugSettings": DebugSettings.from_dict(obj["debugSettings"]) if obj.get("debugSettings") is not None else None,
            "configuration": obj.get("configuration"),
            "additionalInfo": obj.get("additionalInfo"),
            "edgeTemplate": obj.get("edgeTemplate"),
            "converterVersion": obj.get("converterVersion"),
            "version": obj.get("version")
        })
        return _obj


