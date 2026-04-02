
# DeviceConfiguration

`tb_pe_client.models.DeviceConfiguration`

Device configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**DeviceProfileType**](DeviceProfileType.md) | Device profile type | |



## Subtypes

#### DefaultDeviceConfiguration  *(type=`DEFAULT`)*
*(no additional properties)*

## Referenced Types

#### DeviceProfileType (enum)
`DEFAULT`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceConfiguration.model_validate(data)` or `DeviceConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

