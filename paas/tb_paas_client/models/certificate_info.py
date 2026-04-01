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
from tb_paas_client.models.acme_certificate_id import AcmeCertificateId
from tb_paas_client.models.certificate_status import CertificateStatus
from typing import Optional, Set
from typing_extensions import Self

class CertificateInfo(BaseModel):
    """
    CertificateInfo
    """ # noqa: E501
    status: Optional[CertificateStatus] = None
    domain_name: Optional[StrictStr] = Field(default=None, serialization_alias="domainName")
    serial_number: Optional[StrictStr] = Field(default=None, serialization_alias="serialNumber")
    not_before: Optional[StrictInt] = Field(default=None, serialization_alias="notBefore")
    not_after: Optional[StrictInt] = Field(default=None, serialization_alias="notAfter")
    requested_at: Optional[StrictInt] = Field(default=None, serialization_alias="requestedAt")
    issued_at: Optional[StrictInt] = Field(default=None, serialization_alias="issuedAt")
    acme_certificate_id: Optional[AcmeCertificateId] = Field(default=None, serialization_alias="acmeCertificateId")
    __properties: ClassVar[List[str]] = ["status", "domainName", "serialNumber", "notBefore", "notAfter", "requestedAt", "issuedAt", "acmeCertificateId"]

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
        """Create an instance of CertificateInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of acme_certificate_id
        if self.acme_certificate_id:
            _dict['acmeCertificateId'] = self.acme_certificate_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CertificateInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "domain_name": obj.get("domainName"),
            "serial_number": obj.get("serialNumber"),
            "not_before": obj.get("notBefore"),
            "not_after": obj.get("notAfter"),
            "requested_at": obj.get("requestedAt"),
            "issued_at": obj.get("issuedAt"),
            "acme_certificate_id": AcmeCertificateId.from_dict(obj["acmeCertificateId"]) if obj.get("acmeCertificateId") is not None else None
        })
        return _obj


