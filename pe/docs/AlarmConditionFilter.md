
# AlarmConditionFilter

`tb_pe_client.models.AlarmConditionFilter`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **key** | [**AlarmConditionFilterKey**](AlarmConditionFilterKey.md) | JSON object for specifying alarm condition by specific key | [optional] |
| **value_type** | [**EntityKeyValueType**](EntityKeyValueType.md) | String representation of the type of the value | [optional] |
| **value** | **object** |  | [optional] |
| **predicate** | [**KeyFilterPredicate**](KeyFilterPredicate.md) | JSON object representing filter condition | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.key`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmConditionFilter.model_validate(data)` or `AlarmConditionFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

