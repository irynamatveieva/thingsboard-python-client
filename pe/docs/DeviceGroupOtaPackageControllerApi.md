# DeviceGroupOtaPackageControllerApi

`ThingsboardClient` methods:

```python
None client.delete_device_group_ota_package(id: str)  # deleteDeviceGroupOtaPackage
DeviceGroupOtaPackage client.get_firmware_by_id(group_id: str, firmware_type: str)  # getFirmwareById
DeviceGroupOtaPackage client.save_device_group_ota_package(device_group_ota_package: DeviceGroupOtaPackage)  # saveDeviceGroupOtaPackage
```


## delete_device_group_ota_package

```python
None client.delete_device_group_ota_package(id: str)
```

**DELETE** `/api/deviceGroupOtaPackage/{id}`

deleteDeviceGroupOtaPackage


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **str** |  | |

### Return type

None (empty response body)


## get_firmware_by_id

```python
DeviceGroupOtaPackage client.get_firmware_by_id(group_id: str, firmware_type: str)
```

**GET** `/api/deviceGroupOtaPackage/{groupId}/{firmwareType}`

getFirmwareById


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str** |  | |
| **firmware_type** | **str** |  | |

### Return type

**DeviceGroupOtaPackage**


## save_device_group_ota_package

```python
DeviceGroupOtaPackage client.save_device_group_ota_package(device_group_ota_package: DeviceGroupOtaPackage)
```

**POST** `/api/deviceGroupOtaPackage`

saveDeviceGroupOtaPackage


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **device_group_ota_package** | **DeviceGroupOtaPackage** |  | |

### Return type

**DeviceGroupOtaPackage**

