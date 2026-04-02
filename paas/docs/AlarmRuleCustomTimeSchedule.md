
# AlarmRuleCustomTimeSchedule

`tb_paas_client.models.AlarmRuleCustomTimeSchedule`

**Extends:** **AlarmRuleSchedule**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **items** | [**List[AlarmRuleCustomTimeScheduleItem]**](AlarmRuleCustomTimeScheduleItem.md) |  | [optional] |
| **timezone** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.items`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleCustomTimeSchedule.model_validate(data)` or `AlarmRuleCustomTimeSchedule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

