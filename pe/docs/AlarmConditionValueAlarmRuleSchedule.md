
# AlarmConditionValueAlarmRuleSchedule

`tb_pe_client.models.AlarmConditionValueAlarmRuleSchedule`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **dynamic_value_argument** | **str** |  | [optional] |
| **static_value** | [**AlarmRuleSchedule**](AlarmRuleSchedule.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.dynamic_value_argument`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmConditionValueAlarmRuleSchedule.model_validate(data)` or `AlarmConditionValueAlarmRuleSchedule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

