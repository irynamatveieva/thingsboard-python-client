
# AlarmRuleCondition

`tb_paas_client.models.AlarmRuleCondition`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **expression** | [**AlarmConditionExpression**](AlarmConditionExpression.md) |  | |
| **schedule** | [**AlarmConditionValueAlarmRuleSchedule**](AlarmConditionValueAlarmRuleSchedule.md) |  | [optional] |
| **type** | **str** |  | |



## Referenced Types

#### AlarmConditionExpression
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AlarmConditionValueAlarmRuleSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| dynamic_value_argument | str |  | [optional] |
| static_value | AlarmRuleSchedule |  | [optional] |

#### AlarmRuleSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.expression`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleCondition.model_validate(data)` or `AlarmRuleCondition.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

