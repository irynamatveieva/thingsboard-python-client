
# HourInterval

`tb_paas_client.models.HourInterval`

**Extends:** **AggInterval**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **tz** | **str** |  | |
| **offset_sec** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.tz`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `HourInterval.model_validate(data)` or `HourInterval.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

