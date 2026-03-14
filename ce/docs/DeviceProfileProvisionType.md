
# DeviceProfileProvisionType

`tb_ce_client.models.DeviceProfileProvisionType`

## Enum Values


* `DISABLED` (value: `'DISABLED'`)

* `ALLOW_CREATE_NEW_DEVICES` (value: `'ALLOW_CREATE_NEW_DEVICES'`)

* `CHECK_PRE_PROVISIONED_DEVICES` (value: `'CHECK_PRE_PROVISIONED_DEVICES'`)

* `X509_CERTIFICATE_CHAIN` (value: `'X509_CERTIFICATE_CHAIN'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceProfileProvisionType.model_validate(data)` or `DeviceProfileProvisionType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

