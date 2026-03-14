
# StarredDashboardInfo

`tb_paas_client.models.StarredDashboardInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **UUID** | JSON object with Dashboard id. | [optional] [readonly] |
| **title** | **str** | Title of the dashboard. | [optional] |
| **starred_at** | **int** | Starred timestamp | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `StarredDashboardInfo.model_validate(data)` or `StarredDashboardInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

