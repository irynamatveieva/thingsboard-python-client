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
from tb_paas_client.models.mobile_app_version_info import MobileAppVersionInfo
from tb_paas_client.models.o_auth2_client_login_info import OAuth2ClientLoginInfo
from tb_paas_client.models.sign_up_self_registration_params import SignUpSelfRegistrationParams
from tb_paas_client.models.store_info import StoreInfo
from typing import Optional, Set
from typing_extensions import Self

class LoginMobileInfo(BaseModel):
    """
    LoginMobileInfo
    """ # noqa: E501
    o_auth2_client_login_infos: Optional[List[OAuth2ClientLoginInfo]] = Field(default=None, alias="oAuth2ClientLoginInfos")
    self_registration_params: Optional[SignUpSelfRegistrationParams] = Field(default=None, alias="selfRegistrationParams")
    store_info: Optional[StoreInfo] = Field(default=None, alias="storeInfo")
    version_info: Optional[MobileAppVersionInfo] = Field(default=None, alias="versionInfo")
    __properties: ClassVar[List[str]] = ["oAuth2ClientLoginInfos", "selfRegistrationParams", "storeInfo", "versionInfo"]

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
        """Create an instance of LoginMobileInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in o_auth2_client_login_infos (list)
        _items = []
        if self.o_auth2_client_login_infos:
            for _item_o_auth2_client_login_infos in self.o_auth2_client_login_infos:
                if _item_o_auth2_client_login_infos:
                    _items.append(_item_o_auth2_client_login_infos.to_dict())
            _dict['oAuth2ClientLoginInfos'] = _items
        # override the default output from pydantic by calling `to_dict()` of self_registration_params
        if self.self_registration_params:
            _dict['selfRegistrationParams'] = self.self_registration_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of store_info
        if self.store_info:
            _dict['storeInfo'] = self.store_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version_info
        if self.version_info:
            _dict['versionInfo'] = self.version_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoginMobileInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "oAuth2ClientLoginInfos": [OAuth2ClientLoginInfo.from_dict(_item) for _item in obj["oAuth2ClientLoginInfos"]] if obj.get("oAuth2ClientLoginInfos") is not None else None,
            "selfRegistrationParams": SignUpSelfRegistrationParams.from_dict(obj["selfRegistrationParams"]) if obj.get("selfRegistrationParams") is not None else None,
            "storeInfo": StoreInfo.from_dict(obj["storeInfo"]) if obj.get("storeInfo") is not None else None,
            "versionInfo": MobileAppVersionInfo.from_dict(obj["versionInfo"]) if obj.get("versionInfo") is not None else None
        })
        return _obj


