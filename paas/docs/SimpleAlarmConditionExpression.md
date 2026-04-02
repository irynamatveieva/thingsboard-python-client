
# SimpleAlarmConditionExpression

`tb_paas_client.models.SimpleAlarmConditionExpression`

**Extends:** **AlarmConditionExpression**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **filters** | [**List[AlarmRuleConditionFilter]**](AlarmRuleConditionFilter.md) |  | |
| **operation** | [**ComplexOperation**](ComplexOperation.md) |  | [optional] |



## Referenced Types

#### AlarmConditionExpression
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AlarmRuleConditionFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| argument | str |  |  |
| operation | ComplexOperation |  | [optional] |
| predicates | List[AlarmRuleKeyFilterPredicate] |  |  |
| value_type | EntityKeyValueType |  |  |

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
- **Attribute access:** `obj.filters`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SimpleAlarmConditionExpression.model_validate(data)` or `SimpleAlarmConditionExpression.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

