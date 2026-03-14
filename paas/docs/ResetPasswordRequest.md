
# ResetPasswordRequest

`tb_paas_client.models.ResetPasswordRequest`

Reset password request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **reset_token** | **str** | The reset token to verify | [optional] |
| **password** | **str** | The new password to set | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.reset_token`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ResetPasswordRequest.model_validate(data)` or `ResetPasswordRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

