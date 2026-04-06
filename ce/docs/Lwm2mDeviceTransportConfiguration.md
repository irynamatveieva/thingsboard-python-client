
# Lwm2mDeviceTransportConfiguration

`tb_ce_client.models.Lwm2mDeviceTransportConfiguration`

**Extends:** **DeviceTransportConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **power_mode** | [**PowerMode**](PowerMode.md) |  | [optional] |
| **psm_activity_timer** | **int** |  | [optional] |
| **edrx_cycle** | **int** |  | [optional] |
| **paging_transmission_window** | **int** |  | [optional] |



## Referenced Types

#### DeviceTransportConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### PowerMode (enum)
`PSM` | `DRX` | `E_DRX`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.power_mode`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Lwm2mDeviceTransportConfiguration.model_validate(data)` or `Lwm2mDeviceTransportConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

