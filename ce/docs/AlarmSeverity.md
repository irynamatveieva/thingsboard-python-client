
# AlarmSeverity

`tb_ce_client.models.AlarmSeverity`

## Enum Values


* `CRITICAL` (value: `'CRITICAL'`)

* `MAJOR` (value: `'MAJOR'`)

* `MINOR` (value: `'MINOR'`)

* `WARNING` (value: `'WARNING'`)

* `INDETERMINATE` (value: `'INDETERMINATE'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmSeverity.model_validate(data)` or `AlarmSeverity.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

