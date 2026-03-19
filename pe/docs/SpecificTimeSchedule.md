
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



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.days_of_week`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SpecificTimeSchedule.model_validate(data)` or `SpecificTimeSchedule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

