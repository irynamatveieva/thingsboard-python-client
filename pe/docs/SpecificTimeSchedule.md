
# SpecificTimeSchedule

`tb_pe_client.models.SpecificTimeSchedule`

**Extends:** **AlarmSchedule**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **days_of_week** | **List[int]** |  | [optional] |
| **ends_on** | **int** |  | [optional] |
| **starts_on** | **int** |  | [optional] |
| **timezone** | **str** |  | [optional] |



## Referenced Types

#### AlarmSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| dynamic_value | DynamicValueString |  | [optional] |
| type | AlarmScheduleType |  | [optional] |

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

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.days_of_week`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SpecificTimeSchedule.model_validate(data)` or `SpecificTimeSchedule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

