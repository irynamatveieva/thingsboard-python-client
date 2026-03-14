
# RpcStatus

`tb_paas_client.models.RpcStatus`

## Enum Values


* `QUEUED` (value: `'QUEUED'`)

* `SENT` (value: `'SENT'`)

* `DELIVERED` (value: `'DELIVERED'`)

* `SUCCESSFUL` (value: `'SUCCESSFUL'`)

* `TIMEOUT` (value: `'TIMEOUT'`)

* `EXPIRED` (value: `'EXPIRED'`)

* `FAILED` (value: `'FAILED'`)

* `DELETED` (value: `'DELETED'`)



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RpcStatus.model_validate(data)` or `RpcStatus.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

