
# UserDashboardsInfo

`tb_ce_client.models.UserDashboardsInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **last** | [**List[LastVisitedDashboardInfo]**](LastVisitedDashboardInfo.md) | List of last visited dashboards. | [optional] |
| **starred** | [**List[StarredDashboardInfo]**](StarredDashboardInfo.md) | List of starred dashboards. | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.last`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `UserDashboardsInfo.model_validate(data)` or `UserDashboardsInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

