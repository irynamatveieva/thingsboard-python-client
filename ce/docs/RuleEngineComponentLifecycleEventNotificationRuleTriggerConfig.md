
# RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig

`tb_ce_client.models.RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **rule_chains** | **List[UUID]** |  | [optional] |
| **rule_chain_events** | [**List[ComponentLifecycleEvent]**](ComponentLifecycleEvent.md) |  | [optional] |
| **only_rule_chain_lifecycle_failures** | **bool** |  | [optional] |
| **track_rule_node_events** | **bool** |  | [optional] |
| **rule_node_events** | [**List[ComponentLifecycleEvent]**](ComponentLifecycleEvent.md) |  | [optional] |
| **only_rule_node_lifecycle_failures** | **bool** |  | [optional] |



## Referenced Types

#### NotificationRuleTriggerConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| trigger_type | NotificationRuleTriggerType |  |  |

#### ComponentLifecycleEvent (enum)
`CREATED` | `STARTED` | `ACTIVATED` | `SUSPENDED` | `UPDATED` | `STOPPED` | `DELETED` | `FAILED` | `DEACTIVATED` | `RELATION_UPDATED` | … (11 values total)

#### NotificationRuleTriggerType (enum)
`ENTITY_ACTION` | `ALARM` | `ALARM_COMMENT` | `ALARM_ASSIGNMENT` | `DEVICE_ACTIVITY` | `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT` | `EDGE_CONNECTION` | `EDGE_COMMUNICATION_FAILURE` | `NEW_PLATFORM_VERSION` | `ENTITIES_LIMIT` | … (14 values total)

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.rule_chains`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.model_validate(data)` or `RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

