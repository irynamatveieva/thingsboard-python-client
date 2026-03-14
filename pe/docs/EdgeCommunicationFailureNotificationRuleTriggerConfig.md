
# EdgeCommunicationFailureNotificationRuleTriggerConfig

`tb_pe_client.models.EdgeCommunicationFailureNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **edges** | **List[UUID]** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.edges`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EdgeCommunicationFailureNotificationRuleTriggerConfig.model_validate(data)` or `EdgeCommunicationFailureNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

