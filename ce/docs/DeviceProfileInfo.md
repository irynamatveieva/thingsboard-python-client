
# DeviceProfileInfo

`tb_ce_client.models.DeviceProfileInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**EntityId**](EntityId.md) | JSON object with the entity Id.  | [optional] |
| **name** | **str** | Entity Name | [optional] |
| **image** | **str** | Either URL or Base64 data of the icon. Used in the mobile application to visualize set of device profiles in the grid view.  | [optional] |
| **default_dashboard_id** | [**DashboardId**](DashboardId.md) | Reference to the dashboard. Used in the mobile application to open the default dashboard when user navigates to device details. | [optional] |
| **type** | [**DeviceProfileType**](DeviceProfileType.md) | Type of the profile. Always 'DEFAULT' for now. Reserved for future use. | [optional] |
| **transport_type** | [**DeviceTransportType**](DeviceTransportType.md) | Type of the transport used to connect the device. Default transport supports HTTP, CoAP and MQTT. | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) | Tenant id. | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceProfileInfo.model_validate(data)` or `DeviceProfileInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

