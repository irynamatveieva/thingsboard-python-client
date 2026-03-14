
# SlackNotificationTargetConfig

`tb_paas_client.models.SlackNotificationTargetConfig`

**Extends:** **NotificationTargetConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **conversation_type** | [**SlackConversationType**](SlackConversationType.md) |  | [optional] |
| **conversation** | [**SlackConversation**](SlackConversation.md) |  | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.conversation_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SlackNotificationTargetConfig.model_validate(data)` or `SlackNotificationTargetConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

