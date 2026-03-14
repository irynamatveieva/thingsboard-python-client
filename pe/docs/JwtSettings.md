
# JwtSettings

`tb_pe_client.models.JwtSettings`

A JSON value representing the JWT Settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **token_expiration_time** | **int** | The JWT will expire after seconds. | [optional] |
| **refresh_token_exp_time** | **int** | The JWT can be refreshed during seconds. | [optional] |
| **token_issuer** | **str** | The JWT issuer. | [optional] |
| **token_signing_key** | **str** | The JWT key is used to sing token. Base64 encoded. | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.token_expiration_time`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `JwtSettings.model_validate(data)` or `JwtSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

