
# EventType

`tb_ce_client.models.EventType`

## Enum Values


* `ERROR` (value: `'ERROR'`)

* `LC_EVENT` (value: `'LC_EVENT'`)

* `STATS` (value: `'STATS'`)

* `DEBUG_RULE_NODE` (value: `'DEBUG_RULE_NODE'`)

* `DEBUG_RULE_CHAIN` (value: `'DEBUG_RULE_CHAIN'`)

* `DEBUG_CALCULATED_FIELD` (value: `'DEBUG_CALCULATED_FIELD'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EventType.model_validate(data)` or `EventType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

