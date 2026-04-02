
# AlarmRuleAnyTimeSchedule

`tb_ce_client.models.AlarmRuleAnyTimeSchedule`

**Extends:** **AlarmRuleSchedule**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|



## Referenced Types

#### AlarmRuleSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AlarmRuleCustomTimeSchedule  *(extends AlarmRuleSchedule, type=`CUSTOM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| items | List[AlarmRuleCustomTimeScheduleItem] |  | [optional] |
| timezone | str |  | [optional] |

#### AlarmRuleSpecificTimeSchedule  *(extends AlarmRuleSchedule, type=`SPECIFIC_TIME`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| days_of_week | List[int] |  | [optional] |
| ends_on | int |  | [optional] |
| starts_on | int |  | [optional] |
| timezone | str |  | [optional] |

#### AlarmRuleCustomTimeScheduleItem
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| day_of_week | int |  | [optional] |
| enabled | bool |  | [optional] |
| ends_on | int |  | [optional] |
| starts_on | int |  | [optional] |

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleAnyTimeSchedule.model_validate(data)` or `AlarmRuleAnyTimeSchedule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

