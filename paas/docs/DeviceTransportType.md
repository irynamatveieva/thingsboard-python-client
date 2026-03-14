
# DeviceTransportType

`tb_paas_client.models.DeviceTransportType`

## Enum Values


* `DEFAULT` (value: `'DEFAULT'`)

* `MQTT` (value: `'MQTT'`)

* `COAP` (value: `'COAP'`)

* `LWM2M` (value: `'LWM2M'`)

* `SNMP` (value: `'SNMP'`)



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceTransportType.model_validate(data)` or `DeviceTransportType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

