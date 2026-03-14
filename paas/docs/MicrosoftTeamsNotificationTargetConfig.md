
# MicrosoftTeamsNotificationTargetConfig

`tb_paas_client.models.MicrosoftTeamsNotificationTargetConfig`

**Extends:** **NotificationTargetConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **webhook_url** | **str** |  | |
| **channel_name** | **str** |  | |
| **use_old_api** | **bool** |  | [optional] |
| **email** | **str** |  | [optional] |
| **first_name** | **str** |  | [optional] |
| **id** | **object** |  | [optional] |
| **last_name** | **str** |  | [optional] |
| **title** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.webhook_url`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MicrosoftTeamsNotificationTargetConfig.model_validate(data)` or `MicrosoftTeamsNotificationTargetConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

