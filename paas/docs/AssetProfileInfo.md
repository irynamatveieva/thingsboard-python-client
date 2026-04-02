
# AssetProfileInfo

`tb_paas_client.models.AssetProfileInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**EntityId**](EntityId.md) | JSON object with the entity Id.  | [optional] |
| **name** | **str** | Entity Name | [optional] |
| **image** | **str** | Either URL or Base64 data of the icon. Used in the mobile application to visualize set of asset profiles in the grid view.  | [optional] |
| **default_dashboard_id** | [**DashboardId**](DashboardId.md) | Reference to the dashboard. Used in the mobile application to open the default dashboard when user navigates to asset details. | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) | Tenant id. | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AssetProfileInfo.model_validate(data)` or `AssetProfileInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

