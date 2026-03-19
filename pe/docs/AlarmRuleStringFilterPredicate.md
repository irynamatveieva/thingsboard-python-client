
# AlarmRuleStringFilterPredicate

`tb_pe_client.models.AlarmRuleStringFilterPredicate`

**Extends:** **AlarmRuleKeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **ignore_case** | **bool** |  | [optional] |
| **operation** | [**StringOperation**](StringOperation.md) |  | |
| **value** | [**AlarmConditionValueString**](AlarmConditionValueString.md) |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.ignore_case`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleStringFilterPredicate.model_validate(data)` or `AlarmRuleStringFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

