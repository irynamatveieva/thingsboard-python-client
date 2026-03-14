
# AliasEntityType

`tb_ce_client.models.AliasEntityType`

## Enum Values


* `CURRENT_CUSTOMER` (value: `'CURRENT_CUSTOMER'`)

* `CURRENT_TENANT` (value: `'CURRENT_TENANT'`)

* `CURRENT_USER` (value: `'CURRENT_USER'`)

* `CURRENT_USER_OWNER` (value: `'CURRENT_USER_OWNER'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AliasEntityType.model_validate(data)` or `AliasEntityType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

