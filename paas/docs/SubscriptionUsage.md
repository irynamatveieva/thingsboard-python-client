
# SubscriptionUsage

`tb_paas_client.models.SubscriptionUsage`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **devices** | **int** |  | [optional] |
| **assets** | **int** |  | [optional] |
| **customers** | **int** |  | [optional] |
| **users** | **int** |  | [optional] |
| **dashboards** | **int** |  | [optional] |
| **rule_chains** | **int** |  | [optional] |
| **integrations** | **int** |  | [optional] |
| **converters** | **int** |  | [optional] |
| **scheduler_events** | **int** |  | [optional] |
| **edges** | **int** |  | [optional] |
| **transport_messages** | **int** |  | [optional] |
| **transport_data_points** | **int** |  | [optional] |
| **re_executions** | **int** |  | [optional] |
| **js_executions** | **int** |  | [optional] |
| **dp_storage_days** | **int** |  | [optional] |
| **emails** | **int** |  | [optional] |
| **sms** | **int** |  | [optional] |
| **alarms** | **int** |  | [optional] |
| **reports** | **int** |  | [optional] |
| **ai_credits** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.devices`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SubscriptionUsage.model_validate(data)` or `SubscriptionUsage.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

