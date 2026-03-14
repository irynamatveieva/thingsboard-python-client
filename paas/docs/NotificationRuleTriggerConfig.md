
# NotificationRuleTriggerConfig

`tb_paas_client.models.NotificationRuleTriggerConfig`

Configuration for notification rule trigger

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **trigger_type** | [**NotificationRuleTriggerType**](NotificationRuleTriggerType.md) |  | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.trigger_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationRuleTriggerConfig.model_validate(data)` or `NotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

