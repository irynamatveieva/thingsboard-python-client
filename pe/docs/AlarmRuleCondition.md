
# AlarmRuleCondition

`tb_pe_client.models.AlarmRuleCondition`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **expression** | [**AlarmConditionExpression**](AlarmConditionExpression.md) |  | |
| **schedule** | [**AlarmConditionValueAlarmRuleSchedule**](AlarmConditionValueAlarmRuleSchedule.md) |  | [optional] |
| **type** | **str** |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.expression`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleCondition.model_validate(data)` or `AlarmRuleCondition.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

