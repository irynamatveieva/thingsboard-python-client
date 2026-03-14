
# EscalatedNotificationRuleRecipientsConfig

`tb_paas_client.models.EscalatedNotificationRuleRecipientsConfig`

Escalated notification rule recipients configuration

**Extends:** **NotificationRuleRecipientsConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **escalation_table** | **Dict[str, List[UUID]]** |  | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.escalation_table`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EscalatedNotificationRuleRecipientsConfig.model_validate(data)` or `EscalatedNotificationRuleRecipientsConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

