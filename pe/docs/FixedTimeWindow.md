
# FixedTimeWindow

`tb_pe_client.models.FixedTimeWindow`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **start_time_ms** | **int** |  | [optional] |
| **end_time_ms** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.start_time_ms`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `FixedTimeWindow.model_validate(data)` or `FixedTimeWindow.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

