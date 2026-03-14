
# CalculatedFieldType

`tb_pe_client.models.CalculatedFieldType`

## Enum Values


* `SIMPLE` (value: `'SIMPLE'`)

* `SCRIPT` (value: `'SCRIPT'`)

* `GEOFENCING` (value: `'GEOFENCING'`)

* `ALARM` (value: `'ALARM'`)

* `PROPAGATION` (value: `'PROPAGATION'`)

* `RELATED_ENTITIES_AGGREGATION` (value: `'RELATED_ENTITIES_AGGREGATION'`)

* `ENTITY_AGGREGATION` (value: `'ENTITY_AGGREGATION'`)



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CalculatedFieldType.model_validate(data)` or `CalculatedFieldType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

