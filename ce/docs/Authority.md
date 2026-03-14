
# Authority

`tb_ce_client.models.Authority`

## Enum Values


* `SYS_ADMIN` (value: `'SYS_ADMIN'`)

* `TENANT_ADMIN` (value: `'TENANT_ADMIN'`)

* `CUSTOMER_USER` (value: `'CUSTOMER_USER'`)

* `REFRESH_TOKEN` (value: `'REFRESH_TOKEN'`)

* `PRE_VERIFICATION_TOKEN` (value: `'PRE_VERIFICATION_TOKEN'`)

* `MFA_CONFIGURATION_TOKEN` (value: `'MFA_CONFIGURATION_TOKEN'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Authority.model_validate(data)` or `Authority.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

