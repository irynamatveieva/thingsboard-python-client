
# AlarmRuleStringFilterPredicate

`tb_ce_client.models.AlarmRuleStringFilterPredicate`

**Extends:** **AlarmRuleKeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operation** | [**StringOperation**](StringOperation.md) |  | |
| **value** | [**AlarmConditionValueString**](AlarmConditionValueString.md) |  | |
| **ignore_case** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.operation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleStringFilterPredicate.model_validate(data)` or `AlarmRuleStringFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

