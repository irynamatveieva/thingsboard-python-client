
# UserEmailInfo

`tb_pe_client.models.UserEmailInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**UserId**](UserId.md) | User id | [optional] |
| **email** | **str** | User email | [optional] |
| **first_name** | **str** | User first name | [optional] |
| **last_name** | **str** | User last name | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `UserEmailInfo.model_validate(data)` or `UserEmailInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

