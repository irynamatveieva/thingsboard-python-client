
# UserNotificationSettings

`tb_ce_client.models.UserNotificationSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **prefs** | [**Dict[str, NotificationPref]**](NotificationPref.md) |  | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.prefs`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `UserNotificationSettings.model_validate(data)` or `UserNotificationSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

