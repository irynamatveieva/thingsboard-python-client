
# DeviceProfileData

`tb_paas_client.models.DeviceProfileData`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **configuration** | [**DeviceProfileConfiguration**](DeviceProfileConfiguration.md) | JSON object of device profile configuration | [optional] |
| **transport_configuration** | [**DeviceProfileTransportConfiguration**](DeviceProfileTransportConfiguration.md) | JSON object of device profile transport configuration | [optional] |
| **provision_configuration** | [**DeviceProfileProvisionConfiguration**](DeviceProfileProvisionConfiguration.md) | JSON object of provisioning strategy type per device profile | [optional] |
| **alarms** | [**List[DeviceProfileAlarm]**](DeviceProfileAlarm.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.configuration`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceProfileData.model_validate(data)` or `DeviceProfileData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

