
# CustomTimeSchedule

`tb_ce_client.models.CustomTimeSchedule`

**Extends:** **AlarmSchedule**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **timezone** | **str** |  | [optional] |
| **items** | [**List[CustomTimeScheduleItem]**](CustomTimeScheduleItem.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.timezone`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CustomTimeSchedule.model_validate(data)` or `CustomTimeSchedule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

