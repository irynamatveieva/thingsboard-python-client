
# AlarmSchedule

`tb_paas_client.models.AlarmSchedule`

Configuration for alarm schedule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **dynamic_value** | [**DynamicValueString**](DynamicValueString.md) |  | [optional] |
| **type** | [**AlarmScheduleType**](AlarmScheduleType.md) |  | [optional] |



## Referenced Types

#### DynamicValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | str |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### AlarmScheduleType (enum)
`ANY_TIME` | `SPECIFIC_TIME` | `CUSTOM`

#### DynamicValueSourceType (enum)
`CURRENT_TENANT` | `CURRENT_CUSTOMER` | `CURRENT_USER` | `CURRENT_DEVICE`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.dynamic_value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmSchedule.model_validate(data)` or `AlarmSchedule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

