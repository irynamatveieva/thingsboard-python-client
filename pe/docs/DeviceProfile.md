
# DeviceProfile

`tb_pe_client.models.DeviceProfile`

A JSON value representing the device profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**DeviceProfileId**](DeviceProfileId.md) | JSON object with the device profile Id. Specify this field to update the device profile. Referencing non-existing device profile Id will cause error. Omit this field to create new device profile. | [optional] |
| **created_time** | **int** | Timestamp of the profile creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id that owns the profile. | [optional] [readonly] |
| **name** | **str** | Unique Device Profile Name in scope of Tenant. | [optional] |
| **description** | **str** | Device Profile description.  | [optional] |
| **image** | **str** | Either URL or Base64 data of the icon. Used in the mobile application to visualize set of device profiles in the grid view.  | [optional] |
| **type** | [**DeviceProfileType**](DeviceProfileType.md) | Type of the profile. Always 'DEFAULT' for now. Reserved for future use. | [optional] |
| **transport_type** | [**DeviceTransportType**](DeviceTransportType.md) | Type of the transport used to connect the device. Default transport supports HTTP, CoAP and MQTT. | [optional] |
| **provision_type** | [**DeviceProfileProvisionType**](DeviceProfileProvisionType.md) | Provisioning strategy. | [optional] |
| **default_rule_chain_id** | [**RuleChainId**](RuleChainId.md) | Reference to the rule chain. If present, the specified rule chain will be used to process all messages related to device, including telemetry, attribute updates, etc. Otherwise, the root rule chain will be used to process those messages. | [optional] |
| **default_dashboard_id** | [**DashboardId**](DashboardId.md) | Reference to the dashboard. Used in the mobile application to open the default dashboard when user navigates to device details. | [optional] |
| **default_queue_name** | **str** | Rule engine queue name. If present, the specified queue will be used to store all unprocessed messages related to device, including telemetry, attribute updates, etc. Otherwise, the 'Main' queue will be used to store those messages. | [optional] |
| **provision_device_key** | **str** | Unique provisioning key used by 'Device Provisioning' feature. | [optional] |
| **firmware_id** | [**OtaPackageId**](OtaPackageId.md) | Reference to the firmware OTA package. If present, the specified package will be used as default device firmware.  | [optional] |
| **software_id** | [**OtaPackageId**](OtaPackageId.md) | Reference to the software OTA package. If present, the specified package will be used as default device software.  | [optional] |
| **default_edge_rule_chain_id** | [**RuleChainId**](RuleChainId.md) | Reference to the edge rule chain. If present, the specified edge rule chain will be used on the edge to process all messages related to device, including telemetry, attribute updates, etc. Otherwise, the edge root rule chain will be used to process those messages. | [optional] |
| **version** | **int** |  | [optional] |
| **default** | **bool** | Used to mark the default profile. Default profile is used when the device profile is not specified during device creation. | [optional] |
| **profile_data** | [**DeviceProfileData**](DeviceProfileData.md) | Complex JSON object that includes addition device profile configuration (transport, alarm rules, etc). | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceProfile.model_validate(data)` or `DeviceProfile.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

