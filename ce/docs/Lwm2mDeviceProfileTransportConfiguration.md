
# Lwm2mDeviceProfileTransportConfiguration

`tb_ce_client.models.Lwm2mDeviceProfileTransportConfiguration`

**Extends:** **DeviceProfileTransportConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **observe_attr** | [**TelemetryMappingConfiguration**](TelemetryMappingConfiguration.md) | Configuration for mapping LwM2M resources to telemetry and attributes | [optional] |
| **bootstrap_server_update_enable** | **bool** | Flag indicating whether LwM2M bootstrap server update is enabled | [optional] |
| **bootstrap** | [**List[LwM2MBootstrapServerCredential]**](LwM2MBootstrapServerCredential.md) |  | [optional] |
| **client_lw_m2m_settings** | [**OtherConfiguration**](OtherConfiguration.md) | Other LwM2M client settings | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.observe_attr`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Lwm2mDeviceProfileTransportConfiguration.model_validate(data)` or `Lwm2mDeviceProfileTransportConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

