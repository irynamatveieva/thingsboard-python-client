
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



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `TenantId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AdminSettings.model_validate(data)` or `AdminSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

