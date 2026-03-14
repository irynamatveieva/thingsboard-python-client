
# SnmpDeviceProfileTransportConfiguration

`tb_paas_client.models.SnmpDeviceProfileTransportConfiguration`

**Extends:** **DeviceProfileTransportConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **timeout_ms** | **int** |  | [optional] |
| **retries** | **int** |  | [optional] |
| **communication_configs** | [**List[SnmpCommunicationConfig]**](SnmpCommunicationConfig.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.timeout_ms`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SnmpDeviceProfileTransportConfiguration.model_validate(data)` or `SnmpDeviceProfileTransportConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

