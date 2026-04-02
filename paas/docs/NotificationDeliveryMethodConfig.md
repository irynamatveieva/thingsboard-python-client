
# NotificationDeliveryMethodConfig

`tb_paas_client.models.NotificationDeliveryMethodConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **method** | **str** |  | |



## Subtypes

#### MobileAppNotificationDeliveryMethodConfig  *(method=`MOBILE_APP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| firebase_service_account_credentials_file_name | str |  | [optional] |
| firebase_service_account_credentials | str |  | [optional] |
| use_system_settings | bool |  | [optional] |

#### SlackNotificationDeliveryMethodConfig  *(method=`SLACK`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| bot_token | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.method`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationDeliveryMethodConfig.model_validate(data)` or `NotificationDeliveryMethodConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

