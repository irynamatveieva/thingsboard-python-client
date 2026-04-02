
# AlarmConditionFilter

`tb_paas_client.models.AlarmConditionFilter`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **value_type** | [**EntityKeyValueType**](EntityKeyValueType.md) | String representation of the type of the value | [optional] |
| **key** | [**AlarmConditionFilterKey**](AlarmConditionFilterKey.md) | JSON object for specifying alarm condition by specific key | [optional] |
| **predicate** | [**KeyFilterPredicate**](KeyFilterPredicate.md) | JSON object representing filter condition | [optional] |
| **value** | **object** |  | [optional] |



## Referenced Types

#### EntityKeyValueType (enum)
`STRING` | `NUMERIC` | `BOOLEAN` | `DATE_TIME`

#### AlarmConditionFilterKey
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | AlarmConditionKeyType | The key type | [optional] |
| key | str | String value representing the key | [optional] |

#### KeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AlarmConditionKeyType (enum)
`ATTRIBUTE` | `TIME_SERIES` | `ENTITY_FIELD` | `CONSTANT`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.value_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmConditionFilter.model_validate(data)` or `AlarmConditionFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

