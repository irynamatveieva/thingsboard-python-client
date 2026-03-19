
# Login401Response

`tb_pe_client.models.Login401Response`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **error_code** | [**ThingsboardErrorCode**](ThingsboardErrorCode.md) |  | [optional] |
| **message** | **str** | Error message | [optional] [readonly] |
| **status** | **int** | HTTP Response Status Code | [optional] [readonly] |
| **timestamp** | **int** | Timestamp | [optional] [readonly] |
| **reset_token** | **str** | Password reset token | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.error_code`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Login401Response.model_validate(data)` or `Login401Response.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

