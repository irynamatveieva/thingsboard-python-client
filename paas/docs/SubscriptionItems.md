
# SubscriptionItems

`tb_paas_client.models.SubscriptionItems`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **extra_device_pack_count** | **int** |  | [optional] |
| **extra_customer_pack_count** | **int** |  | [optional] |
| **extra_integration_pack_count** | **int** |  | [optional] |
| **extra_calculated_field_count** | **int** |  | [optional] |
| **traffic_pack_count** | **int** |  | [optional] |
| **compute_pack_count** | **int** |  | [optional] |
| **storage_pack_count** | **int** |  | [optional] |
| **alarm_pack_count** | **int** |  | [optional] |
| **email_pack_count** | **int** |  | [optional] |
| **sms_pack_count** | **int** |  | [optional] |
| **ai_credits_pack_count** | **int** |  | [optional] |
| **edge_enabled** | **bool** |  | [optional] |
| **extra_edge_count** | **int** |  | [optional] |
| **trendz_enabled** | **bool** |  | [optional] |
| **white_labeling_addon_enabled** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.extra_device_pack_count`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SubscriptionItems.model_validate(data)` or `SubscriptionItems.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

