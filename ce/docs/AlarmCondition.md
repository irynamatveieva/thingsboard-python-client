
# AlarmCondition

`tb_ce_client.models.AlarmCondition`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **condition** | [**List[AlarmConditionFilter]**](AlarmConditionFilter.md) |  | [optional] |
| **spec** | [**AlarmConditionSpec**](AlarmConditionSpec.md) | JSON object representing alarm condition type | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.condition`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmCondition.model_validate(data)` or `AlarmCondition.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

