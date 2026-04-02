
# HomeDashboardInfo

`tb_paas_client.models.HomeDashboardInfo`

A JSON object that represents home dashboard id and other parameters

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **dashboard_id** | [**DashboardId**](DashboardId.md) | JSON object with the dashboard Id. | [optional] |
| **hide_dashboard_toolbar** | **bool** | Hide dashboard toolbar flag. Useful for rendering dashboards on mobile. | [optional] |



## Referenced Types

> **EntityId types** (`DashboardId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.dashboard_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `HomeDashboardInfo.model_validate(data)` or `HomeDashboardInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

