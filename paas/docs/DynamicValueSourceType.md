
# DynamicValueSourceType

`tb_paas_client.models.DynamicValueSourceType`

## Enum Values


* `CURRENT_TENANT` (value: `'CURRENT_TENANT'`)

* `CURRENT_CUSTOMER` (value: `'CURRENT_CUSTOMER'`)

* `CURRENT_USER` (value: `'CURRENT_USER'`)

* `CURRENT_DEVICE` (value: `'CURRENT_DEVICE'`)



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DynamicValueSourceType.model_validate(data)` or `DynamicValueSourceType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

