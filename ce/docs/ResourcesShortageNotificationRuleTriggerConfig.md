
# ResourcesShortageNotificationRuleTriggerConfig

`tb_ce_client.models.ResourcesShortageNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **cpu_threshold** | **float** |  | [optional] |
| **ram_threshold** | **float** |  | [optional] |
| **storage_threshold** | **float** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.cpu_threshold`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ResourcesShortageNotificationRuleTriggerConfig.model_validate(data)` or `ResourcesShortageNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

