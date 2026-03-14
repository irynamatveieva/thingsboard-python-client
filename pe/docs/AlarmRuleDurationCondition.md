
# AlarmRuleDurationCondition

`tb_pe_client.models.AlarmRuleDurationCondition`

**Extends:** **AlarmRuleCondition**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **unit** | [**TimeUnit**](TimeUnit.md) |  | |
| **value** | [**AlarmConditionValueLong**](AlarmConditionValueLong.md) |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.unit`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleDurationCondition.model_validate(data)` or `AlarmRuleDurationCondition.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

