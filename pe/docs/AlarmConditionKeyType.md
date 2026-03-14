
# AlarmConditionKeyType

`tb_pe_client.models.AlarmConditionKeyType`

## Enum Values


* `ATTRIBUTE` (value: `'ATTRIBUTE'`)

* `TIME_SERIES` (value: `'TIME_SERIES'`)

* `ENTITY_FIELD` (value: `'ENTITY_FIELD'`)

* `CONSTANT` (value: `'CONSTANT'`)



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmConditionKeyType.model_validate(data)` or `AlarmConditionKeyType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

