
# EntitiesLimitNotificationRuleTriggerConfig

`tb_pe_client.models.EntitiesLimitNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_types** | [**List[EntityType]**](EntityType.md) |  | [optional] |
| **threshold** | **float** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.entity_types`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntitiesLimitNotificationRuleTriggerConfig.model_validate(data)` or `EntitiesLimitNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

