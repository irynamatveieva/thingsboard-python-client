# DeviceConnectivityControllerApi

`ThingsboardClient` methods:

```python
bytearray client.download_gateway_docker_compose(device_id: str)  # Download generated docker-compose.yml file for gateway (downloadGatewayDockerCompose)
bytearray client.download_server_certificate(protocol: str)  # Download server certificate using file path defined in device.connectivity properties (downloadServerCertificate)
object client.get_device_publish_telemetry_commands(device_id: str)  # Get commands to publish device telemetry (getDevicePublishTelemetryCommands)
```


## download_gateway_docker_compose

```python
bytearray client.download_gateway_docker_compose(device_id: str)
```

**GET** `/api/device-connectivity/gateway-launch/{deviceId}/docker-compose/download`

Download generated docker-compose.yml file for gateway (downloadGatewayDockerCompose)

Download generated docker-compose.yml for gateway.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **device_id** | **str** | A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**bytearray**


## download_server_certificate

```python
bytearray client.download_server_certificate(protocol: str)
```

**GET** `/api/device-connectivity/{protocol}/certificate/download`

Download server certificate using file path defined in device.connectivity properties (downloadServerCertificate)

Download server certificate.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **protocol** | **str** | A string value representing the device connectivity protocol. Possible values: 'mqtt', 'mqtts', 'http', 'https', 'coap', 'coaps' | |

### Return type

**bytearray**


## get_device_publish_telemetry_commands

```python
object client.get_device_publish_telemetry_commands(device_id: str)
```

**GET** `/api/device-connectivity/{deviceId}`

Get commands to publish device telemetry (getDevicePublishTelemetryCommands)

Fetch the list of commands to publish device telemetry based on device profile If the user has the authority of 'Tenant Administrator', the server checks that the device is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the device is assigned to the same customer.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **device_id** | **str** | A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**object**

