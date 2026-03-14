
# EntityActionNotificationRuleTriggerConfig

`tb_ce_client.models.EntityActionNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_types** | [**List[EntityType]**](EntityType.md) |  | [optional] |
| **created** | **bool** |  | [optional] |
| **updated** | **bool** |  | [optional] |
| **deleted** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.entity_types`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityActionNotificationRuleTriggerConfig.model_validate(data)` or `EntityActionNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

