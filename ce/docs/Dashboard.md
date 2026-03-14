
# Dashboard

`tb_ce_client.models.Dashboard`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**DashboardId**](DashboardId.md) | JSON object with the dashboard Id. Specify existing dashboard Id to update the dashboard. Referencing non-existing dashboard id will cause error. Omit this field to create new dashboard. | [optional] |
| **created_time** | **int** | Timestamp of the dashboard creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. Tenant Id of the dashboard can't be changed. | [optional] [readonly] |
| **title** | **str** | Title of the dashboard. | |
| **name** | **str** | Same as title of the dashboard. Read-only field. Update the 'title' to change the 'name' of the dashboard. | [optional] [readonly] |
| **image** | **str** | Thumbnail picture for rendering of the dashboards in a grid view on mobile devices. | [optional] [readonly] |
| **mobile_hide** | **bool** | Hide dashboard from mobile devices. Useful if the dashboard is not designed for small screens. | [optional] [readonly] |
| **mobile_order** | **int** | Order on mobile devices. Useful to adjust sorting of the dashboards for mobile applications | [optional] [readonly] |
| **assigned_customers** | [**List[ShortCustomerInfo]**](ShortCustomerInfo.md) | List of assigned customers with their info. | [optional] |
| **configuration** | **object** | JSON object with main configuration of the dashboard: layouts, widgets, aliases, etc. The JSON structure of the dashboard configuration is quite complex. The easiest way to learn it is to export existing dashboard to JSON. | [optional] |
| **resources** | [**List[ResourceExportData]**](ResourceExportData.md) |  | [optional] |
| **version** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Dashboard.model_validate(data)` or `Dashboard.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

