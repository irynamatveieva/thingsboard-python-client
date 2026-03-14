
# ActivateUserRequest

`tb_paas_client.models.ActivateUserRequest`

Activate user request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **activate_token** | **str** | The activate token to verify | [optional] |
| **password** | **str** | The new password to set | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.activate_token`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ActivateUserRequest.model_validate(data)` or `ActivateUserRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

