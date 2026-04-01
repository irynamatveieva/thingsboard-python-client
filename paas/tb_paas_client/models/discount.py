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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_paas_client.models.coupon_duration import CouponDuration
from tb_paas_client.models.coupon_id import CouponId
from typing import Optional, Set
from typing_extensions import Self

class Discount(BaseModel):
    """
    Discount
    """ # noqa: E501
    coupon_code: Optional[StrictStr] = Field(default=None, serialization_alias="couponCode")
    coupon_valid: Optional[StrictBool] = Field(default=None, serialization_alias="couponValid")
    amount_off: Optional[StrictInt] = Field(default=None, serialization_alias="amountOff")
    percent_off: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, serialization_alias="percentOff")
    coupon_id: Optional[CouponId] = Field(default=None, serialization_alias="couponId")
    duration: Optional[CouponDuration] = None
    duration_in_months: Optional[StrictInt] = Field(default=None, serialization_alias="durationInMonths")
    end_date: Optional[StrictInt] = Field(default=None, serialization_alias="endDate")
    package: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["couponCode", "couponValid", "amountOff", "percentOff", "couponId", "duration", "durationInMonths", "endDate", "package"]

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
        """Create an instance of Discount from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of coupon_id
        if self.coupon_id:
            _dict['couponId'] = self.coupon_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Discount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "coupon_code": obj.get("couponCode"),
            "coupon_valid": obj.get("couponValid"),
            "amount_off": obj.get("amountOff"),
            "percent_off": obj.get("percentOff"),
            "coupon_id": CouponId.from_dict(obj["couponId"]) if obj.get("couponId") is not None else None,
            "duration": obj.get("duration"),
            "duration_in_months": obj.get("durationInMonths"),
            "end_date": obj.get("endDate"),
            "package": obj.get("package")
        })
        return _obj


