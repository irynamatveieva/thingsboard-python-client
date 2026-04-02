
# DeviceData

`tb_paas_client.models.DeviceData`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **configuration** | [**DeviceConfiguration**](DeviceConfiguration.md) | Device configuration for device profile type. DEFAULT is only supported value for now | [optional] |
| **transport_configuration** | [**DeviceTransportConfiguration**](DeviceTransportConfiguration.md) | Device transport configuration used to connect the device | [optional] |



## Referenced Types

#### DeviceConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | DeviceProfileType | Device profile type |  |

#### DeviceTransportConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### DeviceProfileType (enum)
`DEFAULT`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.configuration`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceData.model_validate(data)` or `DeviceData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

