
# DurationAlarmConditionSpec

`tb_ce_client.models.DurationAlarmConditionSpec`

Duration Alarm Condition Specification

**Extends:** **AlarmConditionSpec**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **unit** | [**TimeUnit**](TimeUnit.md) | Duration time unit | [optional] |
| **predicate** | [**FilterPredicateValueLong**](FilterPredicateValueLong.md) | Duration predicate | [optional] |



## Referenced Types

#### AlarmConditionSpec
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### TimeUnit (enum)
`NANOSECONDS` | `MICROSECONDS` | `MILLISECONDS` | `SECONDS` | `MINUTES` | `HOURS` | `DAYS`

#### FilterPredicateValueLong
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_value | int |  | [optional] |
| user_value | int |  | [optional] |
| dynamic_value | DynamicValueLong |  | [optional] |

#### DynamicValueLong
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

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.unit`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DurationAlarmConditionSpec.model_validate(data)` or `DurationAlarmConditionSpec.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

