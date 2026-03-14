
# Discount

`tb_paas_client.models.Discount`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **coupon_code** | **str** |  | [optional] |
| **coupon_valid** | **bool** |  | [optional] |
| **amount_off** | **int** |  | [optional] |
| **percent_off** | **float** |  | [optional] |
| **coupon_id** | [**CouponId**](CouponId.md) |  | [optional] |
| **duration** | [**CouponDuration**](CouponDuration.md) |  | [optional] |
| **duration_in_months** | **int** |  | [optional] |
| **end_date** | **int** |  | [optional] |
| **package** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.coupon_code`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Discount.model_validate(data)` or `Discount.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

