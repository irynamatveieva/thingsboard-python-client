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

from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.captcha_params import CaptchaParams
from typing import Optional, Set
from typing_extensions import Self

class EnterpriseCaptchaParams(CaptchaParams):
    """
    EnterpriseCaptchaParams
    """ # noqa: E501
    project_id: Optional[StrictStr] = Field(default=None, description="Your Google Cloud project ID", alias="projectId")
    service_account_credentials: Optional[StrictStr] = Field(default=None, description="Service account credentials", alias="serviceAccountCredentials")
    service_account_credentials_file_name: Optional[StrictStr] = Field(default=None, description="Service account credentials file name", alias="serviceAccountCredentialsFileName")
    android_key: Optional[StrictStr] = Field(default=None, description="The reCAPTCHA key associated with android app.", alias="androidKey")
    ios_key: Optional[StrictStr] = Field(default=None, description="The reCAPTCHA key associated with iOS app.", alias="iosKey")
    log_action_name: Optional[StrictStr] = Field(default=None, description="Optional action name used for logging", alias="logActionName")
    __properties: ClassVar[List[str]] = ["version", "projectId", "serviceAccountCredentials", "serviceAccountCredentialsFileName", "androidKey", "iosKey", "logActionName"]

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
        """Create an instance of EnterpriseCaptchaParams from a JSON string"""
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
        """Create an instance of EnterpriseCaptchaParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "version": obj.get("version"),
            "projectId": obj.get("projectId"),
            "serviceAccountCredentials": obj.get("serviceAccountCredentials"),
            "serviceAccountCredentialsFileName": obj.get("serviceAccountCredentialsFileName"),
            "androidKey": obj.get("androidKey"),
            "iosKey": obj.get("iosKey"),
            "logActionName": obj.get("logActionName")
        })
        return _obj


