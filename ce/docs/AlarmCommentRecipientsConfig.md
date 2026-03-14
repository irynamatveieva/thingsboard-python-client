
# AlarmCommentRecipientsConfig

`tb_ce_client.models.AlarmCommentRecipientsConfig`

**Extends:** **NotificationRuleRecipientsConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **targets** | **List[UUID]** |  | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.targets`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmCommentRecipientsConfig.model_validate(data)` or `AlarmCommentRecipientsConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

