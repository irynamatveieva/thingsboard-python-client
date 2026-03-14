
# DeviceCredentials

`tb_ce_client.models.DeviceCredentials`

A JSON value representing the device credentials.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**DeviceCredentialsId**](DeviceCredentialsId.md) | The Id is automatically generated during device creation. Use 'getDeviceCredentialsByDeviceId' to obtain the id based on device id. Use 'updateDeviceCredentials' to update device credentials.  | [readonly] |
| **created_time** | **int** | Timestamp of the device credentials creation, in milliseconds | [optional] |
| **device_id** | [**DeviceId**](DeviceId.md) | JSON object with the device Id. | |
| **credentials_type** | [**DeviceCredentialsType**](DeviceCredentialsType.md) | Type of the credentials | [optional] |
| **credentials_id** | **str** | Unique Credentials Id per platform instance. Used to lookup credentials from the database. By default, new access token for your device. Depends on the type of the credentials. | |
| **credentials_value** | **str** | Value of the credentials. Null in case of ACCESS_TOKEN credentials type. Base64 value in case of X509_CERTIFICATE. Complex object in case of MQTT_BASIC and LWM2M_CREDENTIALS | [optional] |
| **version** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceCredentials.model_validate(data)` or `DeviceCredentials.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

