
# MonthInterval

`tb_ce_client.models.MonthInterval`

**Extends:** **AggInterval**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **tz** | **str** |  | |
| **offset_sec** | **int** |  | [optional] |



## Referenced Types

#### AggInterval
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.tz`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MonthInterval.model_validate(data)` or `MonthInterval.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

