
# DeviceProfileProvisionConfiguration

`tb_ce_client.models.DeviceProfileProvisionConfiguration`

Device profile provision configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **provision_device_secret** | **str** | Provision device secret | [optional] |
| **type** | **str** |  | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.provision_device_secret`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceProfileProvisionConfiguration.model_validate(data)` or `DeviceProfileProvisionConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

