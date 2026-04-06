
# EscalatedNotificationRuleRecipientsConfig

`tb_ce_client.models.EscalatedNotificationRuleRecipientsConfig`

Escalated notification rule recipients configuration

**Extends:** **NotificationRuleRecipientsConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **escalation_table** | **Dict[str, List[UUID]]** |  | |



## Referenced Types

#### NotificationRuleRecipientsConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| trigger_type | NotificationRuleTriggerType |  | [optional] |

#### NotificationRuleTriggerType (enum)
`ENTITY_ACTION` | `ALARM` | `ALARM_COMMENT` | `ALARM_ASSIGNMENT` | `DEVICE_ACTIVITY` | `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT` | `EDGE_CONNECTION` | `EDGE_COMMUNICATION_FAILURE` | `NEW_PLATFORM_VERSION` | `ENTITIES_LIMIT` | … (14 values total)

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.escalation_table`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EscalatedNotificationRuleRecipientsConfig.model_validate(data)` or `EscalatedNotificationRuleRecipientsConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

