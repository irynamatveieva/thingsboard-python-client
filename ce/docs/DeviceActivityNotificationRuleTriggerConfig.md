
# DeviceActivityNotificationRuleTriggerConfig

`tb_ce_client.models.DeviceActivityNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **devices** | **List[UUID]** |  | [optional] |
| **device_profiles** | **List[UUID]** |  | [optional] |
| **notify_on** | [**List[DeviceEvent]**](DeviceEvent.md) |  | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.devices`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceActivityNotificationRuleTriggerConfig.model_validate(data)` or `DeviceActivityNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

