
# AlarmStatus

`tb_ce_client.models.AlarmStatus`

## Enum Values


* `ACTIVE_UNACK` (value: `'ACTIVE_UNACK'`)

* `ACTIVE_ACK` (value: `'ACTIVE_ACK'`)

* `CLEARED_UNACK` (value: `'CLEARED_UNACK'`)

* `CLEARED_ACK` (value: `'CLEARED_ACK'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmStatus.model_validate(data)` or `AlarmStatus.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

