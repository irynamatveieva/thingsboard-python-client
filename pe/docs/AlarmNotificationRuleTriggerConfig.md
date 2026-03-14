
# AlarmNotificationRuleTriggerConfig

`tb_pe_client.models.AlarmNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **alarm_types** | **List[str]** |  | [optional] |
| **alarm_severities** | [**List[AlarmSeverity]**](AlarmSeverity.md) |  | [optional] |
| **notify_on** | [**List[AlarmAction]**](AlarmAction.md) |  | |
| **clear_rule** | [**ClearRule**](ClearRule.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.alarm_types`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmNotificationRuleTriggerConfig.model_validate(data)` or `AlarmNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

