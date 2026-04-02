
# NotificationSettings

`tb_pe_client.models.NotificationSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **delivery_methods_configs** | [**Dict[str, NotificationDeliveryMethodConfig]**](NotificationDeliveryMethodConfig.md) |  | |



## Referenced Types

#### NotificationDeliveryMethodConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| method | str |  |  |

#### MobileAppNotificationDeliveryMethodConfig  *(extends NotificationDeliveryMethodConfig, method=`MOBILE_APP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| firebase_service_account_credentials_file_name | str |  | [optional] |
| firebase_service_account_credentials | str |  | [optional] |
| use_system_settings | bool |  | [optional] |

#### SlackNotificationDeliveryMethodConfig  *(extends NotificationDeliveryMethodConfig, method=`SLACK`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| bot_token | str |  |  |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.delivery_methods_configs`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationSettings.model_validate(data)` or `NotificationSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

