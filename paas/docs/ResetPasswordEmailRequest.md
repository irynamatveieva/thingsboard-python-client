
# ResetPasswordEmailRequest

`tb_paas_client.models.ResetPasswordEmailRequest`

The JSON object representing the reset password email request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **email** | **str** | The email of the user | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.email`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ResetPasswordEmailRequest.model_validate(data)` or `ResetPasswordEmailRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

