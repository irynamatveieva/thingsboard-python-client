
# Device

`tb_paas_client.models.Device`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**DeviceId**](DeviceId.md) | JSON object with the Device Id. Specify this field to update the Device. Referencing non-existing Device Id will cause error. Omit this field to create new Device. | [optional] |
| **created_time** | **int** | Timestamp of the device creation, in milliseconds | [optional] [readonly] |
| **additional_info** | **object** | Additional parameters of the device. May include: 'gateway' (boolean, whether the device is a gateway), 'description' (string), 'lastConnectedGateway' (string, UUID of the last gateway that connected this device). | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. Use 'assignDeviceToTenant' to change the Tenant Id. | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id. Use 'assignDeviceToCustomer' to change the Customer Id. | [optional] [readonly] |
| **name** | **str** | Unique Device Name in scope of Tenant | [optional] |
| **type** | **str** | Device Profile Name | [optional] |
| **label** | **str** | Label that may be used in widgets | [optional] |
| **device_profile_id** | [**DeviceProfileId**](DeviceProfileId.md) | JSON object with Device Profile Id. | |
| **device_data** | [**DeviceData**](DeviceData.md) | JSON object with content specific to type of transport in the device profile. | [optional] |
| **firmware_id** | [**OtaPackageId**](OtaPackageId.md) | JSON object with Ota Package Id. | [optional] |
| **software_id** | [**OtaPackageId**](OtaPackageId.md) | JSON object with Ota Package Id. | [optional] |
| **version** | **int** |  | [optional] |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with Customer or Tenant Id | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`CustomerId`, `DeviceId`, `DeviceProfileId`, `OtaPackageId`, `TenantId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### DeviceData
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| configuration | DeviceConfiguration | Device configuration for device profile type. DEFAULT is only supported value for now | [optional] |
| transport_configuration | DeviceTransportConfiguration | Device transport configuration used to connect the device | [optional] |

#### DeviceConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | DeviceProfileType | Device profile type |  |

#### DeviceTransportConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### DeviceProfileType (enum)
`DEFAULT`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Device.model_validate(data)` or `Device.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

