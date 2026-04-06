
# MobileAppNotificationDeliveryMethodConfig

`tb_paas_client.models.MobileAppNotificationDeliveryMethodConfig`

**Extends:** **NotificationDeliveryMethodConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **firebase_service_account_credentials_file_name** | **str** |  | [optional] |
| **firebase_service_account_credentials** | **str** |  | [optional] |
| **use_system_settings** | **bool** |  | [optional] |



## Referenced Types

#### NotificationDeliveryMethodConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| method | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.firebase_service_account_credentials_file_name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MobileAppNotificationDeliveryMethodConfig.model_validate(data)` or `MobileAppNotificationDeliveryMethodConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

