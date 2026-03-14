
# SaveDeviceWithCredentialsRequest

`tb_paas_client.models.SaveDeviceWithCredentialsRequest`

The JSON object with device and credentials. See method description above for example.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **device** | [**Device**](Device.md) | The JSON with device entity. | |
| **credentials** | [**DeviceCredentials**](DeviceCredentials.md) | The JSON with credentials entity. | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.device`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SaveDeviceWithCredentialsRequest.model_validate(data)` or `SaveDeviceWithCredentialsRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

