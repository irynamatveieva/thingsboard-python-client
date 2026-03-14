
# AlarmRuleConditionFilter

`tb_ce_client.models.AlarmRuleConditionFilter`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **argument** | **str** |  | |
| **value_type** | [**EntityKeyValueType**](EntityKeyValueType.md) |  | |
| **operation** | [**ComplexOperation**](ComplexOperation.md) |  | [optional] |
| **predicates** | [**List[AlarmRuleKeyFilterPredicate]**](AlarmRuleKeyFilterPredicate.md) |  | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.argument`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleConditionFilter.model_validate(data)` or `AlarmRuleConditionFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

