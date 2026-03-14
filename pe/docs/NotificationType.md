
# NotificationType

`tb_pe_client.models.NotificationType`

## Enum Values


* `GENERAL` (value: `'GENERAL'`)

* `ALARM` (value: `'ALARM'`)

* `DEVICE_ACTIVITY` (value: `'DEVICE_ACTIVITY'`)

* `ENTITY_ACTION` (value: `'ENTITY_ACTION'`)

* `ALARM_COMMENT` (value: `'ALARM_COMMENT'`)

* `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT` (value: `'RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT'`)

* `ALARM_ASSIGNMENT` (value: `'ALARM_ASSIGNMENT'`)

* `NEW_PLATFORM_VERSION` (value: `'NEW_PLATFORM_VERSION'`)

* `ENTITIES_LIMIT` (value: `'ENTITIES_LIMIT'`)

* `ENTITIES_LIMIT_INCREASE_REQUEST` (value: `'ENTITIES_LIMIT_INCREASE_REQUEST'`)

* `ADDON_ACCESS_ERROR` (value: `'ADDON_ACCESS_ERROR'`)

* `API_USAGE_LIMIT` (value: `'API_USAGE_LIMIT'`)

* `RULE_NODE` (value: `'RULE_NODE'`)

* `INTEGRATION_LIFECYCLE_EVENT` (value: `'INTEGRATION_LIFECYCLE_EVENT'`)

* `RATE_LIMITS` (value: `'RATE_LIMITS'`)

* `EDGE_CONNECTION` (value: `'EDGE_CONNECTION'`)

* `EDGE_COMMUNICATION_FAILURE` (value: `'EDGE_COMMUNICATION_FAILURE'`)

* `TASK_PROCESSING_FAILURE` (value: `'TASK_PROCESSING_FAILURE'`)

* `RESOURCES_SHORTAGE` (value: `'RESOURCES_SHORTAGE'`)

* `USER_ACTIVATED` (value: `'USER_ACTIVATED'`)

* `USER_REGISTERED` (value: `'USER_REGISTERED'`)

* `REPORT_GENERATED` (value: `'REPORT_GENERATED'`)



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationType.model_validate(data)` or `NotificationType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

