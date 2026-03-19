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
from tb_paas_client.models.billing_customer_id import BillingCustomerId
from tb_paas_client.models.coupon_id import CouponId
from tb_paas_client.models.discount import Discount
from tb_paas_client.models.subscription_id import SubscriptionId
from tb_paas_client.models.subscription_items import SubscriptionItems
from tb_paas_client.models.subscription_plan_id import SubscriptionPlanId
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionDetails(BaseModel):
    """
    SubscriptionDetails
    """ # noqa: E501
    id: Optional[SubscriptionId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", alias="createdTime")
    additional_info: Optional[Any] = Field(default=None, alias="additionalInfo")
    external_id: Optional[StrictStr] = Field(default=None, alias="externalId")
    tenant_id: Optional[TenantId] = Field(default=None, alias="tenantId")
    billing_customer_id: Optional[BillingCustomerId] = Field(default=None, alias="billingCustomerId")
    subscription_plan_id: Optional[SubscriptionPlanId] = Field(default=None, alias="subscriptionPlanId")
    current_period_start_ts: Optional[StrictInt] = Field(default=None, alias="currentPeriodStartTs")
    current_period_end_ts: Optional[StrictInt] = Field(default=None, alias="currentPeriodEndTs")
    active: Optional[StrictBool] = None
    trial: Optional[StrictBool] = None
    trial_end_ts: Optional[StrictInt] = Field(default=None, alias="trialEndTs")
    status: Optional[StrictStr] = None
    last_paid: Optional[StrictBool] = Field(default=None, alias="lastPaid")
    upcoming_invoice_date: Optional[StrictInt] = Field(default=None, alias="upcomingInvoiceDate")
    upcoming_invoice_amount_due: Optional[StrictInt] = Field(default=None, alias="upcomingInvoiceAmountDue")
    coupon_id: Optional[CouponId] = Field(default=None, alias="couponId")
    discount_end_date: Optional[StrictInt] = Field(default=None, alias="discountEndDate")
    subscription_plan_name: Optional[StrictStr] = Field(default=None, alias="subscriptionPlanName")
    plan_has_addons: Optional[StrictBool] = Field(default=None, alias="planHasAddons")
    plan_ui_type: Optional[StrictStr] = Field(default=None, alias="planUiType")
    plan_is_free: Optional[StrictBool] = Field(default=None, alias="planIsFree")
    plan_is_active: Optional[StrictBool] = Field(default=None, alias="planIsActive")
    edge_count_included: Optional[StrictInt] = Field(default=None, alias="edgeCountIncluded")
    items: Optional[SubscriptionItems] = None
    discount: Optional[Discount] = None
    name: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "createdTime", "additionalInfo", "externalId", "tenantId", "billingCustomerId", "subscriptionPlanId", "currentPeriodStartTs", "currentPeriodEndTs", "active", "trial", "trialEndTs", "status", "lastPaid", "upcomingInvoiceDate", "upcomingInvoiceAmountDue", "couponId", "discountEndDate", "subscriptionPlanName", "planHasAddons", "planUiType", "planIsFree", "planIsActive", "edgeCountIncluded", "items", "discount", "name"]

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
        """Create an instance of SubscriptionDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billing_customer_id
        if self.billing_customer_id:
            _dict['billingCustomerId'] = self.billing_customer_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subscription_plan_id
        if self.subscription_plan_id:
            _dict['subscriptionPlanId'] = self.subscription_plan_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of coupon_id
        if self.coupon_id:
            _dict['couponId'] = self.coupon_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of items
        if self.items:
            _dict['items'] = self.items.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount
        if self.discount:
            _dict['discount'] = self.discount.to_dict()
        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": SubscriptionId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdTime": obj.get("createdTime"),
            "additionalInfo": obj.get("additionalInfo"),
            "externalId": obj.get("externalId"),
            "tenantId": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "billingCustomerId": BillingCustomerId.from_dict(obj["billingCustomerId"]) if obj.get("billingCustomerId") is not None else None,
            "subscriptionPlanId": SubscriptionPlanId.from_dict(obj["subscriptionPlanId"]) if obj.get("subscriptionPlanId") is not None else None,
            "currentPeriodStartTs": obj.get("currentPeriodStartTs"),
            "currentPeriodEndTs": obj.get("currentPeriodEndTs"),
            "active": obj.get("active"),
            "trial": obj.get("trial"),
            "trialEndTs": obj.get("trialEndTs"),
            "status": obj.get("status"),
            "lastPaid": obj.get("lastPaid"),
            "upcomingInvoiceDate": obj.get("upcomingInvoiceDate"),
            "upcomingInvoiceAmountDue": obj.get("upcomingInvoiceAmountDue"),
            "couponId": CouponId.from_dict(obj["couponId"]) if obj.get("couponId") is not None else None,
            "discountEndDate": obj.get("discountEndDate"),
            "subscriptionPlanName": obj.get("subscriptionPlanName"),
            "planHasAddons": obj.get("planHasAddons"),
            "planUiType": obj.get("planUiType"),
            "planIsFree": obj.get("planIsFree"),
            "planIsActive": obj.get("planIsActive"),
            "edgeCountIncluded": obj.get("edgeCountIncluded"),
            "items": SubscriptionItems.from_dict(obj["items"]) if obj.get("items") is not None else None,
            "discount": Discount.from_dict(obj["discount"]) if obj.get("discount") is not None else None,
            "name": obj.get("name")
        })
        return _obj


