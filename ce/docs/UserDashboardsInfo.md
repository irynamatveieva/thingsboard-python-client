
# UserDashboardsInfo

`tb_ce_client.models.UserDashboardsInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **last** | [**List[LastVisitedDashboardInfo]**](LastVisitedDashboardInfo.md) | List of last visited dashboards. | [optional] |
| **starred** | [**List[StarredDashboardInfo]**](StarredDashboardInfo.md) | List of starred dashboards. | [optional] |



## Referenced Types

#### LastVisitedDashboardInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | JSON object with Dashboard id. | [optional] [readonly] |
| title | str | Title of the dashboard. | [optional] |
| starred | bool | Starred flag | [optional] |
| last_visited | int | Last visit timestamp | [optional] |

#### StarredDashboardInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | JSON object with Dashboard id. | [optional] [readonly] |
| title | str | Title of the dashboard. | [optional] |
| starred_at | int | Starred timestamp | [optional] |

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.last`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `UserDashboardsInfo.model_validate(data)` or `UserDashboardsInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

