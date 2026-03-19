
# AlarmRuleDefinition

`tb_pe_client.models.AlarmRuleDefinition`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **alarm_details** | **str** |  | [optional] |
| **condition** | [**AlarmRuleCondition**](AlarmRuleCondition.md) |  | |
| **dashboard_id** | [**DashboardId**](DashboardId.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.alarm_details`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleDefinition.model_validate(data)` or `AlarmRuleDefinition.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

