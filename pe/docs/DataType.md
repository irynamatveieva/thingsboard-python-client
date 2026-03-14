
# DataType

`tb_pe_client.models.DataType`

## Enum Values


* `BOOLEAN` (value: `'BOOLEAN'`)

* `LONG` (value: `'LONG'`)

* `DOUBLE` (value: `'DOUBLE'`)

* `STRING` (value: `'STRING'`)

* `JSON` (value: `'JSON'`)



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DataType.model_validate(data)` or `DataType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

