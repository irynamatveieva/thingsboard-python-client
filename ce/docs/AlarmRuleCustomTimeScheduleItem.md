
# AlarmRuleCustomTimeScheduleItem

`tb_ce_client.models.AlarmRuleCustomTimeScheduleItem`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **day_of_week** | **int** |  | [optional] |
| **enabled** | **bool** |  | [optional] |
| **ends_on** | **int** |  | [optional] |
| **starts_on** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.day_of_week`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleCustomTimeScheduleItem.model_validate(data)` or `AlarmRuleCustomTimeScheduleItem.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

