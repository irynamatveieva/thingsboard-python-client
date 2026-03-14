
# TwoFaProviderType

`tb_ce_client.models.TwoFaProviderType`

## Enum Values


* `TOTP` (value: `'TOTP'`)

* `SMS` (value: `'SMS'`)

* `EMAIL` (value: `'EMAIL'`)

* `BACKUP_CODE` (value: `'BACKUP_CODE'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TwoFaProviderType.model_validate(data)` or `TwoFaProviderType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

