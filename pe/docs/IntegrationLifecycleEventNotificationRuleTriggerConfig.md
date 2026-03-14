
# IntegrationLifecycleEventNotificationRuleTriggerConfig

`tb_pe_client.models.IntegrationLifecycleEventNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **integration_types** | [**List[IntegrationType]**](IntegrationType.md) |  | [optional] |
| **integrations** | **List[UUID]** |  | [optional] |
| **notify_on** | [**List[ComponentLifecycleEvent]**](ComponentLifecycleEvent.md) |  | [optional] |
| **only_on_error** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.integration_types`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `IntegrationLifecycleEventNotificationRuleTriggerConfig.model_validate(data)` or `IntegrationLifecycleEventNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

