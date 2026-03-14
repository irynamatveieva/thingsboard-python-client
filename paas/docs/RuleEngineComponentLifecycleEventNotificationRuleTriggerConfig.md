
# RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig

`tb_paas_client.models.RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig`

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



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.rule_chains`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.model_validate(data)` or `RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

