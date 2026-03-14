
# AlarmRuleSpecificTimeSchedule

`tb_pe_client.models.AlarmRuleSpecificTimeSchedule`

**Extends:** **AlarmRuleSchedule**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **timezone** | **str** |  | [optional] |
| **days_of_week** | **List[int]** |  | [optional] |
| **starts_on** | **int** |  | [optional] |
| **ends_on** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.timezone`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleSpecificTimeSchedule.model_validate(data)` or `AlarmRuleSpecificTimeSchedule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

