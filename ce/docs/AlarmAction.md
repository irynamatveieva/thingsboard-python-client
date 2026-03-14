
# AlarmAction

`tb_ce_client.models.AlarmAction`

## Enum Values


* `CREATED` (value: `'CREATED'`)

* `SEVERITY_CHANGED` (value: `'SEVERITY_CHANGED'`)

* `ACKNOWLEDGED` (value: `'ACKNOWLEDGED'`)

* `CLEARED` (value: `'CLEARED'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmAction.model_validate(data)` or `AlarmAction.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

