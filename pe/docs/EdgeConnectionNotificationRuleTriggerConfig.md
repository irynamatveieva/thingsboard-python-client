
# EdgeConnectionNotificationRuleTriggerConfig

`tb_pe_client.models.EdgeConnectionNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **edges** | **List[UUID]** |  | [optional] |
| **notify_on** | [**List[EdgeConnectivityEvent]**](EdgeConnectivityEvent.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.edges`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EdgeConnectionNotificationRuleTriggerConfig.model_validate(data)` or `EdgeConnectionNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

