
# LoginResponse

`tb_ce_client.models.LoginResponse`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **token** | **str** | JWT token | |
| **refresh_token** | **str** | Refresh token | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.token`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LoginResponse.model_validate(data)` or `LoginResponse.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

