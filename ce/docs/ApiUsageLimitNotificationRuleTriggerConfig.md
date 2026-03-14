
# ApiUsageLimitNotificationRuleTriggerConfig

`tb_ce_client.models.ApiUsageLimitNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **api_features** | [**List[ApiFeature]**](ApiFeature.md) |  | [optional] |
| **notify_on** | [**List[ApiUsageStateValue]**](ApiUsageStateValue.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.api_features`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ApiUsageLimitNotificationRuleTriggerConfig.model_validate(data)` or `ApiUsageLimitNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

