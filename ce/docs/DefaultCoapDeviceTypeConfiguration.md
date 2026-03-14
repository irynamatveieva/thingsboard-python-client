
# DefaultCoapDeviceTypeConfiguration

`tb_ce_client.models.DefaultCoapDeviceTypeConfiguration`

**Extends:** **CoapDeviceTypeConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **transport_payload_type_configuration** | [**TransportPayloadTypeConfiguration**](TransportPayloadTypeConfiguration.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.transport_payload_type_configuration`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DefaultCoapDeviceTypeConfiguration.model_validate(data)` or `DefaultCoapDeviceTypeConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

