
# RepeatingAlarmConditionSpec

`tb_paas_client.models.RepeatingAlarmConditionSpec`

**Extends:** **AlarmConditionSpec**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **predicate** | [**FilterPredicateValueInteger**](FilterPredicateValueInteger.md) | Repeating predicate | [optional] |



## Referenced Types

#### AlarmConditionSpec
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### FilterPredicateValueInteger
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_value | int |  | [optional] |
| user_value | int |  | [optional] |
| dynamic_value | DynamicValueInteger |  | [optional] |

#### DynamicValueInteger
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | int |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### DynamicValueSourceType (enum)
`CURRENT_TENANT` | `CURRENT_CUSTOMER` | `CURRENT_USER` | `CURRENT_DEVICE`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.predicate`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RepeatingAlarmConditionSpec.model_validate(data)` or `RepeatingAlarmConditionSpec.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

