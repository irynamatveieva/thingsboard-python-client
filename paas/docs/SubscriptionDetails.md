
# SubscriptionDetails

`tb_paas_client.models.SubscriptionDetails`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**SubscriptionId**](SubscriptionId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **external_id** | **str** |  | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **billing_customer_id** | [**BillingCustomerId**](BillingCustomerId.md) |  | [optional] |
| **subscription_plan_id** | [**SubscriptionPlanId**](SubscriptionPlanId.md) |  | [optional] |
| **current_period_start_ts** | **int** |  | [optional] |
| **current_period_end_ts** | **int** |  | [optional] |
| **active** | **bool** |  | [optional] |
| **trial** | **bool** |  | [optional] |
| **trial_end_ts** | **int** |  | [optional] |
| **status** | **str** |  | [optional] |
| **last_paid** | **bool** |  | [optional] |
| **upcoming_invoice_date** | **int** |  | [optional] |
| **upcoming_invoice_amount_due** | **int** |  | [optional] |
| **coupon_id** | [**CouponId**](CouponId.md) |  | [optional] |
| **discount_end_date** | **int** |  | [optional] |
| **subscription_plan_name** | **str** |  | [optional] |
| **plan_has_addons** | **bool** |  | [optional] |
| **plan_ui_type** | **str** |  | [optional] |
| **plan_is_free** | **bool** |  | [optional] |
| **plan_is_active** | **bool** |  | [optional] |
| **edge_count_included** | **int** |  | [optional] |
| **items** | [**SubscriptionItems**](SubscriptionItems.md) |  | [optional] |
| **discount** | [**Discount**](Discount.md) |  | [optional] |
| **name** | **str** |  | [optional] [readonly] |
| **additional_info** | **object** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SubscriptionDetails.model_validate(data)` or `SubscriptionDetails.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

