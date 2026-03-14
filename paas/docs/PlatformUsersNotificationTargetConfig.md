
# PlatformUsersNotificationTargetConfig

`tb_paas_client.models.PlatformUsersNotificationTargetConfig`

**Extends:** **NotificationTargetConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **users_filter** | [**UsersFilter**](UsersFilter.md) |  | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.users_filter`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PlatformUsersNotificationTargetConfig.model_validate(data)` or `PlatformUsersNotificationTargetConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

