
# CoapDeviceProfileTransportConfiguration

`tb_paas_client.models.CoapDeviceProfileTransportConfiguration`

**Extends:** **DeviceProfileTransportConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **coap_device_type_configuration** | [**CoapDeviceTypeConfiguration**](CoapDeviceTypeConfiguration.md) |  | [optional] |
| **client_settings** | [**PowerSavingConfiguration**](PowerSavingConfiguration.md) |  | [optional] |



## Referenced Types

#### DeviceProfileTransportConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### CoapDeviceTypeConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| coap_device_type | str |  |  |

#### PowerSavingConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| power_mode | PowerMode |  | [optional] |
| psm_activity_timer | int |  | [optional] |
| edrx_cycle | int |  | [optional] |
| paging_transmission_window | int |  | [optional] |

#### PowerMode (enum)
`PSM` | `DRX` | `E_DRX`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.coap_device_type_configuration`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CoapDeviceProfileTransportConfiguration.model_validate(data)` or `CoapDeviceProfileTransportConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

