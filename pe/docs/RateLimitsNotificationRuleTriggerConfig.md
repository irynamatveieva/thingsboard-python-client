
# RateLimitsNotificationRuleTriggerConfig

`tb_pe_client.models.RateLimitsNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **apis** | [**List[LimitedApi]**](LimitedApi.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.apis`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RateLimitsNotificationRuleTriggerConfig.model_validate(data)` or `RateLimitsNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

