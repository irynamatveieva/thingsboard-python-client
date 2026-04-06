
# SlackNotificationTargetConfig

`tb_pe_client.models.SlackNotificationTargetConfig`

**Extends:** **NotificationTargetConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **conversation_type** | [**SlackConversationType**](SlackConversationType.md) |  | [optional] |
| **conversation** | [**SlackConversation**](SlackConversation.md) |  | |



## Referenced Types

#### NotificationTargetConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| description | str |  | [optional] |
| type | str |  |  |

#### SlackConversationType (enum)
`DIRECT` | `PUBLIC_CHANNEL` | `PRIVATE_CHANNEL`

#### SlackConversation
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | SlackConversationType |  |  |
| id | str |  |  |
| name | str |  |  |
| whole_name | str |  | [optional] |
| email | str |  | [optional] |
| title | str |  | [optional] |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.conversation_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SlackNotificationTargetConfig.model_validate(data)` or `SlackNotificationTargetConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

