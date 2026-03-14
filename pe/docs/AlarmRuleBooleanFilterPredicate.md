
# AlarmRuleBooleanFilterPredicate

`tb_pe_client.models.AlarmRuleBooleanFilterPredicate`

**Extends:** **AlarmRuleKeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operation** | [**BooleanOperation**](BooleanOperation.md) |  | |
| **value** | [**AlarmConditionValueBoolean**](AlarmConditionValueBoolean.md) |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.operation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleBooleanFilterPredicate.model_validate(data)` or `AlarmRuleBooleanFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

