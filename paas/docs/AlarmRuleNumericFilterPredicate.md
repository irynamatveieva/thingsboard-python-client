
# AlarmRuleNumericFilterPredicate

`tb_paas_client.models.AlarmRuleNumericFilterPredicate`

**Extends:** **AlarmRuleKeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operation** | [**NumericOperation**](NumericOperation.md) |  | |
| **value** | [**AlarmConditionValueDouble**](AlarmConditionValueDouble.md) |  | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.operation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleNumericFilterPredicate.model_validate(data)` or `AlarmRuleNumericFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

