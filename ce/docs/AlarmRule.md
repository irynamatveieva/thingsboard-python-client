
# AlarmRule

`tb_ce_client.models.AlarmRule`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **condition** | [**AlarmCondition**](AlarmCondition.md) | JSON object representing the alarm rule condition | [optional] |
| **alarm_details** | **str** | String value representing the additional details for an alarm rule | [optional] |
| **dashboard_id** | [**DashboardId**](DashboardId.md) | JSON object with the dashboard Id representing the reference to alarm details dashboard used by mobile application | [optional] |
| **schedule** | [**AlarmSchedule**](AlarmSchedule.md) | JSON object representing time interval during which the rule is active | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.condition`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRule.model_validate(data)` or `AlarmRule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

