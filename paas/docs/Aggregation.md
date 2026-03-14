
# Aggregation

`tb_paas_client.models.Aggregation`

## Enum Values


* `MIN` (value: `'MIN'`)

* `MAX` (value: `'MAX'`)

* `AVG` (value: `'AVG'`)

* `SUM` (value: `'SUM'`)

* `COUNT` (value: `'COUNT'`)

* `NONE` (value: `'NONE'`)



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Aggregation.model_validate(data)` or `Aggregation.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

