
# AlarmCommentNotificationRuleTriggerConfig

`tb_paas_client.models.AlarmCommentNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **alarm_types** | **List[str]** |  | [optional] |
| **alarm_severities** | [**List[AlarmSeverity]**](AlarmSeverity.md) |  | [optional] |
| **alarm_statuses** | [**List[AlarmSearchStatus]**](AlarmSearchStatus.md) |  | [optional] |
| **only_user_comments** | **bool** |  | [optional] |
| **notify_on_comment_update** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.alarm_types`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmCommentNotificationRuleTriggerConfig.model_validate(data)` or `AlarmCommentNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

