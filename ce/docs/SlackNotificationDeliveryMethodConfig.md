
# SlackNotificationDeliveryMethodConfig

`tb_ce_client.models.SlackNotificationDeliveryMethodConfig`

**Extends:** **NotificationDeliveryMethodConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **bot_token** | **str** |  | |



## Referenced Types

#### NotificationDeliveryMethodConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| method | str |  |  |

#### MobileAppNotificationDeliveryMethodConfig  *(extends NotificationDeliveryMethodConfig, method=`MOBILE_APP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| firebase_service_account_credentials_file_name | str |  | [optional] |
| firebase_service_account_credentials | str |  |  |

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.bot_token`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SlackNotificationDeliveryMethodConfig.model_validate(data)` or `SlackNotificationDeliveryMethodConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

