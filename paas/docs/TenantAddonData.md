
# TenantAddonData

`tb_paas_client.models.TenantAddonData`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **max_devices** | **int** |  | [optional] |
| **max_assets** | **int** |  | [optional] |
| **max_customers** | **int** |  | [optional] |
| **max_users** | **int** |  | [optional] |
| **max_integrations** | **int** |  | [optional] |
| **max_converters** | **int** |  | [optional] |
| **max_calculated_fields_per_entity** | **int** |  | [optional] |
| **max_transport_messages** | **int** |  | [optional] |
| **max_transport_data_points** | **int** |  | [optional] |
| **max_re_executions** | **int** |  | [optional] |
| **max_js_executions** | **int** |  | [optional] |
| **max_dp_storage_days** | **int** |  | [optional] |
| **max_created_alarms** | **int** |  | [optional] |
| **max_emails** | **int** |  | [optional] |
| **max_sms** | **int** |  | [optional] |
| **max_ai_credits** | **int** |  | [optional] |
| **edge_enabled** | **bool** |  | [optional] |
| **max_edges** | **int** |  | [optional] |
| **trendz_enabled** | **bool** |  | [optional] |
| **white_labeling_enabled** | **bool** |  | [optional] |
| **default** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.max_devices`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TenantAddonData.model_validate(data)` or `TenantAddonData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

