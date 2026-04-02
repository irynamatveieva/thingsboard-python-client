
# AlarmRuleSchedule

`tb_pe_client.models.AlarmRuleSchedule`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **str** |  | |



## Subtypes

#### AlarmRuleAnyTimeSchedule  *(type=`ANY_TIME`)*
*(no additional properties)*

#### AlarmRuleCustomTimeSchedule  *(type=`CUSTOM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| items | List[AlarmRuleCustomTimeScheduleItem] |  | [optional] |
| timezone | str |  | [optional] |

#### AlarmRuleSpecificTimeSchedule  *(type=`SPECIFIC_TIME`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| days_of_week | List[int] |  | [optional] |
| ends_on | int |  | [optional] |
| starts_on | int |  | [optional] |
| timezone | str |  | [optional] |

## Referenced Types

#### AlarmRuleCustomTimeScheduleItem
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| day_of_week | int |  | [optional] |
| enabled | bool |  | [optional] |
| ends_on | int |  | [optional] |
| starts_on | int |  | [optional] |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleSchedule.model_validate(data)` or `AlarmRuleSchedule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

