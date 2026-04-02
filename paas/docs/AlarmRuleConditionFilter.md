
# AlarmRuleConditionFilter

`tb_paas_client.models.AlarmRuleConditionFilter`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **argument** | **str** |  | |
| **operation** | [**ComplexOperation**](ComplexOperation.md) |  | [optional] |
| **predicates** | [**List[AlarmRuleKeyFilterPredicate]**](AlarmRuleKeyFilterPredicate.md) |  | |
| **value_type** | [**EntityKeyValueType**](EntityKeyValueType.md) |  | |



## Referenced Types

#### ComplexOperation (enum)
`AND` | `OR`

#### AlarmRuleKeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### EntityKeyValueType (enum)
`STRING` | `NUMERIC` | `BOOLEAN` | `DATE_TIME`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.argument`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleConditionFilter.model_validate(data)` or `AlarmRuleConditionFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

