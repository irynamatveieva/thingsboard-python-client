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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.o_auth2_client_registration_template_id import OAuth2ClientRegistrationTemplateId
from tb_ce_client.models.o_auth2_mapper_config import OAuth2MapperConfig
from typing import Optional, Set
from typing_extensions import Self

class OAuth2ClientRegistrationTemplate(BaseModel):
    """
    OAuth2ClientRegistrationTemplate
    """ # noqa: E501
    id: Optional[OAuth2ClientRegistrationTemplateId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", serialization_alias="createdTime")
    provider_id: StrictStr = Field(description="OAuth2 provider identifier (e.g. its name)", serialization_alias="providerId")
    mapper_config: Optional[OAuth2MapperConfig] = Field(default=None, description="Default config for mapping OAuth2 log in response to platform entities", serialization_alias="mapperConfig")
    authorization_uri: Optional[StrictStr] = Field(default=None, description="Default authorization URI of the OAuth2 provider", serialization_alias="authorizationUri")
    access_token_uri: Optional[StrictStr] = Field(default=None, description="Default access token URI of the OAuth2 provider", serialization_alias="accessTokenUri")
    scope: Optional[List[StrictStr]] = Field(default=None, description="Default OAuth scopes that will be requested from OAuth2 platform")
    user_info_uri: Optional[StrictStr] = Field(default=None, description="Default user info URI of the OAuth2 provider", serialization_alias="userInfoUri")
    user_name_attribute_name: Optional[StrictStr] = Field(default=None, description="Default name of the username attribute in OAuth2 provider log in response", serialization_alias="userNameAttributeName")
    jwk_set_uri: Optional[StrictStr] = Field(default=None, description="Default JSON Web Key URI of the OAuth2 provider", serialization_alias="jwkSetUri")
    client_authentication_method: Optional[StrictStr] = Field(default=None, description="Default client authentication method to use: 'BASIC' or 'POST'", serialization_alias="clientAuthenticationMethod")
    comment: Optional[StrictStr] = Field(default=None, description="Comment for OAuth2 provider")
    login_button_icon: Optional[StrictStr] = Field(default=None, description="Default log in button icon for OAuth2 provider", serialization_alias="loginButtonIcon")
    login_button_label: Optional[StrictStr] = Field(default=None, description="Default OAuth2 provider label", serialization_alias="loginButtonLabel")
    help_link: Optional[StrictStr] = Field(default=None, description="Help link for OAuth2 provider", serialization_alias="helpLink")
    additional_info: Optional[Any] = Field(default=None, serialization_alias="additionalInfo")
    name: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "createdTime", "providerId", "mapperConfig", "authorizationUri", "accessTokenUri", "scope", "userInfoUri", "userNameAttributeName", "jwkSetUri", "clientAuthenticationMethod", "comment", "loginButtonIcon", "loginButtonLabel", "helpLink", "additionalInfo", "name"]

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
        """Create an instance of OAuth2ClientRegistrationTemplate from a JSON string"""
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
            "created_time",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mapper_config
        if self.mapper_config:
            _dict['mapperConfig'] = self.mapper_config.to_dict()
        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OAuth2ClientRegistrationTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": OAuth2ClientRegistrationTemplateId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "provider_id": obj.get("providerId"),
            "mapper_config": OAuth2MapperConfig.from_dict(obj["mapperConfig"]) if obj.get("mapperConfig") is not None else None,
            "authorization_uri": obj.get("authorizationUri"),
            "access_token_uri": obj.get("accessTokenUri"),
            "scope": obj.get("scope"),
            "user_info_uri": obj.get("userInfoUri"),
            "user_name_attribute_name": obj.get("userNameAttributeName"),
            "jwk_set_uri": obj.get("jwkSetUri"),
            "client_authentication_method": obj.get("clientAuthenticationMethod"),
            "comment": obj.get("comment"),
            "login_button_icon": obj.get("loginButtonIcon"),
            "login_button_label": obj.get("loginButtonLabel"),
            "help_link": obj.get("helpLink"),
            "additional_info": obj.get("additionalInfo"),
            "name": obj.get("name")
        })
        return _obj


