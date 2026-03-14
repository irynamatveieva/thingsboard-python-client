
# ChangePasswordRequest

`tb_ce_client.models.ChangePasswordRequest`

Change Password Request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **current_password** | **str** | The old password | [optional] |
| **new_password** | **str** | The new password | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.current_password`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ChangePasswordRequest.model_validate(data)` or `ChangePasswordRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

