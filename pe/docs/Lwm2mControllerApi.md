# Lwm2mControllerApi

`ThingsboardClient` methods:

```python
LwM2MServerSecurityConfigDefault client.get_lwm2m_bootstrap_security_info(is_bootstrap_server: bool)  # Get Lwm2m Bootstrap SecurityInfo (getLwm2mBootstrapSecurityInfo)
Device client.save_lwm2m_device_with_credentials(request_body: Dict[str, object], entity_group_id: Optional[str] = None)  # Save LwM2M device with credentials (saveLwm2mDeviceWithCredentials)
```


## get_lwm2m_bootstrap_security_info

```python
LwM2MServerSecurityConfigDefault client.get_lwm2m_bootstrap_security_info(is_bootstrap_server: bool)
```

**GET** `/api/lwm2m/deviceProfile/bootstrap/{isBootstrapServer}`

Get Lwm2m Bootstrap SecurityInfo (getLwm2mBootstrapSecurityInfo)

Get the Lwm2m Bootstrap SecurityInfo object (of the current server) based on the provided isBootstrapServer parameter. If isBootstrapServer == true, get the parameters of the current Bootstrap Server. If isBootstrapServer == false, get the parameters of the current Lwm2m Server. Used for client settings when starting the client in Bootstrap mode.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **is_bootstrap_server** | **bool** | A Boolean value representing the Server SecurityInfo for future Bootstrap client mode settings. Values: 'true' for Bootstrap Server; 'false' for Lwm2m Server.  | |

### Return type

**LwM2MServerSecurityConfigDefault**


## save_lwm2m_device_with_credentials

```python
Device client.save_lwm2m_device_with_credentials(request_body: Dict[str, object], entity_group_id: Optional[str] = None)
```

**POST** `/api/lwm2m/device-credentials`

Save LwM2M device with credentials (saveLwm2mDeviceWithCredentials)

Deprecated.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **request_body** | **Dict[str, object]** |  | |
| **entity_group_id** | **str** |  | [optional] |

### Return type

**Device**

