
# NotificationRuleTriggerType

`tb_ce_client.models.NotificationRuleTriggerType`

## Enum Values


* `ENTITY_ACTION` (value: `'ENTITY_ACTION'`)

* `ALARM` (value: `'ALARM'`)

* `ALARM_COMMENT` (value: `'ALARM_COMMENT'`)

* `ALARM_ASSIGNMENT` (value: `'ALARM_ASSIGNMENT'`)

* `DEVICE_ACTIVITY` (value: `'DEVICE_ACTIVITY'`)

* `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT` (value: `'RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT'`)

* `EDGE_CONNECTION` (value: `'EDGE_CONNECTION'`)

* `EDGE_COMMUNICATION_FAILURE` (value: `'EDGE_COMMUNICATION_FAILURE'`)

* `NEW_PLATFORM_VERSION` (value: `'NEW_PLATFORM_VERSION'`)

* `ENTITIES_LIMIT` (value: `'ENTITIES_LIMIT'`)

* `API_USAGE_LIMIT` (value: `'API_USAGE_LIMIT'`)

* `RATE_LIMITS` (value: `'RATE_LIMITS'`)

* `TASK_PROCESSING_FAILURE` (value: `'TASK_PROCESSING_FAILURE'`)

* `RESOURCES_SHORTAGE` (value: `'RESOURCES_SHORTAGE'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationRuleTriggerType.model_validate(data)` or `NotificationRuleTriggerType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

