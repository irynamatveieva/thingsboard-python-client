
# LoginRequest

`tb_paas_client.models.LoginRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **password** | **str** | User password | |
| **username** | **str** | User email | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.password`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LoginRequest.model_validate(data)` or `LoginRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

