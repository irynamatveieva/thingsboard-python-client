
# History

`tb_paas_client.models.History`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **history_type** | **int** |  | [optional] |
| **interval** | [**Interval**](Interval.md) |  | [optional] |
| **timewindow_ms** | **int** |  | [optional] |
| **fixed_timewindow** | [**FixedTimeWindow**](FixedTimeWindow.md) |  | [optional] |
| **quick_interval** | [**QuickTimeInterval**](QuickTimeInterval.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.history_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `History.model_validate(data)` or `History.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

