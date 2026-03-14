
# NotificationRule

`tb_ce_client.models.NotificationRule`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**NotificationRuleId**](NotificationRuleId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **name** | **str** |  | |
| **enabled** | **bool** |  | [optional] |
| **template_id** | [**NotificationTemplateId**](NotificationTemplateId.md) |  | |
| **trigger_type** | [**NotificationRuleTriggerType**](NotificationRuleTriggerType.md) |  | |
| **trigger_config** | [**NotificationRuleTriggerConfig**](NotificationRuleTriggerConfig.md) |  | |
| **recipients_config** | [**NotificationRuleRecipientsConfig**](NotificationRuleRecipientsConfig.md) |  | |
| **additional_config** | [**NotificationRuleConfig**](NotificationRuleConfig.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationRule.model_validate(data)` or `NotificationRule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

