
# EntityKeyType

`tb_paas_client.models.EntityKeyType`

## Enum Values


* `ATTRIBUTE` (value: `'ATTRIBUTE'`)

* `CLIENT_ATTRIBUTE` (value: `'CLIENT_ATTRIBUTE'`)

* `SHARED_ATTRIBUTE` (value: `'SHARED_ATTRIBUTE'`)

* `SERVER_ATTRIBUTE` (value: `'SERVER_ATTRIBUTE'`)

* `TIME_SERIES` (value: `'TIME_SERIES'`)

* `ENTITY_FIELD` (value: `'ENTITY_FIELD'`)

* `ALARM_FIELD` (value: `'ALARM_FIELD'`)



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityKeyType.model_validate(data)` or `EntityKeyType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

