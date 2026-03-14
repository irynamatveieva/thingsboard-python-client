
# AdminSettings

`tb_paas_client.models.AdminSettings`

A JSON value representing the Mail Settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**AdminSettingsId**](AdminSettingsId.md) | The Id of the Administration Settings, auto-generated, UUID | [optional] |
| **created_time** | **int** | Timestamp of the settings creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. | [optional] [readonly] |
| **key** | **str** | The Administration Settings key, (e.g. 'general' or 'mail') | [optional] |
| **json_value** | **object** | JSON representation of the Administration Settings value | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AdminSettings.model_validate(data)` or `AdminSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

