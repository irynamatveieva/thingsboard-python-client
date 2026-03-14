
# DurationAlarmConditionSpec

`tb_ce_client.models.DurationAlarmConditionSpec`

Duration Alarm Condition Specification

**Extends:** **AlarmConditionSpec**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **unit** | [**TimeUnit**](TimeUnit.md) | Duration time unit | [optional] |
| **predicate** | [**FilterPredicateValueLong**](FilterPredicateValueLong.md) | Duration predicate | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.unit`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DurationAlarmConditionSpec.model_validate(data)` or `DurationAlarmConditionSpec.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

