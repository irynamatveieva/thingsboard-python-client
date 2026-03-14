
# NotificationInfo

`tb_paas_client.models.NotificationInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **dashboard_id** | [**DashboardId**](DashboardId.md) |  | [optional] |
| **state_entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **type** | **str** |  | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.dashboard_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationInfo.model_validate(data)` or `NotificationInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

