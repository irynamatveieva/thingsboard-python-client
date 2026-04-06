
# AlarmRuleNoDataFilterPredicate

`tb_pe_client.models.AlarmRuleNoDataFilterPredicate`

**Extends:** **AlarmRuleKeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **duration** | [**AlarmConditionValueLong**](AlarmConditionValueLong.md) |  | |
| **unit** | [**TimeUnit**](TimeUnit.md) |  | |



## Referenced Types

#### AlarmRuleKeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AlarmConditionValueLong
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | int |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

#### TimeUnit (enum)
`NANOSECONDS` | `MICROSECONDS` | `MILLISECONDS` | `SECONDS` | `MINUTES` | `HOURS` | `DAYS`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.duration`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleNoDataFilterPredicate.model_validate(data)` or `AlarmRuleNoDataFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

