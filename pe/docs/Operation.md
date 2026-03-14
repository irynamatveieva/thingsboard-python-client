
# Operation

`tb_pe_client.models.Operation`

## Enum Values


* `ALL` (value: `'ALL'`)

* `CREATE` (value: `'CREATE'`)

* `READ` (value: `'READ'`)

* `WRITE` (value: `'WRITE'`)

* `DELETE` (value: `'DELETE'`)

* `RPC_CALL` (value: `'RPC_CALL'`)

* `READ_CREDENTIALS` (value: `'READ_CREDENTIALS'`)

* `WRITE_CREDENTIALS` (value: `'WRITE_CREDENTIALS'`)

* `READ_ATTRIBUTES` (value: `'READ_ATTRIBUTES'`)

* `WRITE_ATTRIBUTES` (value: `'WRITE_ATTRIBUTES'`)

* `READ_TELEMETRY` (value: `'READ_TELEMETRY'`)

* `WRITE_TELEMETRY` (value: `'WRITE_TELEMETRY'`)

* `ADD_TO_GROUP` (value: `'ADD_TO_GROUP'`)

* `REMOVE_FROM_GROUP` (value: `'REMOVE_FROM_GROUP'`)

* `CHANGE_OWNER` (value: `'CHANGE_OWNER'`)

* `IMPERSONATE` (value: `'IMPERSONATE'`)

* `CLAIM_DEVICES` (value: `'CLAIM_DEVICES'`)

* `SHARE_GROUP` (value: `'SHARE_GROUP'`)

* `ASSIGN_TO_TENANT` (value: `'ASSIGN_TO_TENANT'`)

* `READ_CALCULATED_FIELD` (value: `'READ_CALCULATED_FIELD'`)

* `WRITE_CALCULATED_FIELD` (value: `'WRITE_CALCULATED_FIELD'`)



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Operation.model_validate(data)` or `Operation.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

