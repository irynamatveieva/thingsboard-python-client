
# AlarmRuleComplexFilterPredicate

`tb_pe_client.models.AlarmRuleComplexFilterPredicate`

**Extends:** **AlarmRuleKeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operation** | [**ComplexOperation**](ComplexOperation.md) |  | [optional] |
| **predicates** | [**List[AlarmRuleKeyFilterPredicate]**](AlarmRuleKeyFilterPredicate.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.operation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleComplexFilterPredicate.model_validate(data)` or `AlarmRuleComplexFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

