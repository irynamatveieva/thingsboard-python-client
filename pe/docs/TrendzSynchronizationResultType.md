
# TrendzSynchronizationResultType

`tb_pe_client.models.TrendzSynchronizationResultType`

## Enum Values


* `SYNC_NOT_INITIALIZED` (value: `'SYNC_NOT_INITIALIZED'`)

* `SYNC_COMPLETED` (value: `'SYNC_COMPLETED'`)

* `SYNC_DISABLED` (value: `'SYNC_DISABLED'`)

* `TRENDZ_UNSUPPORTED_VERSION` (value: `'TRENDZ_UNSUPPORTED_VERSION'`)

* `TRENDZ_AUTH_INVALID` (value: `'TRENDZ_AUTH_INVALID'`)

* `TRENDZ_URL_UNREACHABLE` (value: `'TRENDZ_URL_UNREACHABLE'`)

* `TB_URL_MISMATCH` (value: `'TB_URL_MISMATCH'`)

* `TB_URL_UNREACHABLE` (value: `'TB_URL_UNREACHABLE'`)

* `TB_AUTH_INVALID` (value: `'TB_AUTH_INVALID'`)

* `SYNC_INTERNAL_ERROR` (value: `'SYNC_INTERNAL_ERROR'`)



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TrendzSynchronizationResultType.model_validate(data)` or `TrendzSynchronizationResultType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

