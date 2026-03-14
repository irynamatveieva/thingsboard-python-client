
# SimpleAlarmConditionExpression

`tb_ce_client.models.SimpleAlarmConditionExpression`

**Extends:** **AlarmConditionExpression**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **filters** | [**List[AlarmRuleConditionFilter]**](AlarmRuleConditionFilter.md) |  | |
| **operation** | [**ComplexOperation**](ComplexOperation.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.filters`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SimpleAlarmConditionExpression.model_validate(data)` or `SimpleAlarmConditionExpression.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

