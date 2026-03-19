
# AlarmSchedule

`tb_pe_client.models.AlarmSchedule`

Configuration for alarm schedule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **dynamic_value** | [**DynamicValueString**](DynamicValueString.md) |  | [optional] |
| **type** | [**AlarmScheduleType**](AlarmScheduleType.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.dynamic_value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmSchedule.model_validate(data)` or `AlarmSchedule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

