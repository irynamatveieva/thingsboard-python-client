
# SnmpCommunicationSpec

`tb_ce_client.models.SnmpCommunicationSpec`

## Enum Values


* `TELEMETRY_QUERYING` (value: `'TELEMETRY_QUERYING'`)

* `CLIENT_ATTRIBUTES_QUERYING` (value: `'CLIENT_ATTRIBUTES_QUERYING'`)

* `SHARED_ATTRIBUTES_SETTING` (value: `'SHARED_ATTRIBUTES_SETTING'`)

* `TO_DEVICE_RPC_REQUEST` (value: `'TO_DEVICE_RPC_REQUEST'`)

* `TO_SERVER_RPC_REQUEST` (value: `'TO_SERVER_RPC_REQUEST'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SnmpCommunicationSpec.model_validate(data)` or `SnmpCommunicationSpec.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

