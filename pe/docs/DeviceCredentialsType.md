
# DeviceCredentialsType

`tb_pe_client.models.DeviceCredentialsType`

## Enum Values


* `ACCESS_TOKEN` (value: `'ACCESS_TOKEN'`)

* `X509_CERTIFICATE` (value: `'X509_CERTIFICATE'`)

* `MQTT_BASIC` (value: `'MQTT_BASIC'`)

* `LWM2_M_CREDENTIALS` (value: `'LWM2M_CREDENTIALS'`)



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceCredentialsType.model_validate(data)` or `DeviceCredentialsType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

