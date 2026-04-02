
# ThingsboardErrorResponse

`tb_paas_client.models.ThingsboardErrorResponse`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **error_code** | [**ThingsboardErrorCode**](ThingsboardErrorCode.md) |  | [optional] |
| **message** | **str** | Error message | [optional] [readonly] |
| **status** | **int** | HTTP Response Status Code | [optional] [readonly] |
| **subscription_entry** | [**SubscriptionEntry**](SubscriptionEntry.md) |  | [optional] |
| **subscription_error_code** | [**SubscriptionExceptionErrorCode**](SubscriptionExceptionErrorCode.md) |  | [optional] |
| **subscription_value** | **object** |  | [optional] |
| **timestamp** | **int** | Timestamp | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.error_code`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ThingsboardErrorResponse.model_validate(data)` or `ThingsboardErrorResponse.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

