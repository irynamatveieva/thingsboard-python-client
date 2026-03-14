
# SubmitStrategyType

`tb_ce_client.models.SubmitStrategyType`

## Enum Values


* `BURST` (value: `'BURST'`)

* `BATCH` (value: `'BATCH'`)

* `SEQUENTIAL_BY_ORIGINATOR` (value: `'SEQUENTIAL_BY_ORIGINATOR'`)

* `SEQUENTIAL_BY_TENANT` (value: `'SEQUENTIAL_BY_TENANT'`)

* `SEQUENTIAL` (value: `'SEQUENTIAL'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SubmitStrategyType.model_validate(data)` or `SubmitStrategyType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

