
# LastVisitedDashboardInfo

`tb_pe_client.models.LastVisitedDashboardInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **UUID** | JSON object with Dashboard id. | [optional] [readonly] |
| **title** | **str** | Title of the dashboard. | [optional] |
| **starred** | **bool** | Starred flag | [optional] |
| **last_visited** | **int** | Last visit timestamp | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LastVisitedDashboardInfo.model_validate(data)` or `LastVisitedDashboardInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

