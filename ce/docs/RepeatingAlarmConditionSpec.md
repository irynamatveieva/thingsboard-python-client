
# RepeatingAlarmConditionSpec

`tb_ce_client.models.RepeatingAlarmConditionSpec`

**Extends:** **AlarmConditionSpec**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **predicate** | [**FilterPredicateValueInteger**](FilterPredicateValueInteger.md) | Repeating predicate | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.predicate`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RepeatingAlarmConditionSpec.model_validate(data)` or `RepeatingAlarmConditionSpec.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

