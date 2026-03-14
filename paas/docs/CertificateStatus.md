
# CertificateStatus

`tb_paas_client.models.CertificateStatus`

## Enum Values


* `PENDING_VALIDATION` (value: `'PENDING_VALIDATION'`)

* `ISSUED` (value: `'ISSUED'`)

* `INACTIVE` (value: `'INACTIVE'`)

* `EXPIRED` (value: `'EXPIRED'`)

* `VALIDATION_TIMED_OUT` (value: `'VALIDATION_TIMED_OUT'`)

* `REVOKED` (value: `'REVOKED'`)

* `FAILED` (value: `'FAILED'`)

* `UNKNOWN` (value: `'UNKNOWN'`)



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CertificateStatus.model_validate(data)` or `CertificateStatus.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

