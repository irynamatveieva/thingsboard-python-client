
# JobStatus

`tb_paas_client.models.JobStatus`

## Enum Values


* `QUEUED` (value: `'QUEUED'`)

* `PENDING` (value: `'PENDING'`)

* `RUNNING` (value: `'RUNNING'`)

* `COMPLETED` (value: `'COMPLETED'`)

* `FAILED` (value: `'FAILED'`)

* `CANCELLED` (value: `'CANCELLED'`)



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `JobStatus.model_validate(data)` or `JobStatus.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

