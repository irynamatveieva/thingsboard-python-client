
# LoginRequest

`tb_pe_client.models.LoginRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **username** | **str** | User email | |
| **password** | **str** | User password | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.username`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LoginRequest.model_validate(data)` or `LoginRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

